import praw
import time
import random
from itertools import cycle

file = open("reach.txt", "r")
log = file.read().splitlines()
file.close

reddit = praw.Reddit(
    client_id="eVc-MD7vpU7Ylg",
    client_secret="MRWl7bphxJJOarzmXVMFvRtcc_1bAA",
    user_agent="<console:THESCIENCE89:1.0",
    username=log[0],
    password=log[1]
)

visited = list()

def add_parents_author_to_visited(comment_obj):
    global visited
    try:
        visited.append(comment_obj.parent().author.name)
        return True
    except:
        return False

def check_comment_karma():
    global visited
    print("####################################")
    print("Comment Removal Starting")
    visited = list()
    for comment_obj in reddit.redditor(log[0]).comments.new(limit=None):
        try:
            if(comment_obj.score < 1):
                try:
                    print("removing a comment with score: " +
                          str(comment_obj.score))
                    comment_obj.delete()
                    continue
                except:
                    pass
            else:
                if not (add_parents_author_to_visited(comment_obj)):
                    try:
                        print("could not add an author")
                        comment_obj.delete()
                        continue
                    except:
                        pass
        except:
            try:
                print("removing a comment, can't access score")
                comment_obj.delete()
                continue
            except:
                pass
    print("####################################")
    print("Comment Removal Done")
    print("Comments Made: " + str(len(visited)))
    print("Users Visited: " + str(len(visited)))
    print("####################################")


# "Catswhoyell"
sub_names = ["CatsInBusinessAttire", "CatsonGlass",
             "CatsInSinks", "CatLoaf", "Catswithjobs", "Catswhoyell"
             ]

to_comments = ["In ancient times cats were worshipped as gods; they have not forgotten this.",
               "Cats can work out mathematically the exact place to sit that will cause most inconvenience.",
               "The problem with cats is that they get the same exact look whether they see a moth or an ax-murderer.",
               "Dogs have owners, cats have staff."
               ]

pool = cycle(sub_names)

subs_visited = 0

while True:
    if subs_visited % 5 == 0:
        check_comment_karma()
    sub_found = False

    while not sub_found:
        try:
            sub_name = next(pool)
            subreddit = reddit.subreddit(sub_name)
            sub_found = True
        except:
            print("***REMOVE " + sub_name + " from the list***")
            continue

    print("Subreddit: " + sub_name)
    for submission in subreddit.hot(limit=10):
        max_comments = 2
        total_commented = 0
        for comment in submission.comments:
            if total_commented >= max_comments:
                break
            if not hasattr(comment, "body"):
                continue
            comment_lower = comment.body.lower()
            if " cat " not in comment_lower:
                continue
            if(comment.author.name in visited):
                continue
            try:
                to_comment = to_comments[random.randint(0, len(to_comments) - 1)]
                comment.reply(to_comment)
                total_commented += 1
            except:
                continue
            print("waiting...")
            time.sleep(610)
    subs_visited += 1
    #####
    #####
    #####
