import praw
import time
import random
from itertools import cycle

file = open("reach.txt","r")
log = file.read().splitlines()
file.close

reddit = praw.Reddit(
    client_id="eVc-MD7vpU7Ylg",
    client_secret="MRWl7bphxJJOarzmXVMFvRtcc_1bAA",
    user_agent="<console:THESCIENCE89:1.0",
    username=log[0],
    password=log[1]
)

file = open("visited.txt","r")
visited = file.read().splitlines()
file.close

def has_been_visited(authors_name):
    return authors_name in visited

def add_to_visited(authors_name):
    visited.append(authors_name)
    file = open("visited.txt","a")
    file.write(authors_name + "\n")
    file.close

def add_to_comments(comment_id):
    file = open("comments.txt","a")
    file.write(str(comment_id) + "\n")
    file.close
#"Catswhoyell"
sub_names = ["Pets", "CatsStandingUp","CatsInBusinessAttire", "CatsonGlass",
             "CatsInSinks", "CatLoaf", "Catswithjobs", "Catswhoyell"
             ]

to_comments = ["In ancient times cats were worshipped as gods; they have not forgotten this.",    
                "Cats can work out mathematically the exact place to sit that will cause most inconvenience.",
                "The problem with cats is that they get the same exact look whether they see a moth or an ax-murderer.",
                "I’m a cat whisperer. When I go to people’s houses, their cats always like me better than the owners.",
                "Dogs have owners, cats have staff."
               ]

pool = cycle(sub_names)
    
while True:
    print("total users visited: " + str(len(visited)))

    sub_found = False
    
    while not sub_found:
        try:
            sub_name = next(pool)
            subreddit = reddit.subreddit(sub_name)
            sub_found = True
        except:
            print("***REMOVE " + sub_name + " from the list***")
            continue
    
    print("=========================")
    print("Subreddit: " + sub_name)
    print("=========================")
    for submission in subreddit.hot(limit=5):
        #print(submission.title)
        max_comments = 2
        total_commented = 0
        for comment in submission.comments:
            if total_commented >= max_comments:
                 break
            #print(comment.body)
            if not hasattr(comment, "body"):
                continue   
            comment_lower = comment.body.lower()
            if " cat " not in comment_lower:
                continue
            if(has_been_visited(comment.author.name)):
                continue
            try:
                to_comment = to_comments[random.randint(0, len(to_comments) - 1)]
                comment_id = comment.reply(to_comment)
                add_to_comments(comment_id)
            except:
                print("exception occured, skipping")
                continue
            total_commented += 1
            print("comment total: " + str(total_commented))
            add_to_visited(comment.author.name)
            #print("sleeping...")
            time.sleep(610)
            #print("searching...")
    
    #print("moving to a new subreddit...")
