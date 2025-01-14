# Préparation de la solution d'IA pour la mise en production (cours-A61)

---

## Les problèmes que j'ai rencontré...

#### Bibliothèques dans leurs versions les plus récentes
Lors de l'installation des dépendances, deux bibliothèques avec leur dernière version se sont retrouvées dans l'environnement de développement. Les versions de ces deux bibliothèques (Jinja2 et Werkzeug) avaient délesté des classes qui étaient appelé par les autres bibliothèques. Avec l'aide de **chatGPT**, j'ai demandé quelle version de jinja2/werkzeug contenait les classes manquantes. Et avec la réponse retournée par **chatGPT**, j'ai rétrogradé les bibliothèques et j'ai mis à jour le fichier **requirements.txt** pour installer explicitement les deux bibliothèques avec les versions compatibles avec le projet.


#### Concaténation
![image](https://github.com/user-attachments/assets/1fe26733-3db6-47ca-95e3-ae4a175bd33b)
Dans le code, python a essayé de concaténer deux objets (objet **path** et objet **string**) et une erreur apparaissait. J'ai ré-écris le code pour obtenir le bon résultat et j'ai dû le faire pour d'autres parties du code qui se comportait de la même façon.

#### Étape 13 (CircleCI)
![image](https://github.com/user-attachments/assets/2a809d3d-ac1a-495e-bfb5-02169aa1dd98)

