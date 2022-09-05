#!/usr/bin/env python3
import logging
import os


log_level = os.getenv("LOG_LEVEL", "WARNING").upper()

# ch -> console handler
# BOILERPLATE
# TODO: Usar funçao
# TODO: Usar lib externa (loguru)
log = logging.Logger("logs.py", log_level)
ch = logging.StreamHandler() # Console/Terminalstderr
ch.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s'
)
ch.setFormatter(fmt)
log.addHandler(ch)

"""
log.debug("Log debug")
log.info("Log info")
log.warning("Log warning")
log.error("Log error")
log.critical("Log critical")
"""


print("-" * 10)

try:
    1/0
except ZeroDivisionError as e:
    log.error("Deu erro. lol. %s", str(e) ) # logging não suporta f-string