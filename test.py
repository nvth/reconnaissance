import google.generativeai as genai
import os


api_key = "AIzaSyCKzRH4lsuv7gs4dz-GnfMXn2OoUIrVYtE"  

genai.configure(api_key=api_key)

model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# prompt_parts = [
#   genai.upload_file("test.jpeg"),  # pass the path to your image
#   "Describe the image.",  # text prompt (can be before, after, or interleaved)
# ]


output_raw = """
{    [ [92mazure-domain-tenant [0m] [ [94mhttp [0m] [ [34minfo [0m] https://login.microsoftonline.com:443/tesla.com/v2.0/.well-known/openid-configuration [ [96m"9026c5f4-86d0-4b9f-bd39-b7d4d0fb4674" [0m]
[ [92mcookies-without-httponly [0m] [ [94mjavascript [0m] [ [34minfo [0m] tesla.com [ [96m"akavpau_zezxapz5yf" [0m]
[ [92mwaf-detect [0m: [1;92makamai [0m] [ [94mhttp [0m] [ [34minfo [0m] https://tesla.com
[ [92mtls-version [0m] [ [94mssl [0m] [ [34minfo [0m] tesla.com:443 [ [96m"tls12" [0m]
[ [92mtls-version [0m] [ [94mssl [0m] [ [34minfo [0m] tesla.com:443 [ [96m"tls13" [0m]
[ [92mgoogle-floc-disabled [0m] [ [94mhttp [0m] [ [34minfo [0m] https://tesla.com
[ [92mtech-detect [0m: [1;92makamai [0m] [ [94mhttp [0m] [ [34minfo [0m] https://tesla.com
[ [92mrdap-whois [0m: [1;92msecureDNS [0m] [ [94mhttp [0m] [ [34minfo [0m] https://rdap.verisign.com/com/v1/domain/tesla.com [ [96m"false" [0m]
[ [92mrdap-whois [0m: [1;92mstatus [0m] [ [94mhttp [0m] [ [34minfo [0m] https://rdap.verisign.com/com/v1/domain/tesla.com [ [96m"server update prohibited" [0m, [96m"client delete prohibited" [0m, [96m"client transfer prohibited" [0m, [96m"client update prohibited" [0m, [96m"server delete prohibited" [0m, [96m"server transfer prohibited" [0m]
[ [92mrdap-whois [0m: [1;92mregistrationDate [0m] [ [94mhttp [0m] [ [34minfo [0m] https://rdap.verisign.com/com/v1/domain/tesla.com [ [96m"1992-11-04T05:00:00Z" [0m]
[ [92mrdap-whois [0m: [1;92mlastChangeDate [0m] [ [94mhttp [0m] [ [34minfo [0m] https://rdap.verisign.com/com/v1/domain/tesla.com [ [96m"2024-10-02T10:15:20Z" [0m]
[ [92mrdap-whois [0m: [1;92mexpirationDate [0m] [ [94mhttp [0m] [ [34minfo [0m] https://rdap.verisign.com/com/v1/domain/tesla.com [ [96m"2026-11-03T05:00:00Z" [0m]
[ [92mrdap-whois [0m: [1;92mnameServers [0m] [ [94mhttp [0m] [ [34minfo [0m] https://rdap.verisign.com/com/v1/domain/tesla.com [ [96m"A28-65.AKAM.NET" [0m, [96m"A9-67.AKAM.NET" [0m, [96m"EDNS69.ULTRADNS.BIZ" [0m, [96m"EDNS69.ULTRADNS.ORG" [0m, [96m"A1-12.AKAM.NET" [0m, [96m"A10-67.AKAM.NET" [0m, [96m"A7-66.AKAM.NET" [0m, [96m"EDNS69.ULTRADNS.COM" [0m, [96m"EDNS69.ULTRADNS.NET" [0m, [96m"A12-64.AKAM.NET" [0m]
[ [92mhttp-missing-security-headers [0m: [1;92mx-content-type-options [0m] [ [94mhttp [0m] [ [34minfo [0m] https://tesla.com
[ [92mhttp-missing-security-headers [0m: [1;92mx-permitted-cross-domain-policies [0m] [ [94mhttp [0m] [ [34minfo [0m] https://tesla.com
[ [92mhttp-missing-security-headers [0m: [1;92mreferrer-policy [0m] [ [94mhttp [0m] [ [34minfo [0m] https://tesla.com
[ [92mhttp-missing-security-headers [0m: [1;92mcross-origin-resource-policy [0m] [ [94mhttp [0m] [ [34minfo [0m] https://tesla.com
[ [92mhttp-missing-security-headers [0m: [1;92mcontent-security-policy [0m] [ [94mhttp [0m] [ [34minfo [0m] https://tesla.com
[ [92mhttp-missing-security-headers [0m: [1;92mclear-site-data [0m] [ [94mhttp [0m] [ [34minfo [0m] https://tesla.com
[ [92mhttp-missing-security-headers [0m: [1;92mcross-origin-embedder-policy [0m] [ [94mhttp [0m] [ [34minfo [0m] https://tesla.com
[ [92mhttp-missing-security-headers [0m: [1;92mcross-origin-opener-policy [0m] [ [94mhttp [0m] [ [34minfo [0m] https://tesla.com
[ [92mhttp-missing-security-headers [0m: [1;92mx-frame-options [0m] [ [94mhttp [0m] [ [34minfo [0m] https://tesla.com
[ [92mcaa-fingerprint [0m] [ [94mdns [0m] [ [34minfo [0m] tesla.com
[ [92mmx-fingerprint [0m] [ [94mdns [0m] [ [34minfo [0m] tesla.com [ [96m"10 tesla-com.mail.protection.outlook.com." [0m]
[ [92mmx-service-detector [0m: [1;92mOffice 365 [0m] [ [94mdns [0m] [ [34minfo [0m] tesla.com
[ [92mnameserver-fingerprint [0m] [ [94mdns [0m] [ [34minfo [0m] tesla.com [ [96m"a28-65.akam.net." [0m, [96m"a10-67.akam.net." [0m, [96m"a1-12.akam.net." [0m, [96m"a9-67.akam.net." [0m, [96m"a7-66.akam.net." [0m, [96m"a12-64.akam.net." [0m, [96m"edns69.ultradns.com." [0m]
[ [92mdmarc-detect [0m] [ [94mdns [0m] [ [34minfo [0m] _dmarc.tesla.com [ [96m""v=DMARC1; p=reject; pct=100; rua=mailto:n2ju30bc@ag.dmarcian.com; ruf=mailto:n2ju30bc@fr.dmarcian.com; fo=1"" [0m]
[ [92mssl-issuer [0m] [ [94mssl}
"""
dirty_text = f""" 
{output_raw}
"""
prompt = f"""
Hãy làm sạch đoạn văn sau: loại bỏ ký tự màu, mã định dạng và các ký tự không cần thiết khác. 

{dirty_text}
"""

response = model.generate_content(prompt)

print(response.text)