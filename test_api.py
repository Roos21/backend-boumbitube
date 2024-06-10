import requests
import json

# URL de votre API (à adapter en fonction de votre configuration)
url = "http://127.0.0.1:8000/event/event-ticket/reservation"

# Données à envoyer dans la requête POST
data = {
    "event": "6rBNXA1",
    "buyer": "epA6WQ3",
    "is_reserved": True,
    "reservation_expiry": "2024-06-09T12:00:00Z",
    "is_vip": True,
    "is_big": False
}

# En-têtes HTTP, si nécessaire (par exemple pour l'authentification)
headers = {
    'Content-Type': 'application/json',
}

# Envoi de la requête POST
response = requests.post(url, data=json.dumps(data), headers=headers)

# Affichage de la réponse
if response.status_code == 201:
    print("Ticket créé avec succès!")
    print("Réponse:", response.json())
else:
    print(f"Échec de la création du ticket. Statut: {response.status_code}")
    print("Erreur:", response.json())
