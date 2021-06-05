import praw
import time

reddit = praw.Reddit(
    client_id="eVc-MD7vpU7Ylg",
    client_secret="MRWl7bphxJJOarzmXVMFvRtcc_1bAA",
    user_agent="<console:THESCIENCE89:1.0",
    username="TheScience89",
    password="ajASFK3i253kasd$"
)

#h0lilj4

while True:
    file = open("comments.txt","r")
    comment_ids = file.read().splitlines()
    print(comment_ids)
    file.close

    comment_objs = list()

    print("getting comment objects")
    for comment_id in comment_ids:
        try:
            comment_objs.append(reddit.comment(id=comment_id))
        except:
            print("could not get comment")
            comment_ids.remove(comment_id)

    print("comment objs1: ")
    print(comment_objs)

    print("checking comment scores")
    for comment_obj in comment_objs:
        try:
            print(comment.score)
            if(comment.score < 1):
                print("removing: " + comment_obj.comment_id)
                comment_objs.remove(comment_obj)
                comment.delete()
        except:
            print("error with score")
            comment_objs.remove(comment_obj)

    file = open("comments.txt","w")

    print("comment objs2: ")
    print(comment_objs)
    
    for comment_obj in comment_objs:
        print("comment: " + comment_obj + ", score: " +
              str(comment_obj.score))
        try:
            file.write(str(comment_id) + "\n")
        except:
            print("error getting comment id or writing to file")
    file.close

    print("sleeping for 1 hour")
    time.sleep(3600)
    

