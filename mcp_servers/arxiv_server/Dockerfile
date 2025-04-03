FROM python:3.12.9-slim

RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates
# Download the latest installer
ADD https://astral.sh/uv/install.sh /uv-installer.sh
# Run the installer then remove it
RUN sh /uv-installer.sh && rm /uv-installer.sh
# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.local/bin/:$PATH"
COPY . /app
WORKDIR /app
RUN uv init
RUN uv pip install --system -r requirements.txt 
CMD [ "python", "main.py" ]