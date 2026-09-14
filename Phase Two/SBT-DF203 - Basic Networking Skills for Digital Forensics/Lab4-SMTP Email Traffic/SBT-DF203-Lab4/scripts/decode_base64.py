import base64

# Captured Base64 values from the SMTP AUTH LOGIN exchange
samples = {
    'Username': 'Z3VycGFydGFwQHBhdHJpb3RzLmlu',
    'Password': 'cHVuamFiQDEyMw=='
}

print("=== Offline Base64 Decode Results ===")
for label, value in samples.items():
    try:
        decoded = base64.b64decode(value).decode('utf-8', errors='replace')
        if label == 'Password':
            # Mask the password in output for safe reporting
            masked = decoded[:1] + '*' * (len(decoded) - 2) + decoded[-1:] if len(decoded) > 2 else '***'
            print(f"{label}: {masked}  (masked for reporting)")
        else:
            print(f"{label}: {decoded}")
    except Exception as exc:
        print(f"{label}: decode failed: {exc}")
