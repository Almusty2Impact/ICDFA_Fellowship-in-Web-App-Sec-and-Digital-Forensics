## Stage 1: Suspected Drug Dealer Posted Ad on Craigslist
Visit ID	Time (Local)	URL ID	URL / Title	Transition	Interpretation
1-2	09:54:18	1	google.com/search?q=craigslist	5 (Omnibar)	User typed "craigslist" into the browser.
3-5	09:54:19	2,3,4	craigslist.org -> geo.craigslist.org -> baltimore.craigslist.org	0 (Link) + Redirects	User clicked the Craigslist link and was redirected to the Baltimore site.
6-8	09:54:22 - 09:54:39	5,6	accounts.craigslist.org/login/home	0 (Link) + Form Submit (7)	User navigated to the login page. At 09:54:39, they submitted the login form (Visit 8).
9-10	09:55:03	2,4	www.craigslist.org -> baltimore.craigslist.org	0 (Link)	User navigated back to the Baltimore homepage.
11-13	09:55:05	7,8,9	post.craigslist.org/...	0 (Link) + Redirects	User clicked "create a posting" and navigated to the posting workflow.
14	09:55:10	10	post.craigslist.org/...?s=cat	7 (Form Submit)	User selected a category and submitted the form.
15	09:55:15	11	post.craigslist.org/...?s=edit	7 (Form Submit)	User submitted the initial ad content.
16	09:58:13	12	post.craigslist.org/...?s=geoverify	7 (Form Submit)	User confirmed location.
17	09:58:17	13	post.craigslist.org/...?s=editimage	7 (Form Submit)	User navigated to image upload step.
18	09:58:19	14	post.craigslist.org/...?s=preview	7 (Form Submit)	User previewed the ad.
19	09:58:22	8	post.craigslist.org/...	7 (Form Submit)	User published the ad (Posting Confirmation).
20	09:58:27	15	post.craigslist.org/manage/7473121658	0 (Link)	User navigated to the management page for the newly published post.

## Stage 2: Interested Buyer Messaged Dealer & Dealer Replied with Transaction Details
Visit ID	Time (Local)	URL ID	URL / Title	Transition	Interpretation
21-23	09:58:31 - 09:58:39	16,17	baltimore.craigslist.org/hab/d/... -> google.com/search?q=gmail	0 (Link) -> 5 (Omnibar)	User clicked to view their own ad. Then typed "gmail" into the address bar.
24-36	09:58:40 - 09:59:26	18-29	google.com/gmail -> accounts.google.com/...	0 (Link) + Redirects	User navigated to Gmail and went through the login process (identifier and password challenge).
37-42	09:59:29 - 09:59:31	30-33	accounts.google.com/CheckCookie -> mail.google.com/mail/u/0/#inbox	0 (Link) + Redirects	Successful login. User arrives at the inbox unsub.fscs@gmail.com.
43	10:04:12	34	mail.google.com/mail/u/0/#inbox/WhctKKXXDrfC...	0 (Link)	User opens the email with subject "cheaper than Rx supplements - order".
44-45	10:04:35 - 10:04:46	35,36	...?compose=JHrtffdgkF... & ...?compose=DXDwSWwx...	0 (Link)	User clicks "Reply" twice, composing two responses to the order email.
46-48	10:04:52 - 10:56:47	34,33,37	mail.google.com/...	0 (Link)	User navigates back to the inbox. At 10:56:47, user opens a new email with the subject containing the TXID (txid: 517b2156...).

## Stage 3: Buyer Sent Payment & Dealer Confirmed Payment
Visit ID	Time (Local)	URL ID	URL / Title	Transition	Interpretation
49-50	10:56:52	38,39	google.com/url?q=https://imgur.com/dTgrkP7 -> imgur.com/dTgrkP7	0 (Link)	User clicks the Imgur link from the email and views the transaction proof. Download occurs at 10:56:58.
51-54	10:58:59 - 10:59:02	40,41	google.com/search?q=blockchain+explorer -> blockchain.com/explorer	5 (Omnibar) -> 0 (Link)	User types "blockchain explorer" and clicks the link to Blockchain.com.
55-58	10:59:06 - 10:59:21	42,43,44	blockchain.com/search?search=517b... -> blockchain.com/btc/tx/517b... -> blockchain.com/btc/address/38Rcs...	0 (Link)	User searches for the TXID, views the transaction, and then clicks on the Bitcoin wallet address 38RcsURW....
59-62	10:59:38 - 10:59:47	45,46	google.com/search?q=kraken -> kraken.com/en-us/sign-in	5 (Omnibar) -> 0 (Link)	User types "kraken" and clicks the sign-in link.
63-65	11:00:21 - 11:01:12	47,48,49	kraken.com/en-us/device-approval -> .../u/trade -> .../u/instant	0 (Link)	User approves the login device, then lands on the trading/instant page.
66-70	11:01:21 - 11:01:33	50-54	kraken.com/u/funding -> kraken.com/redirect?url=...mempool.space... -> mempool.space/tx/517b...	0 (Link)	User views funding page, then clicks a link that redirects to mempool.space to view the same transaction.
71	11:02:05	55	kraken.com/u/history/ledger	0 (Link)	User checks the Kraken ledger history.

## Stage 4: Dealer Shipped Drugs / Further Communication
Visit ID	Time (Local)	URL ID	URL / Title	Transition	Interpretation
72-74	11:02:32 - 11:02:56	56,57,37	mail.google.com/mail/u/0/#inbox/WhctKKXXDrfC...	0 (Link)	User navigates back to Gmail. Clicks reply to the "order" email twice more, then goes back to the "txid" email.

