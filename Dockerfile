FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

COPY . .
RUN pip3 install -r src/configs/requirements.txt
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]