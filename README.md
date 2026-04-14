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

### Graphique expérience 1 : 

<img width="1000" height="600" alt="conc" src="https://github.com/user-attachments/assets/d8938aa6-385d-4899-a209-d365b882bb6a" />

Suite à notre première expérience, nous pouvons remarquer que le temps moyen par requête est similaire de 1 à 100 utilisateurs et que ces temps de réponses sont rapides (moins de 150ms).

Mais à partir de 500 utilisateurs le temps moyen par requête explose car l'application ne peut pas traiter immédiatement ce flux. Lors du troisième run, grâce à l'augmentation des instances, le temps moyen n'est que de 126ms, ce qui explique la très grande variance qu'on peut observer sur cette colonne.

Pour 1000 utilisateurs, le temps moyen est inférieur à celui pour 500 utilisateurs, car l'infrastructure s'est adaptée à la charge en créant un grand nombre d'instances, mais la variance reste très grande, ce qui montre que le système reste tout de même instable.

Pour cette expérience, on peut en conclure que l'application est capable de passer à l'échelle sur la charge, pas par l'efficacité de son code mais seulement grâce à son infrastructure Cloud qui crée jusqu'à 20 instances. On remarque également que ce passage à l'échelle a créé une forte instabilité et des temps de latence très lents lors du pic soudain à 500 utilisateurs.


### Graphique expérience 2 : 

<img width="1000" height="600" alt="fanout" src="https://github.com/user-attachments/assets/031882b6-11c6-4d91-aef8-04fece5e5530" />
