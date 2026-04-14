# elouan-rousseau-tinyinsta

URL de la webapp : https://tp1-elouanrousseau.ew.r.appspot.com 

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

<img width="1000" height="600" alt="conc" src="https://github.com/user-attachments/assets/d8938aa6-385d-4899-a209-d365b882bb6a" />

<img width="1000" height="600" alt="fanout" src="https://github.com/user-attachments/assets/031882b6-11c6-4d91-aef8-04fece5e5530" />
