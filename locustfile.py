import random
from locust import HttpUser, task, between

class TinyInstaUser(HttpUser):
    # Un utilisateur attend entre 1 et 5 secondes entre chaque rechargement
    wait_time = between(1, 5)

    def on_start(self):
        """
        Cette fonction est exécutée une seule fois au démarrage de chaque utilisateur simulé.
        """
        # On choisit un utilisateur aléatoire parmi les 1000 que tu as générés
        self.username = f"user{random.randint(1, 1000)}" 
        
        # On le connecte à l'application
        self.client.post("/login", data={"username": self.username})

    @task
    def load_timeline(self):
        """
        C'est l'action principale : l'utilisateur rafraîchit sa timeline.
        On utilise l'endpoint API prévu à cet effet dans main.py pour un test plus précis.
        """
        # On appelle l'API timeline en passant le nom de l'utilisateur
        self.client.get(f"/api/timeline?user={self.username}")
