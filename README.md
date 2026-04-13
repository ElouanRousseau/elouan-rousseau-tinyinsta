# elouan-rousseau-tinyinsta

Le fichier locustfile.py a été généré grâce à Gemini.

### Expérience 1 : Passage à l'échelle sur la charge
Commande permettant de remplir la base de données :
```bash
curl -X POST "[http://127.0.0.1:8080/admin/seed](http://127.0.0.1:8080/admin/seed)" -d "users=1000" -d "posts=50000" -d "follows_min=20" -d "follows_max=20"
```

### Expérience 2 : Passage à l'échelle sur la taille des données
Commande permettant de remplir la base de données : 
```bash
curl -X POST "http://127.0.0.1:8080/admin/seed" -d "users=1000" -d "posts=100000" -d "follows_min=20" -d "follows_max=20"
```
On ajoute ensuite pour tester avec 40 puis 60 followees.
