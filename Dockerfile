FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN useradd --create-home --shell /usr/sbin/nologin appuser
RUN chown -R appuser:appuser /app

COPY --chown=appuser:appuser app.py .
COPY --chown=appuser:appuser tests/ ./tests/

EXPOSE 5000

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:5000/').read()"

USER appuser

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
