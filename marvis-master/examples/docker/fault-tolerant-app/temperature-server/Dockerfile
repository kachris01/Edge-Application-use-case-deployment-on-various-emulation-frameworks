FROM python:3-alpine

COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

COPY temperature_server.py /temperature_server.py

CMD python3 -u /temperature_server.py
