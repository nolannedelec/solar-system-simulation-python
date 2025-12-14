FROM python:3.10-slim
# dire à Matplotlib de pas planter
# force le mode agg pour sauvegarder des fichiers au lieu d'afficher des fenêtres
ENV MPLBACKEND=Agg
WORKDIR /app
# installation des dépendances scientifiques
RUN pip install --no-cache-dir numpy matplotlib
COPY . .
CMD ["python", "runge_kutta.py"]
