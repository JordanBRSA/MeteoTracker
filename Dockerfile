FROM python:3.12-slim

WORKDIR /app

# Copier seulement le fichier requirements.txt pour profiter du cache Docker
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code
COPY . .

# Exposer le port Flask
EXPOSE 5000

# Commande par défaut
ENTRYPOINT ["python", "main.py"]

