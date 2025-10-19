FROM python:3.13-slim
WORKDIR /programas/api-employees
RUN pip3 install "fastapi[standard]"
RUN pip3 install pydantic
COPY . .
CMD ["fastapi", "run", "./main.py", "--port", "8000"]
