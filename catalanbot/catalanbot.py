import praw
import pdb
import re
import os
import random

# Authenticate with Reddit API
reddit = praw.Reddit(
    user_agent="",
    client_id="",
    client_secret="",
    username="",
    password=""
)

#Create a txt file to avoid responding twice to same comments
if not os.path.isfile("catbot_replied_to.txt"):
    comments_replied_to = []
else:
    with open("catbot_replied_to.txt", "r") as f:
       comments_replied_to = f.read()
       comments_replied_to = comments_replied_to.split("\n")
       comments_replied_to = list(filter(None, comments_replied_to))

def remove_comments(reddit, items_to_watch):
    # Get comments from subreddit
    subreddit = reddit.subreddit("catalunya")
    comments = subreddit.comments(limit=100)
    # Loop through comments
    for comment in comments:
        if comment.id not in comments_replied_to:
        # Convert the comment body to lowercase
            comment_body = comment.body.lower()
            # Split the comment body into words
            words = comment_body.split()
            # Check if at least two items from the items_to_watch list are present in the words list
            contains_enough_items = sum(item in words for item in items_to_watch) >= 2
            if contains_enough_items:
                # Remove the comment as a moderator
                comment.mod.remove()
                comments_replied_to.append(comment.id)
                with open("catbot_replied_to.txt", "w") as f:
                    for comment_id in comments_replied_to:
                        f.write(comment_id + "\n")

# Lost of words that trigger removal
items_to_watch = ["y", "cuando", "todo", "también", "fue", "había", "muy", "años", "hasta", "porque", "vez", "hay", "puede", "todos", "tiene", "donde", "tiempo", "mismo", "ahora", "otro", "después", "otros", "aunque", "otra", "hace", "gobierno", "durante", "siempre", "dijo", "país", "según", "menos", "año", "antes", "estado", "nada", "hacer", "estaba", "poco", "presidente", "mayor", "ayer", "hecho", "mucho", "mientras", "además", "quien", "momento", "millones", "hoy", "lugar", "trabajo", "mejor", "nuevo", "decir", "algunos", "entonces", "todas", "debe", "cómo", "luego", "pasado", "medio", "nunca", "ver", "veces", "partido", "pueden", "cuenta", "tienen", "nueva", "cual", "fueron", "mujer", "cosas", "ciudad", "tener", "será", "muchos", "dentro", "nuestro", "dice", "ello", "cualquier", "noche", "aún", "parece", "situación", "fuera", "bajo", "nuestra", "ejemplo", "acuerdo", "hizo", "nadie", "países", "tarde", "ley", "proceso", "sentido", "lado", "cambio", "allí", "número", "sociedad", "gente", "relación", "cuerpo", "incluso", "último", "modo", "información", "ojos", "muerte", "público", "todavía", "mañana", "nosotros", "muchas", "verdad", "unidos", "junto", "cabeza", "aquel", "cuanto", "tierra", "equipo", "segundo", "cierto", "nivel", "largo", "llegar", "propio", "primero", "hemos", "algún", "tuvo", "respecto", "varios", "quienes", "mayoría", "claro", "iba", "buena", "quiere", "aquella", "palabras", "esas", "ahí", "últimos", "creo", "tengo", "dios", "condiciones", "fuerza", "único", "acción", "sabe", "calle", "tampoco", "ningún", "buen", "hubiera", "razón", "estoy", "hablar", "dio", "minutos", "quién", "demás", "diferentes", "dado", "ambos", "libertad", "medios", "ir", "población", "haya", "siendo", "mediante", "imagen", "deben", "datos", "miembros", "llegó", "bueno", "uso", "aquellos", "pronto", "soy", "hacía", "nuestros", "sigue", "siguiente", "nuevas", "and", "of", "in", "to", "have", "too", "it", "that", "for", "you", "with", "say", "this", "they", "at", "but", "we", "his", "from", "cant", "wont", "by", "she", "or", "as", "what", "go", "their", "can", "who", "get", "if", "would", "all", "my", "make", "about", "know", "will", "one", "time", "there", "think", "when", "which", "them", "some", "out", "into", "just", "see", "could", "now", "than", "like", "other", "how", "its", "our", "also", "only", "those", "very", "back"]
remove_comments(reddit, items_to_watch)
