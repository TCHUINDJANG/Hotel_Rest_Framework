Ce projet illustre une architecture de microservices pour une application de gestion hotelliere utilisant Django. Le backend se compose de trois microservices Django : « Email », « reservation » et « Hotels », chacun équipé de sa propre base de données dédiée. RabbitMQ facilite la communication asynchrone entre ces microservices. Le frontend, développé en React, est conteneurisé et NGINX agit comme un proxy inverse.


Microservices

email-service:Microservice Django gérant les fonctionnalités liées au courrier électronique.
Hotels-services : Microservice Django gérant le traitement et l'exécution des hotels
Reservations-services : Microservice Django gérant les reservations

Bases de données

Chaque microservice Django utilise sa base de données dédiée. Pour les besoins de ce modèle de base, nous utiliserons les bases de données PostgreSQL pour les reservations et les emails et MongoDB pour les hotels.

Communication via RabbitMQ

Les microservices communiquent de manière asynchrone via RabbitMQ, qui fait office de courtier de messages. Des événements tels que les reservations en ligne , les mises à jour de reservations et les notifications par e-mail sont échangés entre les microservices, garantissant ainsi une architecture découplée.


Technologies back-end

Django : Les microservices backend sont développés à l'aide de Django, offrant un framework Web de haut niveau pour créer des applications robustes et évolutives.

RabbitMQ : courtier de messages asynchrones facilitant la communication entre les microservices Django.

PostgreSQL, MongoDB, MySQL : Bases de données choisies en fonction des exigences spécifiques de chaque microservice Django.

L'extrémité avant

L'interface utilisateur graphique (GUI) de notre application est construite avec Angular web et ionic mobile, offrant une expérience intuitive et réactive aux utilisateurs interagissant avec la plateforme de gestion d'hotel .

Proxy inverse NGINX

Lorsque les microservices et l'interface graphique sont derrière NGINX, la communication entre eux implique généralement des API basées sur HTTP. NGINX sert de proxy inverse, acheminant les requêtes entre l'interface graphique et les microservices. Voici quelques bonnes pratiques pour faciliter la communication dans une telle configuration :

API RESTful
Gestion des versions d'API
Équilibrage de charge
Résiliation SSL


Docker Compose

L'ensemble de l'application est orchestré à l'aide de Docker Compose, permettant un déploiement et une mise à l'échelle faciles des microservices Django et des composants frontend.

Commencer

1- Cloner ce dépôt : Je vais mettre le lien github du projet ici
2 -Accédez au répertoire du projet : cd microservices-template
3-Exécutez l’application à l’aide de Docker Compose :docker-compose up

Visitez les URL suivantes pour interagir avec différents composants :
Front-end : http://localhost:80
Interface utilisateur de gestion RabbitMQ : http://localhost:15672 (nom d'utilisateur : guest, mot de passe : guest)