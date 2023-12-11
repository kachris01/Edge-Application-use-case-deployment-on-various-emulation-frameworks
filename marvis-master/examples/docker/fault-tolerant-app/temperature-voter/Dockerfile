FROM python:3-alpine

COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

COPY temperature_voter.py /temperature_voter.py

CMD python3 -u temperature_voter.py
