FROM python
COPY . .
CMD ["python", "./count.py"]