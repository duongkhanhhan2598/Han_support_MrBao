from jwcrypto import jwk, jwe
from jwcrypto.common import json_encode, json_decode
from jose import jwk, jwt, jwe, jws
from jose.utils import base64url_decode, base64url_encode
import traceback
import base64
import json
import ujson

from cryptography import x509
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

rootCA = """-----BEGIN CERTIFICATE-----
MIIGJjCCBA6gAwIBAgIEW9smdTANBgkqhkiG9w0BAQsFADCBjDELMAkGA1UEBhMC
Vk4xDjAMBgNVBAgTBUhhbm9pMQ4wDAYDVQQHEwVIYW5vaTEwMC4GA1UEChMnTmF0
aW9uYWwgUGF5bWVudCBDb3Jwb3JhdGlvbiBvZiBWaWV0bmFtMRQwEgYDVQQLEwtJ
VCBTZWN1cml0eTEVMBMGA1UEAxMMTmFwYXMgUm9vdENBMCAXDTE4MTEwMTE1NDQ1
NVoYDzIwNTMxMTAxMTYxNDU1WjCBjDELMAkGA1UEBhMCVk4xDjAMBgNVBAgTBUhh
bm9pMQ4wDAYDVQQHEwVIYW5vaTEwMC4GA1UEChMnTmF0aW9uYWwgUGF5bWVudCBD
b3Jwb3JhdGlvbiBvZiBWaWV0bmFtMRQwEgYDVQQLEwtJVCBTZWN1cml0eTEVMBMG
A1UEAxMMTmFwYXMgUm9vdENBMIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKC
AgEAvESVXUS5HJJYga3Bm1lShNSF0FkqBTIzVvBjkpw54RPHI0gnuXOgQOmUgE8y
UvL/Ub+510eZzfNrtvx8a9rlC4SV/QfV74lmai0OJDbznuu2tExWjQpnb9U87pR8
MWHY3Uab1eKwpRDIZjqBXUzjCKeeZIgGtC2Au8qV6aRpgYOzzKapTyrP3vmKX1kn
rz0wehP7KwU3/hCXPw+7/TIcMPHKOIrvJQOKCgGFUMr3Y8bix3G1M4EM+ta+foTn
kWC5mojTrqPjIUGnWS+BDeoPkF/uqy1oNhTnZJj3RaCDE02Q0KzPWDC+Jr7DGHX/
+mVPL3uOm1qE/3Ge4UQsm2qqunY8kiZAlHFlccvZr0adyc5pE4CA0ThRvVctrLKe
980iYcakhr78Vxvf5FT0DEznNvvafoW96Lb2jx0vkSURM6VHrVPZH89RPp9eyUy4
/7nXJyWZjnmiRyippqqvlyOFDFYHa+ubNFjGBqXksk76P909/770bfCWsf6XZMfy
c0aVdLJ2l5nTTbCPEOIrZSVy8CHXvT1eXSXiUQELpXOTRBYdyPiXwH9/6nLGRjVV
T5zijTKO5JoVXEiq81AjtqExLKei6j/q38zg1jgJknT5XuCAY4vnYGMabb9cDV0o
Jevt6OlGOTK1IwXQnX4Jj/YFO7YPSHNy8mcLIrosJ50YkpECAwEAAaOBizCBiDAr
BgNVHRAEJDAigA8yMDE4MTEwMTE1NDQ1NVqBDzIwNTMxMTAxMTYxNDU1WjALBgNV
HQ8EBAMCAQYwHwYDVR0jBBgwFoAUoi7XniqXUlEOYGFFvLB9xG49+KUwHQYDVR0O
BBYEFKIu154ql1JRDmBhRbywfcRuPfilMAwGA1UdEwQFMAMBAf8wDQYJKoZIhvcN
AQELBQADggIBAKQ1Ml1yFbmAIp8N673fcJ6NgaJedbHlU8OjC1Yq2+GwBH9kA3r1
4rl2Q5YUbC3hVQqoQ+k2Pb3mzE6tj/60n7cf+U70eKtFyMe6RT3dQgIlloVfZU/9
PEqVjE7qF6xmLI7TYjZmzKhdoD+9jv8HwrVrbTufvzcvGOTt0CBHG7XqrPXO3dsK
rQtm9gVwGL6bnEjDtFYEPYcH3RAsDkXwwB4PtFYiBTxaN9BlHztxsgTO9W4vn8TP
CJ5e6h0AFLsn60s4t/ZSaJiL2pcAwuICMKk8ODWasPDfwy5pMaT9b3iWA1NiW/NS
E5pTnrGUHR0n2YgRAQ2gPzY0/sFbrk54+H5fDH/eIfmR6X/wADzE2HFftHM05Wvk
bkigLGFs97tu7A8853XqnEU4fgSypaQkalOGHovrvbhd6OGmnmtw+TUpRZzxcLEZ
OmDvwyZb0C22/l5foPzNkjiXNEdX8Bcii74khmoMTJMlN4IsVCUj6+WdrHdX8FHt
SD71TOGnu/ZVXdk5lKrsPe1c05wKHF1ctDqlEkrG0jtJ3CFhfrOeiDChHqIyC0Ps
nRK8n6GhFTTXfODBrUb5XiPYtERf2a+ActKG3pS+lctk5WUkTXdpxrpnyXqouFVp
pL4cDrT8c/ELy1hmoaP7tJgb7IFbg7EWHwhdLQrFdu8Z0nE2+n34gavU
-----END CERTIFICATE-----
"""

rootCA_pub = """-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAvESVXUS5HJJYga3Bm1lS
hNSF0FkqBTIzVvBjkpw54RPHI0gnuXOgQOmUgE8yUvL/Ub+510eZzfNrtvx8a9rl
C4SV/QfV74lmai0OJDbznuu2tExWjQpnb9U87pR8MWHY3Uab1eKwpRDIZjqBXUzj
CKeeZIgGtC2Au8qV6aRpgYOzzKapTyrP3vmKX1knrz0wehP7KwU3/hCXPw+7/TIc
MPHKOIrvJQOKCgGFUMr3Y8bix3G1M4EM+ta+foTnkWC5mojTrqPjIUGnWS+BDeoP
kF/uqy1oNhTnZJj3RaCDE02Q0KzPWDC+Jr7DGHX/+mVPL3uOm1qE/3Ge4UQsm2qq
unY8kiZAlHFlccvZr0adyc5pE4CA0ThRvVctrLKe980iYcakhr78Vxvf5FT0DEzn
NvvafoW96Lb2jx0vkSURM6VHrVPZH89RPp9eyUy4/7nXJyWZjnmiRyippqqvlyOF
DFYHa+ubNFjGBqXksk76P909/770bfCWsf6XZMfyc0aVdLJ2l5nTTbCPEOIrZSVy
8CHXvT1eXSXiUQELpXOTRBYdyPiXwH9/6nLGRjVVT5zijTKO5JoVXEiq81AjtqEx
LKei6j/q38zg1jgJknT5XuCAY4vnYGMabb9cDV0oJevt6OlGOTK1IwXQnX4Jj/YF
O7YPSHNy8mcLIrosJ50YkpECAwEAAQ==
-----END PUBLIC KEY-----
"""

interCA_pub = """-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEA676OWPh4cLEUE0UkcJLG
m8bCuIi9GhnAlUToeBoIcpr7qk2/Vw0g08ZVuDP5AMtJWgJT497RC0QEDjAAxlZs
gR5/+BinlJ/iuE/pe2QYCX4jNLdhl3HtZTkqjy1XJEA2u8xz/RqXF/Az8Vwmk5cQ
2q9srKNcF+h+3OYdWg3OWOE31XoVu3b8xQF5oPed8W6S8/ILzA6E0K9gihCHa4Kk
7Cg0vzAQLa2SyYBffR8yyDBtNVzgGaNDO+ZfLqOk6BDFBAazzEZoHuxhxW57sVfR
L+O2y7LfbGkwbPBGz+nKY1WJEaAlC9fU1wDmSy5WnV8+bCGzjuU9/3SSZ9X3ABcZ
/SGjacBngvmwJrG/IqrxfXgB9xVbtDptfcxu3A+fCRla4DLo6vDYv7WSiNGQyi90
fI4gk9lpbq2HAvVXn558YWdXUfbDznd4UaOhffruIGhag2r/g9eLVQPb4DNykG54
1AnQkL+Wo7i1sT+5fLiv8n1UxAfBaEb9I9fxs21CvtF+U4GeonBiXor+O1VVlYCx
/0IKvK7kdfWxvu3ascF8qiptjd/qHpnG6mVdH8C9pBGJg6C85lvl9CoDiPKBTXy1
XLOI6LpAq4ugLbdzKSS8rcTVE+zDBkHDkDxfh4l5rf6qlHPy4lwYbo/rZ1FM7anc
sCbBwoIRcF5hQlkAOELRpOsCAwEAAQ==
-----END PUBLIC KEY-----
"""

interCA = """-----BEGIN CERTIFICATE-----
MIIG7TCCBNWgAwIBAgIEW9smsjANBgkqhkiG9w0BAQsFADCBjDELMAkGA1UEBhMC
Vk4xDjAMBgNVBAgTBUhhbm9pMQ4wDAYDVQQHEwVIYW5vaTEwMC4GA1UEChMnTmF0
aW9uYWwgUGF5bWVudCBDb3Jwb3JhdGlvbiBvZiBWaWV0bmFtMRQwEgYDVQQLEwtJ
VCBTZWN1cml0eTEVMBMGA1UEAxMMTmFwYXMgUm9vdENBMB4XDTE4MTEwMTE3NTk1
MFoXDTQzMTEwMTE4Mjk1MFowgZQxCzAJBgNVBAYTAlZOMQ4wDAYDVQQIEwVIYW5v
aTEOMAwGA1UEBxMFSGFub2kxMDAuBgNVBAoTJ05hdGlvbmFsIFBheW1lbnQgQ29y
cG9yYXRpb24gb2YgVmlldG5hbTEUMBIGA1UECxMLSVQgU2VjdXJpdHkxHTAbBgNV
BAMTFE5hcGFzIEludGVybWVkaWF0ZUNBMIICIjANBgkqhkiG9w0BAQEFAAOCAg8A
MIICCgKCAgEA676OWPh4cLEUE0UkcJLGm8bCuIi9GhnAlUToeBoIcpr7qk2/Vw0g
08ZVuDP5AMtJWgJT497RC0QEDjAAxlZsgR5/+BinlJ/iuE/pe2QYCX4jNLdhl3Ht
ZTkqjy1XJEA2u8xz/RqXF/Az8Vwmk5cQ2q9srKNcF+h+3OYdWg3OWOE31XoVu3b8
xQF5oPed8W6S8/ILzA6E0K9gihCHa4Kk7Cg0vzAQLa2SyYBffR8yyDBtNVzgGaND
O+ZfLqOk6BDFBAazzEZoHuxhxW57sVfRL+O2y7LfbGkwbPBGz+nKY1WJEaAlC9fU
1wDmSy5WnV8+bCGzjuU9/3SSZ9X3ABcZ/SGjacBngvmwJrG/IqrxfXgB9xVbtDpt
fcxu3A+fCRla4DLo6vDYv7WSiNGQyi90fI4gk9lpbq2HAvVXn558YWdXUfbDznd4
UaOhffruIGhag2r/g9eLVQPb4DNykG541AnQkL+Wo7i1sT+5fLiv8n1UxAfBaEb9
I9fxs21CvtF+U4GeonBiXor+O1VVlYCx/0IKvK7kdfWxvu3ascF8qiptjd/qHpnG
6mVdH8C9pBGJg6C85lvl9CoDiPKBTXy1XLOI6LpAq4ugLbdzKSS8rcTVE+zDBkHD
kDxfh4l5rf6qlHPy4lwYbo/rZ1FM7ancsCbBwoIRcF5hQlkAOELRpOsCAwEAAaOC
AUswggFHMIHpBgNVHR8EgeEwgd4wgaeggaSggaGkgZ4wgZsxCzAJBgNVBAYTAlZO
MQ4wDAYDVQQIEwVIYW5vaTEOMAwGA1UEBxMFSGFub2kxMDAuBgNVBAoTJ05hdGlv
bmFsIFBheW1lbnQgQ29ycG9yYXRpb24gb2YgVmlldG5hbTEUMBIGA1UECxMLSVQg
U2VjdXJpdHkxFTATBgNVBAMTDE5hcGFzIFJvb3RDQTENMAsGA1UEAxMEQ1JMMTAy
oDCgLoYsaHR0cDovL2NybC5uYXBhcy5jb20udm4vQ1JML05hcGFzX1Jvb3RDQS5j
cmwwCwYDVR0PBAQDAgEGMB8GA1UdIwQYMBaAFKIu154ql1JRDmBhRbywfcRuPfil
MB0GA1UdDgQWBBTw25WZRRFFFP5MN+2nmPclZB+6EjAMBgNVHRMEBTADAQH/MA0G
CSqGSIb3DQEBCwUAA4ICAQBvpc6Vy5/3EQERfCcLlfLWlJjQODgScmuAMO6RjY4H
aURmDWHMXn0dNxUvhB4Tn91jCHp9bkx53vVo1HA0/ev0G7yjQCVhvMPJUdK9fDYf
mghAvUwRHLSDwn6x8vbQSZZhbkCuvBiOx0njBPVuilotHCAHZyngL/aEyWBPQcK5
1BupVYGnLUH05zYu+L8EZxj03fsI4TZutLCq8y6tUXNPhjZp5AYyfL72BxIJbb2g
WC7nGFJxcmWUJQmosnOHqVanBM/l4dJUxDEO8JvfhZXA5/sBtXXQ6WkHjN2j/qKb
ZR8YL5WJC0lInSNyK0LH/T3uBf7u9qdGsWLnAnOmmoGBD/iBFONH5EnggCKD0NDk
fpBkCJ/I8LNvSE2vS3oRmWLEt+XYXkCTuTRUWv7jCb8tV3KE4xH8Kikzwpsq/fzD
SrNzy8ZRtizlCrQjGsfTJ5uTgO7TlQsGIJqWO3FmaMRRpCz1FilQEb03t0kZQWcf
pJiKlIWEfS6yU22uk88FcHta341tO1F8PEGQ1lsEIVqudD5/eGWxdC+/QTzuy4v3
evEyYEbmHaOuk/LmRq1ztpuBx6fm8E/2KrrGTEBeqsTWFRbIuO7mIZgpFMWFxdtZ
yktRc9+KknC0W70/AOdtaru5Sm6L/iOLS1LoPldKk7HDi162YRMyDunphn3tGWVc
PQ==
-----END CERTIFICATE-----
"""

NAPAS_TGTT_PUB = """-----BEGIN CERTIFICATE-----
MIIEBTCCAu2gAwIBAgIJAMJYfSgXHJOkMA0GCSqGSIb3DQEBCwUAMIGYMQswCQYD
VQQGEwJWTjEOMAwGA1UECAwFSGFub2kxDjAMBgNVBAcMBUhhbm9pMTAwLgYDVQQK
DCdOYXRpb25hbCBQYXltZW50IENvcnBvcmF0aW9uIG9mIFZpZXRuYW0xFDASBgNV
BAsMC0lUIFNlY3VyaXR5MSEwHwYDVQQDDBhOYXBhcyBUR1RUIGZvciBOb25lIEJh
bmswHhcNMjIwODI2MDQxMTM5WhcNMjMwODI2MDQxMTM5WjCBmDELMAkGA1UEBhMC
Vk4xDjAMBgNVBAgMBUhhbm9pMQ4wDAYDVQQHDAVIYW5vaTEwMC4GA1UECgwnTmF0
aW9uYWwgUGF5bWVudCBDb3Jwb3JhdGlvbiBvZiBWaWV0bmFtMRQwEgYDVQQLDAtJ
VCBTZWN1cml0eTEhMB8GA1UEAwwYTmFwYXMgVEdUVCBmb3IgTm9uZSBCYW5rMIIB
IjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwXmMjbZjYjN0uJJ4cxl4deR7
zi2ZFheixQ/YFPVBBr2EaQ/dtu8r5KHiMwuaEWfPK+bEcNz69wa48V4oHlEmOOYw
2jw+i2iNyIri316bDCwxomhIF9FCAEs/K31RTMSk2rXcjMsRDbWnPt7DgSSeJfN4
jM85QI4A/udc2SkmWLmfMt4W2f+srZHe2gi5/i209WJPKzQvHe1asCO+mu+55MBu
b389jpMPEczqOmRJDRi3HPJB+E3Pm5MYIN+TjA4Kj/bT3fJKGI//5b/L+jHPFqjO
GxxaXmFPngYyDBoWRMFJlmvdqfvPp3Iy/8AWzVo7ROcyPgd9SH2Wk8/tC9RUywID
AQABo1AwTjAdBgNVHQ4EFgQUZFjIPnzpkFSfyiaP6utZdjm1R2gwHwYDVR0jBBgw
FoAUZFjIPnzpkFSfyiaP6utZdjm1R2gwDAYDVR0TBAUwAwEB/zANBgkqhkiG9w0B
AQsFAAOCAQEAYf0pdQ1X76nDa/q1E3/0O9hYWq1byE0eUj/CUOni0qg4jHaQ2nIG
FrC2DR/FVirZwzoQy6vnq9ivUR5HqPJi0YH5nhhZnEysG+EOJyONAq1UNicrAQmx
gNRbVnbJIvbND71jRNztCpna9/KPTzTifop72XOMUmIFU+ADt5l5nYYJfiMcvBfa
RAd3LoUSA45/FyiTH4VVqgirK4SbYm+m9W7C5DwuIBgu1sJCwtBI0ItR308fCgf6
RmTXMgLGOYkhCg1Vtskx3LsiFZFyPLmW0KjBgr6NK4Pquo9X2hqrWSWrxr9mVQnx
SDgu3hSn7UeKUPAQcf8KrhRgctxjBVzH9w==
-----END CERTIFICATE-----
"""

NAPAS_TGTT_PRIV = """-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDBeYyNtmNiM3S4
knhzGXh15HvOLZkWF6LFD9gU9UEGvYRpD9227yvkoeIzC5oRZ88r5sRw3Pr3Brjx
XigeUSY45jDaPD6LaI3IiuLfXpsMLDGiaEgX0UIASz8rfVFMxKTatdyMyxENtac+
3sOBJJ4l83iMzzlAjgD+51zZKSZYuZ8y3hbZ/6ytkd7aCLn+LbT1Yk8rNC8d7Vqw
I76a77nkwG5vfz2Okw8RzOo6ZEkNGLcc8kH4Tc+bkxgg35OMDgqP9tPd8koYj//l
v8v6Mc8WqM4bHFpeYU+eBjIMGhZEwUmWa92p+8+ncjL/wBbNWjtE5zI+B31IfZaT
z+0L1FTLAgMBAAECggEAJSieKR2Niu/NDCH9hkWvEB149clmLIsPlP+NBcFw4sWF
Z9RHRfo7mObKlfk1dwBUFt90fSTEAqvE2360/9WgHK+BVHjbnlTPXmPmXPZDmxvl
0IZsyj5DieDp2gVwlujxrJvfJx9dQB/SZk3MiMIqqalQTuMB4PclE9AF0iOIHOP8
EQ7qOECU48L5AUYsQiRr0OixjQON+/mmezKZVq4uqttMLXJ82Jc7WWuGfTcRvtSj
fswpZKJlYApZPzUrfOmA/yq9HS8E5zBgWoJLIqp020pIQ2lVpjAxuFHJqpaaamaZ
XVk8qksgBkgYWBDxIQHahAu8LyLqB9Ats2FQdClysQKBgQDuhGJApKC8yksQ6Bpn
xTXITupcra3JRUX8UYgJR7lLSTtk4aBnp3Umuxth1w+iea0Rm6lvXTAg+o/rxzcr
9fCZwKP/3wN4Qx8+SaeEcK9kpZjcAt+G/v7oHbtCCurb43F7XprYKEimA0oqyJV/
IWykvYRdkXUfHseyCx/BPnjwSQKBgQDPp/nOsz/gm003QKMZSe/uqDUQqH97mQB7
f0+SEqXWx7x1eaP4WsJ3luJYzSPmdgDXu2sw1oyWZaE3qtxa7ygpLz66Xvfji1eB
V7QuTEdXojzh5COAybJWFLuSdeGI/PYoj/3jSV3bVHfJaDeGFHKccwrh9S2RLWM0
3AO0WEVEcwKBgGEi5Oiyowt/zyZpgCd2tzqGeQeZa8cmQSRLB/3PifTRNDEXej38
gsdtN++WqDVhHEypek1yRCGKKYa6MQvkM0JKo/+WkVEu9NBnKqPTSHrSvfgL64CM
5L8fLJ3u2EsIy7SUiLczYLLLcC8QVWHa+OX2kKuSi4JLBMTLpvkKOjKRAoGBAMDN
VJq/QVLYvwPLBuQnCxfKo6J44AyxDYqctROKLuJRh0CHlV+1XRPOSxBqP6ft7nBf
OnIY8mV9rQdTo87meKJslFBUdtKVgMS92rSV7DOIlgCiYvhjzSoxi8q7mpEnVaJp
tzA94WAQeDvPgKYD/DoYcoVDsHA39QGSOfpLbtzTAoGBAOl8onQaknRdRhw8Tvri
SS1smOH8xQTq5SHfIF7el9KMyVFJ0ZNm4g145hWjWSvZh1BOTtvtXk2RUflpwWw0
HsntTz8wd8f7afcwRWou8YjgmNhxKDrWBYONDpS8e6wdbV9qaCA5sbZDopgqo2Kw
Tu7/CLglV+65IFiIfU3OjbF/
-----END PRIVATE KEY-----
"""

NAPS_QR_CER = """-----BEGIN CERTIFICATE-----
MIIGnjCCBIagAwIBAgINANntl+gAAAAAW1vVqzANBgkqhkiG9w0BAQsFADCBnzEL
MAkGA1UEBhMCVk4xDjAMBgNVBAgTBUhhbm9pMQ4wDAYDVQQHEwVIYW5vaTExMC8G
A1UEChMoTkFUSU9OQUwgUEFZTUVOVCBDT1JQT1JBVElPTiBPRiBWSUVUIE5BTTEW
MBQGA1UECxMNSVQgRGVwYXJ0bWVudDElMCMGA1UEAxMcTmFwYXMgSW50ZXJtZWRp
YXRlIEF1dGhvcml0eTAeFw0xODA4MzEwMzI3NTZaFw0yMTA4MzEwMzU3NTZaMIGW
MQswCQYDVQQGEwJWTjEOMAwGA1UECBMFSGFub2kxDjAMBgNVBAcTBUhhbm9pMTEw
LwYDVQQKEyhOQVRJT05BTCBQQVlNRU5UIENPUlBPUkFUSU9OIE9GIFZJRVQgTkFN
MRYwFAYDVQQLEw1JVCBEZXBhcnRtZW50MRwwGgYDVQQDExNOYXBhcyBRUlBheSBT
aWduaW5nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA2aKvObeKjPEY
ObkIpHsIpfQTSrUGREDbU1kBbyKliIGrZF6H4ZKQgBMa3OwW3SdjyuyX4KIKnvzP
Nd8gsTXwmwASWAEll3qF+Nhay38agRxi/R0NmKypbMPJvmdxvQyZ8qGWNKSx/Y2i
xkaLkYALMG3q4Dadu7bDO0xcZAwvlf+1b/h4/pe5QP57StlU+lOpb4v7MN9+f17Z
HCM1+t08ZQ0hJ1YvOM6C3CIKBKnWfrgGDnCerB5Jq9Her/q1mQ/sL3hwMihSzC89
xfBlj+5ZziunHJ7D5C9g2XFTk6gR/0Sh9z6N4PvUS1GdXvUDxaCaA5EC2mD8qqbL
Ov5+whwmywIDAQABo4IB3jCCAdowCwYDVR0PBAQDAgP4MB0GA1UdJQQWMBQGCCsG
AQUFBwMBBggrBgEFBQcDAjARBglghkgBhvhCAQEEBAMCBsAwggEEBgNVHR8Egfww
gfkwgbqggbeggbSkgbEwga4xCzAJBgNVBAYTAlZOMQ4wDAYDVQQIEwVIYW5vaTEO
MAwGA1UEBxMFSGFub2kxMTAvBgNVBAoTKE5BVElPTkFMIFBBWU1FTlQgQ09SUE9S
QVRJT04gT0YgVklFVCBOQU0xFjAUBgNVBAsTDUlUIERlcGFydG1lbnQxJTAjBgNV
BAMTHE5hcGFzIEludGVybWVkaWF0ZSBBdXRob3JpdHkxDTALBgNVBAMTBENSTDEw
OqA4oDaGNGh0dHA6Ly9jcmwubmFwYXMuY29tLnZuL0NSTC9OYXBhc19JbnRlcm1l
ZGlhdGVDQS5jcmwwKwYDVR0QBCQwIoAPMjAxODA4MzEwMzI3NTZagQ8yMDIxMDgz
MTAzNTc1NlowHwYDVR0jBBgwFoAUIRxfoyiPyPx1Ne8nFmcZgFRc9pUwHQYDVR0O
BBYEFC/+VgXXvkxbc5zhiLGXhQaWNtwKMAkGA1UdEwQCMAAwGQYJKoZIhvZ9B0EA
BAwwChsEVjguMQMCA6gwDQYJKoZIhvcNAQELBQADggIBAEWjuucrJlo+bEOvSAw0
m5liOgLwogUg7WHU6EgwNQaUcVNegW1kpJ5LapSE1LweyrBUwYx1+Ojj9hAarxyq
P90PzWd55bgrkdQdMZnCplFlKKp7HYupfb2dt/4yW4DWicNfhKF4dNXvIH/GafDx
SnU7yb4b+qoU/Tpc33pQpsc7j0FkgrVUTsKHx0RPYquBmQ/SRnak2GT8irgQnywu
rg8zuUaVUTwpdlltG6190g/HMa+fKae3QRtiETsLvszhgIteVFUNQgQI0FtzPnlJ
PyaIWDw07NfBgsA11/sas3+YMkUqrFddgKZbrzYblM/Lv5/cxf89bnpvyE0JzEEP
NrEjDCE8Pb9+PqcR1ehXhAzk040Z8Rilm5XqFVvFKFKvdzmaR1GGAm40kyMoNsAv
EMTeArF9XVyKK3tyZyhHk4QndmAecqfPgwiLVMg2VyzrK5ZLApUnIeZwEv2PmOqZ
NHk5BbHtyfojpSX9RzKI2NW+a0W1wug1uSZALBxNtbvsVa2RKmxlL4hE5ciytNoO
p4H6NQiUmQp/i0mCETplNYp3BDa6XOcj9nZ6ulAQmu3XPV8aWkEC8tc1VO9qZHYc
Dn7MFtDf2kSmvNxJdZtxGd/GVvaDcx0DMZFgpZM2uL75K4z3o9/TrhwXnZfQf7o/
Lr2TutTnqCQQBbQWUWSraL+r
-----END CERTIFICATE-----"""

UAT_PRIVATE = """-----BEGIN PRIVATE KEY-----
MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCdYNuqwpMSLNrg
RK2A8JmqoWRKFd/Ti8BdyZIJ4wEaON5HyIb7x/VkJ3HL/L4WYKXUih7iMxwyyOFJ
yZPramZWdk9x3+GRPohl8Q/EHUt5/MDUlRY8gzdQ5/4F/DFzSf8Ib5tnYjOoShEy
772xtEm6G3rzhKspdaGQXcA95/4pRALhGpAuRs26MYaif5QZAO2aAojpfX8NEKLK
qxTClHN3J4hJfNM08Ad9q4YZ3H/IRdGH6AjgD9uelUO8JYO6Y+sZtwk4L3T+Z2iG
Ys4gmjpsZcOhmNzPnMg1GJDZ/lYaZpef/j9U8WPL/3nsTqBIgjcAWUirmBuNq+WK
vXCm0KLlAgMBAAECggEALEU4Vc85NuYmResb0Ycc+vo+b3a6yVPpL5jJu30/bKRt
psy6Z+5GUb+ky8iTolDapTCbYm8VMhX/BdYuBY2fLxhF3dcoKUbpcJ/Amx7Qgga/
Ka2snSYeM+SmuQFJ2dAJbVKT6R+fP2piby0wc+Iu0Sr0ybbavSVpZuZwcxmlDe8y
TJ9cjPBFNOXElMTEDsZViU2WG6/hSAopo13Laf+Gc7CEGnMQ3oPTPADhMiWjbTbN
xgJmuXM/5L8HjG+HITaNMOMVLGJC4V5WTfcRrx+8+O9Bh/ZbZuifxbmXSxAjqrXZ
YJMuz2OvBXZOiBH3YqUvdmHWsOBg/7+WZewNlAGsOwKBgQDBWVpXDLc1PEEJy2YR
X1oOltp3tytMgNW3e/xQWAJBQqS5WHo1wgK5x9NNs9uBK5GoV9GMTO06PYMRvYTC
Tn1hBWS5fJoY1s//R3i9q2ovCqDSwOfBqEpJMTcs8g/yjVrZv3cVrT9epfCt90l7
NZ1ImrcwaZmk4DW5+IdLeKCMwwKBgQDQX6xEJxG+F/WJHXv3cg5KqBpHhAq2IpBB
MYP61Rt0mWivK5Dx120PgJbZFvyJO9K3vyfMrf3cnG3ORWCZpBa4FBTn1hYU9UH5
OmVmYFMc49wG/RAf5+yYqID8FVHBdXW4afPTAPvsikqJE2AfCB/etGDAgfBwsNsH
7MyU+lG3NwKBgCdGwGxIf/sHd2rG77/9r6yhBlYlVl1fGosAW7vydNrO7+layNCc
zbLxncH+FEwEDr20wTOP+OzIzBRRfGOAUEXiM5jeb+s1z+DaovNcm+Bcd1j4qNuV
FSoTHlM6BPVPs7HiDA3SOLpAWUjtn/awaHf0PdxOx1BP33ocu1cgdPTDAoGABBKq
qlZdKWsMeJaj8q0/DESG5vj0wKSiTzPpkYCS3c+V1T6zwZZlYlUwHaQuYXxS3RaW
b5DDEonYN5zxi29Cpmx2ECYGHnjAxl9W1g5x8XGevmA57XW6ES3R/5tnErH6EBW6
F1jAk9oMJOvFCDY/cTnzXi/sBDfgwCHnyc2uxTcCgYBTlteh9Su+obX5j39nuoil
iitQw3lqodZvmYquTaTjV4NgkmX2LwO3KsDFKRwmmiYIndvvUEXV6ixqfPMdxGjI
3adIQwO8jzRr3uXOjp3FyNb5kwHwQ7Er0ddTcHFuxA/TYBBjFcPAhW+GCvxkyKus
ZKgZl1JlzKaOdG+yTX9MNA==
-----END PRIVATE KEY-----
"""

UAT_CERT = """-----BEGIN CERTIFICATE-----
MIID1TCCAr2gAwIBAgIUDXPUp0uXAzG/xHDRaiMGet1Yo/8wDQYJKoZIhvcNAQEL
BQAwejELMAkGA1UEBhMCVk4xDDAKBgNVBAgMA0hDTTEMMAoGA1UEBwwDSENNMQ4w
DAYDVQQKDAVVQmFuazENMAsGA1UECwwEVUJJVDENMAsGA1UEAwwEVUJJVDEhMB8G
CSqGSIb3DQEJARYSaXRzdXBwb3J0QHViYW5rLnZuMB4XDTIzMDExMTExMDQzMFoX
DTI0MDExMTExMDQzMFowejELMAkGA1UEBhMCVk4xDDAKBgNVBAgMA0hDTTEMMAoG
A1UEBwwDSENNMQ4wDAYDVQQKDAVVQmFuazENMAsGA1UECwwEVUJJVDENMAsGA1UE
AwwEVUJJVDEhMB8GCSqGSIb3DQEJARYSaXRzdXBwb3J0QHViYW5rLnZuMIIBIjAN
BgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAnWDbqsKTEiza4EStgPCZqqFkShXf
04vAXcmSCeMBGjjeR8iG+8f1ZCdxy/y+FmCl1Ioe4jMcMsjhScmT62pmVnZPcd/h
kT6IZfEPxB1LefzA1JUWPIM3UOf+Bfwxc0n/CG+bZ2IzqEoRMu+9sbRJuht684Sr
KXWhkF3APef+KUQC4RqQLkbNujGGon+UGQDtmgKI6X1/DRCiyqsUwpRzdyeISXzT
NPAHfauGGdx/yEXRh+gI4A/bnpVDvCWDumPrGbcJOC90/mdohmLOIJo6bGXDoZjc
z5zINRiQ2f5WGmaXn/4/VPFjy/957E6gSII3AFlIq5gbjavlir1wptCi5QIDAQAB
o1MwUTAdBgNVHQ4EFgQUoivGyVlypxFc1Ozi1PfcNrE04e8wHwYDVR0jBBgwFoAU
oivGyVlypxFc1Ozi1PfcNrE04e8wDwYDVR0TAQH/BAUwAwEB/zANBgkqhkiG9w0B
AQsFAAOCAQEAbxb4eFh3hgZSq4IWHCImlE1eRwQKVw1onFZyjJsAVH4H0ECyD+bM
1wNEd6VUDA+bUNsD4bN1546l2/2QtcF0uSspl6r586zSfpjFlkHwt29cieNPUCZG
kxpQ/CZ6hXirEz0XUtlXmQ8mynyHpENn8uWPHtCKuOmaE+0JtFfOrW3y4uMXiGgx
WXeu88wAAHZhh7kIgdgqiLoJ41YHkDQ0GBY1G1k5RVNIPttQV7MtIxAkwKak4qwY
08Jw8N6daqM3rw1oVXUMKUKcRrs22CQ1CvAWjyd+zf03xcx0NkJsCs7Uxs8miU3n
ScB9CWJUot5ACHslpQsjqgOnPhTdNuUkkw==
-----END CERTIFICATE-----
"""

NAPAS_QRPAY_SIGN_PUB = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA2aKvObeKjPEYObkIpHsI
pfQTSrUGREDbU1kBbyKliIGrZF6H4ZKQgBMa3OwW3SdjyuyX4KIKnvzPNd8gsTXw
mwASWAEll3qF+Nhay38agRxi/R0NmKypbMPJvmdxvQyZ8qGWNKSx/Y2ixkaLkYAL
MG3q4Dadu7bDO0xcZAwvlf+1b/h4/pe5QP57StlU+lOpb4v7MN9+f17ZHCM1+t08
ZQ0hJ1YvOM6C3CIKBKnWfrgGDnCerB5Jq9Her/q1mQ/sL3hwMihSzC89xfBlj+5Z
ziunHJ7D5C9g2XFTk6gR/0Sh9z6N4PvUS1GdXvUDxaCaA5EC2mD8qqbLOv5+whwm
ywIDAQAB
-----END PUBLIC KEY-----
"""

# ENCODE DECODE

UBANK_PRIVATE = """-----BEGIN PRIVATE KEY-----
MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCdYNuqwpMSLNrg
RK2A8JmqoWRKFd/Ti8BdyZIJ4wEaON5HyIb7x/VkJ3HL/L4WYKXUih7iMxwyyOFJ
yZPramZWdk9x3+GRPohl8Q/EHUt5/MDUlRY8gzdQ5/4F/DFzSf8Ib5tnYjOoShEy
772xtEm6G3rzhKspdaGQXcA95/4pRALhGpAuRs26MYaif5QZAO2aAojpfX8NEKLK
qxTClHN3J4hJfNM08Ad9q4YZ3H/IRdGH6AjgD9uelUO8JYO6Y+sZtwk4L3T+Z2iG
Ys4gmjpsZcOhmNzPnMg1GJDZ/lYaZpef/j9U8WPL/3nsTqBIgjcAWUirmBuNq+WK
vXCm0KLlAgMBAAECggEALEU4Vc85NuYmResb0Ycc+vo+b3a6yVPpL5jJu30/bKRt
psy6Z+5GUb+ky8iTolDapTCbYm8VMhX/BdYuBY2fLxhF3dcoKUbpcJ/Amx7Qgga/
Ka2snSYeM+SmuQFJ2dAJbVKT6R+fP2piby0wc+Iu0Sr0ybbavSVpZuZwcxmlDe8y
TJ9cjPBFNOXElMTEDsZViU2WG6/hSAopo13Laf+Gc7CEGnMQ3oPTPADhMiWjbTbN
xgJmuXM/5L8HjG+HITaNMOMVLGJC4V5WTfcRrx+8+O9Bh/ZbZuifxbmXSxAjqrXZ
YJMuz2OvBXZOiBH3YqUvdmHWsOBg/7+WZewNlAGsOwKBgQDBWVpXDLc1PEEJy2YR
X1oOltp3tytMgNW3e/xQWAJBQqS5WHo1wgK5x9NNs9uBK5GoV9GMTO06PYMRvYTC
Tn1hBWS5fJoY1s//R3i9q2ovCqDSwOfBqEpJMTcs8g/yjVrZv3cVrT9epfCt90l7
NZ1ImrcwaZmk4DW5+IdLeKCMwwKBgQDQX6xEJxG+F/WJHXv3cg5KqBpHhAq2IpBB
MYP61Rt0mWivK5Dx120PgJbZFvyJO9K3vyfMrf3cnG3ORWCZpBa4FBTn1hYU9UH5
OmVmYFMc49wG/RAf5+yYqID8FVHBdXW4afPTAPvsikqJE2AfCB/etGDAgfBwsNsH
7MyU+lG3NwKBgCdGwGxIf/sHd2rG77/9r6yhBlYlVl1fGosAW7vydNrO7+layNCc
zbLxncH+FEwEDr20wTOP+OzIzBRRfGOAUEXiM5jeb+s1z+DaovNcm+Bcd1j4qNuV
FSoTHlM6BPVPs7HiDA3SOLpAWUjtn/awaHf0PdxOx1BP33ocu1cgdPTDAoGABBKq
qlZdKWsMeJaj8q0/DESG5vj0wKSiTzPpkYCS3c+V1T6zwZZlYlUwHaQuYXxS3RaW
b5DDEonYN5zxi29Cpmx2ECYGHnjAxl9W1g5x8XGevmA57XW6ES3R/5tnErH6EBW6
F1jAk9oMJOvFCDY/cTnzXi/sBDfgwCHnyc2uxTcCgYBTlteh9Su+obX5j39nuoil
iitQw3lqodZvmYquTaTjV4NgkmX2LwO3KsDFKRwmmiYIndvvUEXV6ixqfPMdxGjI
3adIQwO8jzRr3uXOjp3FyNb5kwHwQ7Er0ddTcHFuxA/TYBBjFcPAhW+GCvxkyKus
ZKgZl1JlzKaOdG+yTX9MNA==
-----END PRIVATE KEY-----
"""

UBANK_PUBLIC = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAnWDbqsKTEiza4EStgPCZ
qqFkShXf04vAXcmSCeMBGjjeR8iG+8f1ZCdxy/y+FmCl1Ioe4jMcMsjhScmT62pm
VnZPcd/hkT6IZfEPxB1LefzA1JUWPIM3UOf+Bfwxc0n/CG+bZ2IzqEoRMu+9sbRJ
uht684SrKXWhkF3APef+KUQC4RqQLkbNujGGon+UGQDtmgKI6X1/DRCiyqsUwpRz
dyeISXzTNPAHfauGGdx/yEXRh+gI4A/bnpVDvCWDumPrGbcJOC90/mdohmLOIJo6
bGXDoZjcz5zINRiQ2f5WGmaXn/4/VPFjy/957E6gSII3AFlIq5gbjavlir1wptCi
5QIDAQAB
-----END PUBLIC KEY-----
"""

enc = "eyJraWQiOiJTSy5PQ0UuQVVUIiwiYWxnIjoiUlMyNTYifQ.ZXlKcmFXUWlPaUpRU3k1VFJDNUxSVXNpTENKbGJtTWlPaUpCTVRJNFIwTk5JaXdpWVd4bklqb2lVbE5CTVY4MUluMC5iN3VNQUI3YnpsTXJSVmgwUWRlTjBQMFdKMGxpSGRQc1ZWTEd6bmt0T1BhYldVUldpeElGVllaVWVyZjY0SmJoNW40VWpSM0pURGctS1NiVVBYbDFpWXlkemN4Vm85NE5MUTFaSWlpVEhYbEpPdW84dFYzM0xQcTRnc2ZqV2N0c19UTm9kZE1wcVJ1cm9uNGJqdlJUcjUzSjNJeXBvM2xMd016aHdrWUdjWjY4cjJxcDA3NmcyMDJrRXVWY2tFRlBtdWQ2UDFjQnRSRDhKTEs1Y2J2aWdXQzhvR214cTUwTWxhUEtiN2NDcEpJRTY1MTdjUWNHWS1JMm1jSlJJeGxBbzdkY0NVcVFUTEIxSUdGZ3VjTWxiN3NwM2hITXdsX00yS1JlOUZlYzJVb2NYQjFvSjVPbDU3ZWpaczNoREhfZWpUd1pVME9vOThCN2pZXzE3ZjJ5TncuUGs0QlpPdklfNFlIMmYtRS5SZVZBSGx2a3BCZWRjYXJKMlNJZ21pbGVrQWtOQVM2V3UzZDFrZ19lc1pYdVRHNTZmY0xkbEItUDZIaUpzY09iOXhxeEs5VXZLa2ZDSHZQcU9MTlVrT0NmTVNBenhFTE42dW96d2J1MFNZckczQS5GMUpFQW9pcTdyaS1nbzJ5c0lQS1FR.LhGWb7a0ysjsSc1vutlKKshUjtTZzPwhJtcmpHPSHfNfOkuz9At8GTIMwb1-h3OJieSx1ujvK02iBjMDnwm15fiuGmmpWw1ZwR3679FIefXXsg-Jhu6KM_vJQ3TxCil-v4oyG9xRZGduCR9ICZH60E5d1fC606XIMsGWR0mPvJYI46y4VQIBGs5lhKaS7umbyxrsSulYHMzB9cPu1VJpC488mguaXHMzjP7r30bi81T63Ccw_hdRs2tQ1VpYPn7OxRXhge3lyH0LQI2xPqxuIjLJ4-Cr615cbvRR6nDukR0GEYWNAjkONgyvIyThLHdf2MlqgnGPDZmtCR8A1FVzDQ"


def decode(token):
    try:
        # print('token: ', token)
        # get the kid from the headers prior to verification
        headers = jwt.get_unverified_headers(token)
        print('headers: ', headers)

        # construct the public key
        public_key = jwk.construct(NAPAS_TGTT_PUB, headers['alg'])
        # get the last two sections of the token,
        # message and signature (encoded in base64)
        message, encoded_signature = str(token).rsplit('.', 1)
        # decode the signature
        decoded_signature = base64url_decode(encoded_signature.encode('utf-8'))
        # verify the signature
        if not public_key.verify(message.encode("utf8"), decoded_signature):
            return {
                'status': False,
                'errcode': 'AU02',
                'errMsg': 'signature verification failed',
                'verified': False,
            }
        print('signature successfully verified')
        # since we passed the verification, we can now safely
        # use the unverified claims
        encrypted_payload = message.split('.')[1]
        print('encrypted_payload: ', encrypted_payload)
        claims = b'{}'

        # decrypt JWE
        payload = base64url_decode(encrypted_payload.encode('utf-8')).decode()
        # print('payload: ', payload)
        print('TRUE')
        claims = jwe.decrypt(payload, UBANK_PRIVATE)
        return {
            'status': True,
            'verified': True,
            'claims': json.loads(claims.decode())
        }
    except Exception as e:
        print(traceback.format_exc())
        return {
            'status': False,
            'errcode': 'AU05',
            'errMsg': 'Token is invalid'
        }


def encode(payload):
    try:
        # print(payload)

        # pack JWE
        payload = jwe.encrypt(plaintext=payload.encode(), key=NAPAS_TGTT_PUB, kid='PK.SD.KEK', encryption='A256GCM',
                              algorithm="RSA1_5")

        # print('payload: ', payload)

        # pack JWS
        jws_token = jws.sign(payload=payload, key=UBANK_PRIVATE, headers={'kid': 'SK.OCE.AUT'}, algorithm='RS512')

        print('jws_token: ', jws_token)
        return jws_token
    except Exception as e:
        print(traceback.format_exc())
        return {
            'status': False,
            'errcode': 'AU05',
            'errMsg': 'Token is invalid'
        }


def sign_data(body):
    key = UAT_PRIVATE
    private_key = serialization.load_pem_private_key(key.encode('utf-8'), None)
    signature = private_key.sign(
        body.encode('utf-8'),
        padding.PKCS1v15(),
        hashes.SHA256()
    )
    signature = base64.b64encode(signature).decode()
    print('signature: ', signature)
    return signature


def verify_data(signature, data):
    # GET PUBLIC KEY
    # cer = serialization.load_pem_public_key(PUBLIC_KEY.encode())
    # GET PUBLIC KEY FROM CERTIFICATION
    cer = x509.load_pem_x509_certificate(UAT_CERT.encode()).public_key()
    print(cer)
    try:
        cer.verify(
            base64.b64decode(signature),
            data.encode(),
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        print('True')
        return True
    except InvalidSignature as e:
        print('InvalidSignature Exception============>', e)
        return False


# -------------------- TEST HELLO WORLD
# text = 'Hello World!'
# signature = sign_data(text)
# verify_data(signature,text)


# ---------------------- TEST MYSELF
# req_sample1 = {
#     "header": {
#         "requestor": {
#             "id": "901008",
#             "name": "Duong Khanh Han"
#         },
#         "reference-id": "f452f607-433f-42b7-bdeb-b04f05abb12",
#         "timestamp": 20230103041212,
#         "operation": "QRLOOKUP"
#     },
#     "payload": {
#         "payment_reference": "449316143527",
#         "qr_string": "00020101021138540010A0000007270126000697041901121000050925440206QRPUSH5204594453037045802VN5904Hanh6005HANOI620063045D12"
#     }
# }
# encode_data = json.dumps(json.dumps(req_sample1).replace(' ',''))
# signature = sign_data(json.dumps(req_sample1))
# # encode_data = json.dumps(req_sample1).replace(' ','')
# # signature = sign_data(str(req_sample1))
# verify_data(signature,encode_data)


# ---------------------- TEST 2
data4 = {
    "apiOperation": "QRUPI_PAYMENT",
    "timestamp": "20221107152913",
    "result": {
        "code": "68",
        "description": "Transaction failure. IST or IIB return 68",
        "status": "ERROR"
    },
    "payment": {
        "reference": "ecdd02d2-a9c2-33bf-e053-65fe020acd8e",
        "type": "QR_PUSH",
        "channel": "07",
        "transaction_local_date_time": "2022-11-07T15:29:13.000Z",
        "trace": "575107",
        "payment_reference": "202211071530092813",
        "end_to_end_reference": "202211071530092813",
        "exchange_rate": "2",
        "interbank_amount": "0.43",
        "interbank_currency": "840",
        "txid": "202211071530092813",
        "instruction_id": "202211071530092813"
    },
    "amount": "10000.00",
    "currency": "VND",
    "settlement_amount": "10000.00",
    "sender": {
        "full_name": "UPI",
        "address": {
            "line1": "TQ",
            "country": "TQ"
        }
    },
    "participant": {
        "originating_institution_id": "602907",
        "receiving_institution_id": "970423",
        "merchant_id": "104765941000012",
        "card_acceptor_id": "walletID",
        "card_acceptor_name": "NGUYEN TRAN CUONG",
        "card_acceptor_country": "VN",
        "merchant_category_code": "5941"
    },
    "recipient_account": "eyJraWQiOiJTSy5PQ0UuQVVUIiwiYWxnIjoiUlM1MTIifQ.ZXlKcmFXUWlPaUpRU3k1VFJDNUxSVXNpTENKbGJtTWlPaUpCTWpVMlIwTk5JaXdpWVd4bklqb2lVbE5CTVY4MUluMC5aRzBsLXpFczJ0OW9qSnItSHdmaW5aMlhESkdTbGNpT3Y1ZWc0R0x4NWw2VmpSWFVfMDhGNHlPRjZGeHE0QnA0UV9Bb0dGcUZJU2hFZ082V3VFNkFMUlBkZ3dOX3hEZzVPUjdVMTE0c3ZZUGkzWmFXREhlVy14bGU1ZFhWeV9hTFBKc19XRzVJV3hVeDMyVTRwZmdINVRZTWxYMTZ5SURkV25uMGdWNmVkejNPT0VpVmxBWWZPOXlvT1BDSXA3TGZiLUJ3ZDNORFQ3cXAxR0dOR2k0Y3NTSTB3MG8tR2RKbUxLV3pBSUxsZktFa3VsVHJ5VjhrT2dZUWhhaW1FRjE4cm9SemlMNHVSZVZHZjIyS3lBMEFBaUo2NHlqZGlwc24tcm1uMzVuNEg3Vm5VUE9kVzdnRFg3U1A1dWxyVDd3SUJIa3MwQ3JxNkNJZV81azZNV1BNQVEuRElKTG1zUUxydE1xOE5rYS50dUVsN0ZsUFl6bElQREoxeVFYVG16ajVEd3k5d3lRSEJzWURhSjNsdVZNQ1ZWTzdTMHlSbVJEaXVZNnFNa0NFdkJFYVpuNk5CTVBkNEJkd1M3bDl0Ylgzb3hpMWVPSGE4elN0UlpDV0ZHU3NqU0lLLkJpXzJ5MFVPa20xS0VoSHg4Y21JYUE.V80YIMh8XZizghjrFhTF4G8pRSGZa--F4uxEVgL6BWXG0b07njseT2UzUagkhdoY3X73oECFYPhtd7qT57l1kFzaSEjHWZufV3IDnf7XvG035xIRfk-jYF7a_RCRTkSxLcrvhJzLyGwLbjI-KmyogSllXThu5Yao7agb9lXYLe6dim9sLkQR-fTyQSlnOoUIkuHWNLaJnl1gzFnQGJnTFwHhN_mqEaBJ95nITo05LuqQuJNcKcdi6vlYvqJ2TMcZV3Dsa3slouVSVNXK8aMV8ZQcbiH0gyJ7GRgp2C7uOryriXy80Tbk6wMQ3dZeR0969WUw8vV7KFsByctK7yClzQ",
    "cardholder": {
        "billing_amount": "50000",
        "conversion_rate": "5.7534",
        "currency": "344"
    },
    "content_transfers": "Thanh toán QR UPI"
}
encode_data = json.dumps(json.dumps(data4).replace(' ', ''))
signature = sign_data(encode_data)
verify_data(signature, encode_data)

# ---------------------- TEST 1
# signtest2 = "Ka37vsOHykofudSBDJlAVLCl3bEGJg2d9kOaclLzthPo6tlnY3D2TIFdgRrmYs4XWe44UJ0+0sdMgb9lE4VWCqyW8TgXHmKKku9MB6R0J/XDbtIk50O1iPPffBo1AOC7eY5NzDr1+DFQkCBDsqdh113HT2t4veaEn0tjZqO45r17MVf/XUbU3/zo263ARHPQ69iXM6C9EVlDk1yQkXcxaOWkB72t9YvW65X8yOrnNS9VikV3lhkeT+bAyamUYaDs4cBQSePLwlbrCUSa3Tpf/NbmsUwniSEutayE2BzbHREdVHuBHOuNUrIWM6S2JhDH008JgmNv5gryHIEnfVkuyg=="
# encode_body4 = "{\"apiOperation\":\"QRUPI_PAYMENT\",\"timestamp\":\"20221107152913\",\"result\":{\"code\":\"68\",\"description\":\"Transaction failure. IST or IIB return 68\",\"status\":\"ERROR\"},\"payment\":{\"reference\":\"ecdd02d2-a9c2-33bf-e053-65fe020acd8e\",\"type\":\"QR_PUSH\",\"channel\":\"07\",\"transaction_local_date_time\":\"2022-11-07T15:29:13.000Z\",\"trace\":\"575107\",\"payment_reference\":\"202211071530092813\",\"end_to_end_reference\":\"202211071530092813\",\"exchange_rate\":\"2\",\"interbank_amount\":\"0.43\",\"interbank_currency\":\"840\",\"txid\":\"202211071530092813\",\"instruction_id\":\"202211071530092813\"},\"amount\":\"10000.00\",\"currency\":\"VND\",\"settlement_amount\":\"10000.00\",\"sender\":{\"full_name\":\"UPI\",\"address\":{\"line1\":\"TQ\",\"country\":\"TQ\"}},\"participant\":{\"originating_institution_id\":\"602907\",\"receiving_institution_id\":\"970423\",\"merchant_id\":\"104765941000012\",\"card_acceptor_id\":\"walletID\",\"card_acceptor_name\":\"NGUYEN TRAN CUONG\",\"card_acceptor_country\":\"VN\",\"merchant_category_code\":\"5941\"},\"recipient_account\":\"eyJraWQiOiJTSy5PQ0UuQVVUIiwiYWxnIjoiUlM1MTIifQ.ZXlKcmFXUWlPaUpRU3k1VFJDNUxSVXNpTENKbGJtTWlPaUpCTWpVMlIwTk5JaXdpWVd4bklqb2lVbE5CTVY4MUluMC5aRzBsLXpFczJ0OW9qSnItSHdmaW5aMlhESkdTbGNpT3Y1ZWc0R0x4NWw2VmpSWFVfMDhGNHlPRjZGeHE0QnA0UV9Bb0dGcUZJU2hFZ082V3VFNkFMUlBkZ3dOX3hEZzVPUjdVMTE0c3ZZUGkzWmFXREhlVy14bGU1ZFhWeV9hTFBKc19XRzVJV3hVeDMyVTRwZmdINVRZTWxYMTZ5SURkV25uMGdWNmVkejNPT0VpVmxBWWZPOXlvT1BDSXA3TGZiLUJ3ZDNORFQ3cXAxR0dOR2k0Y3NTSTB3MG8tR2RKbUxLV3pBSUxsZktFa3VsVHJ5VjhrT2dZUWhhaW1FRjE4cm9SemlMNHVSZVZHZjIyS3lBMEFBaUo2NHlqZGlwc24tcm1uMzVuNEg3Vm5VUE9kVzdnRFg3U1A1dWxyVDd3SUJIa3MwQ3JxNkNJZV81azZNV1BNQVEuRElKTG1zUUxydE1xOE5rYS50dUVsN0ZsUFl6bElQREoxeVFYVG16ajVEd3k5d3lRSEJzWURhSjNsdVZNQ1ZWTzdTMHlSbVJEaXVZNnFNa0NFdkJFYVpuNk5CTVBkNEJkd1M3bDl0Ylgzb3hpMWVPSGE4elN0UlpDV0ZHU3NqU0lLLkJpXzJ5MFVPa20xS0VoSHg4Y21JYUE.V80YIMh8XZizghjrFhTF4G8pRSGZa--F4uxEVgL6BWXG0b07njseT2UzUagkhdoY3X73oECFYPhtd7qT57l1kFzaSEjHWZufV3IDnf7XvG035xIRfk-jYF7a_RCRTkSxLcrvhJzLyGwLbjI-KmyogSllXThu5Yao7agb9lXYLe6dim9sLkQR-fTyQSlnOoUIkuHWNLaJnl1gzFnQGJnTFwHhN_mqEaBJ95nITo05LuqQuJNcKcdi6vlYvqJ2TMcZV3Dsa3slouVSVNXK8aMV8ZQcbiH0gyJ7GRgp2C7uOryriXy80Tbk6wMQ3dZeR0969WUw8vV7KFsByctK7yClzQ\",\"cardholder\":{\"billing_amount\":\"50000\",\"conversion_rate\":\"5.7534\",\"currency\":\"344\"},\"content_transfers\":\"Thanh toán QR UPI\"}"
# verify_data(signtest2, encode_body4)





