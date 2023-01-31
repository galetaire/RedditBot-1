import praw
import pdb
import re
import os
import random

# Reddit instance
reddit = praw.Reddit(
    user_agent="",
    client_id="",
    client_secret="",
    username="",
    password=""
)

#Llista per no respondre a missatges ja resposts
if not os.path.isfile("catsongbot_replied_to.txt"):
    comments_replied_to = []
else:
    with open("catsongbot_replied_to.txt", "r") as f:
       comments_replied_to = f.read()
       comments_replied_to = comments_replied_to.split("\n")
       comments_replied_to = list(filter(None, comments_replied_to))

# Cançons a recomanar
llista_musical = \
[
" [Oques Grasses - La gent que estimo](https://www.youtube.com/watch?v=yGO3UPPuVKs)",
" [Zoo - Estiu](https://www.youtube.com/watch?v=MI19iKuNeHg)",
" [Maria Arnal i Marcel Bagés - Ball del vetlatori](https://www.youtube.com/watch?v=Xd9MRjCyC84)",
]

# Resposta del bot
subreddit = reddit.subreddit("catalunya")
for comment in subreddit.stream.comments():
    if comment.id not in comments_replied_to:
        if re.search("cançó!", comment.body, re.IGNORECASE):
            llista_reply = "Cançó recomanada: " + random.choice(llista_musical)
            comment.reply(llista_reply)
            comments_replied_to.append(comment.id)
            with open("catsongbot_replied_to.txt", "w") as f:
                for comment_id in comments_replied_to:
                    f.write(comment_id + "\n")
