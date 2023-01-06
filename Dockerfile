FROM python:3.11
RUN mkdir -p /home/risk/
WORKDIR /home/risk/
ADD ./* /home/risk/
RUN apt update \
    && apt -y upgrade \
    && pip install -r /home/risk/requirements.txt
VOLUME /home/risk/run/
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "risk_neutral_player.wsgi:application"]