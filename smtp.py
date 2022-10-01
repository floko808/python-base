#!/usr/bin/env python3
"""exemplo de envio de emails"""
import smtplib

SERVER = "localhost"
PORT = 8025



FROM = "eu@yo.com"
TO = ["zino@arrombado.com", "zeze@arrombado.com"]
SUBJECT = "E-mail via Pyhton"
TEXT = """\
E-mail enviado pelo python para os arrombados.
<b>ArROmbADoS</b>
"""


# SMTP
MESSAGE = f"""From: {FROM}
To: {", ".join(TO)}
Subject: {SUBJECT}

{TEXT}
"""


with smtplib.SMTP(host=SERVER, port=PORT) as server:
    server.sendmail(FROM, TO, MESSAGE.encode("utf-8"))

