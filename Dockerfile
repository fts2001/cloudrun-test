FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

RUN pip install --no-cache-dir -r requirements.txt --root-user-action=ignore

EXPOSE 5555

CMD ["python", "app.py"]
