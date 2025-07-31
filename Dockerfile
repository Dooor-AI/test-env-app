FROM python:3.11-slim

# Using confidential-space-debug image - but still need to declare allowed env vars
LABEL "tee.launch_policy.allow_env_override"="APP_NAME,ENVIRONMENT,VERSION,PORT,NODE_ENV"
LABEL "tee.launch_policy.allow_log_redirect"="always"

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .

EXPOSE 8080

CMD ["python", "app.py"] 