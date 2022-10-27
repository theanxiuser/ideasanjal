# insert posts from csv file to db

import csv

# import post from models
from home.models import Post, IsUser

# python manage.py runscript load_posts

def run():
    fhand = open("home/posts.csv")
    reader = csv.reader(fhand)
    next(reader)

#     delete old contents
    Post.objects.all().delete()

#     title slug content

    for row in reader:
        print(row)
        a = IsUser.objects.get(pk=1)
        p = Post(title=row[0], slug=row[1], content=row[2], author=a, image=row[3])
        p.save()
