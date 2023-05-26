import serial
import psycopg2
import time
from datetime import datetime

temps = datetime.now()

#Etape de connection a la base de donnee

# Configuration de la base de données PostgreSQL
host_Name = 'localhost'
port_Adrdress = 5432
Database_name = 'detecteur'
user_id = 'postgres'
password_id = 'Marikoben10'

#Connexion à la base de données PostgreSQL
# Vérification de la connexion à la base de données PostgreSQL
try:
    conn = psycopg2.connect(
        host=host_Name,
        port=port_Adrdress,
        database=Database_name,
        user=user_id,
        password=password_id
    )
    print("Connecté à la base de données PostgreSQL")


except psycopg2.Error:
    print("Erreur lors de la connexion à la base de données PostgreSQL:", psycopg2.Error)
    exit()

# Configuration de la communication série (à adapter selon votre configuration)
serial_port = 'COM5'
baud_rate = 9600

# Ouverture de la connexion série avec l'Arduino
Ouverture = serial.Serial(serial_port, baud_rate)

#ETAPE DINSERTION DES DONNEE A LA BASE DE DONNEE
while True:
    # Lecture des données des capteurs depuis l'Arduino
        # Lecture des données depuis le port série
        #la connection serie fait des envoies sequencielle et pour chaque envoi je stock dans la variable correspondante
   
    Sen0018 = Ouverture.readline().decode().strip() 
    Dfr0034 = Ouverture.readline().decode().strip()  
    Sen0307 = Ouverture.readline().decode().strip()  
        

     # Créer un curseur pour exécuter des requêtes SQL
    cursor = conn.cursor()
   
    # Requête d'insertion

    query = "INSERT INTO receuillcap (id_cap,nom_cap,valeur_cap,temps) VALUES (%s, %s, %s,%s)"
    values = (9999, " Sen0018 " ,Sen0018,temps)

    stock = "INSERT INTO receuillcap (id_cap,nom_cap,valeur_cap,temps) VALUES (%s, %s, %s,%s)"
    value =  (9998, " Dfr0034 " ,Dfr0034,temps)

    type = "INSERT INTO receuillcap (id_cap,nom_cap,valeur_cap,temps) VALUES (%s, %s, %s,%s)"
    val =    (999, " Sen0307 " ,Sen0307,temps)

        # Exécution de la requête
    cursor.execute(query, values)
        # Exécution de la requête
    cursor.execute(stock, value)
        # Exécution de la requête
    cursor.execute(type, val)

    conn.commit()
   


     #ETAPE DE VERIFICATION (extraction)
# Exemple : Exécution d'une requête SELECT
    cursor.execute("SELECT * FROM receuillcap") #pour verifier

    records = cursor.fetchall() # Récupérer les résultats de la requête 
    print("Les donnees envoyer a la tables receuillcp de la base de donnee:")
    # Parcourir les résultats
    for record in records:
            # Traiter chaque ligne
        print(record)

    # Fermeture du curseur
    cursor.close()
    
