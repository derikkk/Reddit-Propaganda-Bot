#IndexError because no comments in not_my_comments
import praw
import random
import datetime
import time
import textblob

# FIXME:
# copy your generate_comment function from the madlibs assignment here

madlibs = [
    "[BIDEN] is a [NICE] guy.  He [MIGHT] be [OLD]. But [EVERYONE] should [LOVE] him.",
    "[BIDEN] [LOVES] to speak [SLOWLY]. But he [CAN] convince people. Thus, he is a [NICE] candidate for president.",
    "[TRUMP] [CAN] talk about himself for [HOURS]. [EVERYONE] [SHOULD] realize that not all of it makes sense.",
    "[TRUMP] [LOVES] to talk to [NORTH KOREA]. He says they [MIGHT] be able to provide [AID] in mobile technology.",
    "There is no [CONNECTION] between [TRUMP] and [RUSSIA] at all. It's not like they [HELP] him in any way. They are not [SUSPICIOUS] at all.",
    "[NORTH KOREA] says they have [LOTS] of food for their [PEOPLE]. They do not need [AID]. But we [SHOULD] doubt what they tell us.",
    "Here are some [NICE] [SYNONYMS] for yeet: [YEET], [YEET]. [TRUMP] should use it more often- it might [HELP] him communicate better.",
    ]

replacements = {
    'BIDEN' : ['Biden', 'Joe', 'Joe Biden'],
    'SYNONYMS' : ['synonyms', 'alternatives', 'equivalents'],
    'YEET' : ['yeet', 'yote', 'yeetus','reeeeee'],
    'NICE' : ['great', 'magnificent', 'fantastic', 'wonderful'],
    'MIGHT' : ['may', 'might'],
    'CAN' : ['can', 'is able to', 'is capable of', 'is competent enough to'],
    'LOTS'  : ['lots', 'a whole lot', 'ridiculous amounts'],
    'STUFF' : ['stuff', 'things', 'fun things'],
    'OLD' : ['old', 'ancient', 'gray-haired'],
    'LOVE' : ['love', 'like', 'prefer'],
    'LOVES' : ['loves', 'prefers to', 'likes'],
    'EVERYONE' : ['Everyone', 'Everyone, yes that means you,', 'All students', 'People everywhere', 'You'],
    'SHOULD' : ['should', 'must', 'have to'],
    'BECOME' : ['become', 'turn into', 'try to be'],
    'SLOWLY' : ['slow', 'steadily', 'at a snails pace'],
    'HOURS' : ['days', 'years', 'hours'],
    'TRUMP' : ['Donald', 'Trump', 'Donald Trump'],
    'NORTH KOREA' : ['Kimmy', 'Kim Jong Un', 'Jong Un'],
    'HELP' : ['aid', 'assist', 'are of service to'],
    'CONNECTION' : ['link', 'relationship', 'connection', 'correspondence'],
    'RUSSIA' : ['the russians', 'the USSR', 'the russian federation'],
    'SUSPICIOUS' : ['sus', 'suspect', 'suspicious'],
    'PEOPLE' : ['citizens', 'residents', 'men, women, and children'],
    'AID' : ['help', 'assistance', 'aid'],
    }


#make code very generic so it works with all messages 
#[+k+] only things surrounded by [] can be replaced 
# contents of generate function 
def generate_comment():
    '''
    This function generates random comments according to the patterns specified in the `madlibs` variable.
    To implement this function, you should:
    1. Randomly select a string from the madlibs list.
    2. For each word contained in square brackets `[]`:
        Replace that word with a randomly selected word from the corresponding entry in the `replacements` dictionary.
    3. Return the resulting string.
    For example, if we randomly seleected the madlib "I [LOVE] [PYTHON]",
    then the function might return "I like Python" or "I adore Programming".
    Notice that the word "Programming" is incorrectly capitalized in the second sentence.
    You do not have to worry about making the output grammatically correct inside this function.
    '''

    s = random.choice(madlibs)
    for k in replacements.keys():
        s = s.replace('['+k+']', random.choice(replacements[k]))
    return s

# connect to reddit 
reddit = praw.Reddit('bot', user_agent = 'cs40')

# select a "home" submission in the /r/BotTown subreddit to post to,
# and put the url below
submission_url = 'https://www.reddit.com/r/BotTown2/comments/r0yi9l/main_discussion_thread/'
submission = reddit.submission(url=submission_url)

# each iteration of this loop will post a single comment;
# since this loop runs forever, your bot will continue posting comments forever;
# (this is what makes it a deamon);
# recall that you can press CTRL-C in the terminal to stop your bot
#
# HINT:
# while you are writing and debugging your code, 
# you probably don't want it to run in an infinite loop;
# you can change this while loop to an if statement to make the code run only once
while True: #change to while True for final submission

    # Extra credit: using textblob to conduct sentiment analysis + upvote 
    
    submission_text = textblob(submission.title)
    if ("biden" in submission_text.lower() and submission_text.sentiment.polarity>0.7) or ("trump" in submission_text.lower() and submission_text.sentiment.polarity<-0.5):
        submission.upvote()
    elif ("biden" in submission_text.lower() and submission_text.sentiment.polarity<-0.7) or ("trump" in submission_text.lower() and submission_text.sentiment.polarity>0.5):
        submission.downvote()
   

    # printing the current time will help make the output messages more informative
    # since things on reddit vary with time
    print()
    print('new iteration at:',datetime.datetime.now())
    # print('submission.title=',submission.title)
    print('submission.url=',submission.url)

    # FIXME (task 0): get a list of all of the comments in the submission
    # HINT: this requires using the .list() and the .replace_more() functions
    
    submission.comments.replace_more(limit=None)
    all_comments = submission.comments.list()

    # HINT: 
    # we need to make sure that our code is working correctly,
    # and you should not move on from one task to the next until you are 100% sure that 
    # the previous task is working;
    # in general, the way to check if a task is working is to print out information 
    # about the results of that task, 
    # and manually inspect that information to ensure it is correct; 
    # in this specific case, you should check the length of the all_comments variable,
    # and manually ensure that the printed length is the same as the length displayed on reddit;
    # if it's not, then there are some comments that you are not correctly identifying,
    # and you need to figure out which comments those are and how to include them.
    print('len(all_comments)=',len(all_comments))

    #(task 1): filter all_comments to remove comments that were generated by your bot
    # HINT: 
    # use a for loop to loop over each comment in all_comments,
    # and an if statement to check whether the comment is authored by you or not
    not_my_comments = []
    for comment in all_comments:
        # print('comment.author=', comment.author)
        # print('type(comment.author)=', type(comment.author))
        if str(comment.author) != 'botgoyeet':
            not_my_comments.append(comment)
        
        text = textblob(str(comment.body))
        if ("biden" in text.lower() and text.sentiment.polarity>0.5) or ("trump" in text.lower() and text.sentiment.polarity<-0.5):
            comment.upvote()
        elif ("biden" in text.lower() and text.sentiment.polarity<-0.5) or ("trump" in text.lower() and text.sentiment.polarity>0.5):
            comment.downvote()
        
    

    # HINT:
    # checking if this code is working is a bit more complicated than in the previous tasks;
    # reddit does not directly provide the number of comments in a submission
    # that were not gerenated by your bot,
    # but you can still check this number manually by subtracting the number
    # of comments you know you've posted from the number above;
    # you can use comments that you post manually while logged into your bot to know 
    # how many comments there should be. 
    print('len(not_my_comments)=',len(not_my_comments))

    # if the length of your all_comments and not_my_comments lists are the same,
    # then that means you have not posted any comments in the current submission;
    # (your bot may have posted comments in other submissions);
    # your bot will behave differently depending on whether it's posted a comment or not
    has_not_commented = len(not_my_comments) == len(all_comments)
    print('has_not_commented=', has_not_commented)

    if has_not_commented:
        #(task 2)
        # if you have not made any comment in the thread, then post a top level comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # a top level comment is created when you reply to a post instead of a message
        
        text = generate_comment()
        submission.reply(text)
        

    else:
        #(task 3): filter the not_my_comments list to also remove comments that 
        # you've already replied to
        # HINT:
        # there are many ways to accomplish this, but my solution uses two nested for loops
        # the outer for loop loops over not_my_comments,
        # and the inner for loop loops over all the replies of the current comment from the outer loop,
        # and then an if statement checks whether the comment is authored by you or not

        comments_without_replies = []
        for comment in not_my_comments:
            valid_comment = True
            for reply in comment.replies: 
                try:
                    if reply.author == 'botgotyeet':
                        valid_comment = False
                        break
                except praw.exceptions.APIException:
                    pass
        
            if valid_comment:
                comments_without_replies.append(comment)

        print('comments_without_replies=', len(comments_without_replies))
        # print('comments_without_replies=', comments_without_replies)

        #comments_without_replies = not_my_comments #Index Error because no comments in not_my_comments


        # HINT:
        # this is the most difficult of the tasks,
        # and so you will have to be careful to check that this code is in fact working correctly

        #(task 4): randomly select a comment from the comments_without_replies list,
        # and reply to that comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # these will not be top-level comments;
        # so they will not be replies to a post but replies to a message
        if len(comments_without_replies) > 0:
            comment = random.choice(comments_without_replies)
            try:
                comment = sorted(comments_without_replies, key=score_comment, reverse=True)[0]
                comment.reply(generate_comment())
                time.sleep(1)
                print('existing_comment_body=', comment.body)
            except praw.exceptions.APIException:
                print('not replying to a comment that has been deleted')
    
    #(task 5): select a new submission for the next iteration;
    # your newly selected submission should be randomly selected from the 5 hottest submissions
    
    submission = random.choice(list(reddit.subreddit("BotTown2").hot(limit=5)))
    
    # We sleep just for 1 second at the end of the while loop.
    # This doesn't avoid rate limiting
    # (since we're not sleeping for a long period of time),
    # but it does make the program's output more readable.
   
