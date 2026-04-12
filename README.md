# elouan-rousseau-tinyinsta

Le fichier locustfile.py a été généré grâce à Gemini.

Expérience 1 : Commande permettant de remplir la base de données pour le passage à l'échelle sur la charge
curl -X POST "http://127.0.0.1:8080/admin/seed" -d "users=1000" -d "posts=50000" -d "follows_min=20" -d "follows_max=20"

Expérience 2 : Commande permettant de remplir la base de données pour le passage à l'échelle sur la taille des données
curl -X POST "http://127.0.0.1:8080/admin/seed" -d "users=1000" -d "posts=100000" -d "follows_min=20" -d "follows_max=20"
