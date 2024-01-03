FROM python:3.11
WORKDIR /bot
COPY requirements.txt /bot/
RUN pip install -r requirements.txt
COPY . /bot
CMD python main.py MTE4OTkyMjY0NTY5NzkwNDc5MA.Ga7G6g.abZGM9KYoGleGLt6SlPAnB7vvlKX81kWd7pRFc