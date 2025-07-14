FROM python:3.12

WORKDIR /main

COPY . .

RUN pip install uv

RUN uv venv .venv && . .venv/bin/activate && uv pip install --system -r pyproject.toml

CMD ["python", "-u", "main.py"]

# Install all the dependencies:    sudo docker build -t backend-configs .
# Run the project:    sudo docker run -it --rm backend-configs