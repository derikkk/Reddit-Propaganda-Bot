# Reddit-Propaganda-Bot
[**project instructions** ](https://github.com/mikeizbicki/cmc-csci040/tree/2021fall/hw_04)

### README.md file requirements
1. Clearly states which politician your bot is supporting or opposing (My bot supports Biden and is against Trump)
3. Provides a link to your favorite thread involving your bot, an image screenshot of the thread, and a short description of what you like about it. (Below each comment is a button labeled permalink that lets you link to a comment.)
4. Includes the output of running the bot_counter.py file on your bot to count how many comments you've created. The output of this command must be inside of a markdown code block (i.e. use the triple backticks notation).

### What my score should be: 32/30
COMPLETE- Each task in `bot.py` is worth 3 points.
(6 tasks * 3 points/task = 18 points)

COMPLETE- Github repo (2 points)

COMPLETE- Getting at least 100 valid comments posted. (2 points)

COMPLETE- Getting at least 500 valid comments posted. (2 points)

COMPLETE- Getting at least 1000 valid comments posted. (2 points)

COMPLETE- Replying to the most highly upvoted comment that you haven't replied to (2 points) --> Line 218

COMPLETE- Upvote any submissions that mention your favorite candidate (2 points) --> Lines 92 + 136

COMPLETE- Textblob sentiment analysis for upvoting/downvoting (2 points) --> Lines 92 + 136

### The Output of my `bot_counter.py` file running:
```
Mrss-MacBook-Pro:redditbot oneinchdong$ /usr/local/bin/python3 /Users/oneinchdong/Documents/GitHub/Python/redditbot/bot_counter.py --username=botgoyeet
len(comments)= 1000
len(top_level_comments)= 91
len(replies)= 909
len(valid_top_level_comments)= 91
len(not_self_replies)= 909
len(valid_replies)= 909
========================================
valid_comments= 1000
========================================
```
**Note: This was the output of the Bot Counter file before BotTown was banned.**

### [Botgoyeet Screenshot](https://www.reddit.com/r/BotTown2/comments/r4nt42/comment/hmhvfzj/?utm_source=share&utm_medium=web2x&context=3)
<img width="1001" alt="Tweets Screenshot" src="https://github.com/derikkk/Reddit-Propaganda-Bot/blob/main/Tweets%20Final.png">
I like this screenshot because it almost mimics what actual people would comment. Then you have a bot that is randomly commenting things about hues of green. All in all the other replies mention different political figures.

### Optional Tasks

In order to earn full credit on the assignment,
you will have to complete some of the optional tasks.
There are many of these optional tasks,
and so it is possible to earn significant extra credit on this assignment.

You earn 2 points of extra credit for each of the following tasks you complete.

1. Getting at least 100 valid comments posted.

1. Getting at least 500 valid comments posted.

1. Getting at least 1000 valid comments posted.

1. Make your bot create new submission posts instead of just new comments.
   You can easily automate this process by scanning the top posts in your favorite sub (e.g. /r/liberal or /r/conservative) and posting them to the class sub.
   I recommend creating a separate python file for creating submissions and creating comments.

1. Create an "army" of 5 bots that are all posting similar comments.
   This will require creating 5 different reddit accounts.
   You can use the same code for each bot (but different `praw.ini` files with the corresponding login credentials).
   The challenge is keeping all 5 of these bots running simultaneously.
   Each bot needs to post at least 500 valid comments to get this extra credit.

1. Instead of having your bot reply randomly to posts,
   make your bot reply to the most highly upvoted comment in a thread that it hasn't already replied to.
   Since reddit sorts comments by the number of upvotes, this will ensure that your bot's comments are more visible.
   You will still have to ensure that your bot never replies to itself if your bot happens to have the most upvoted comment.

1. Have your bot upvote any comment or submission that mentions your favorite candidate.
   I recommend creating a separate python file for performing the upvotes,
   and you must be able to upvote comments contained within any submission in the class subreddit.

   You may earn an additional two points if you use the [TextBlob](https://textblob.readthedocs.io/en/dev/) sentiment analysis library to determine the sentiment of all the posts that mention your favorite candidate.
   If the comment/submission has positive sentiment, then upvote it;
   if the comment/submission has a negative sentiment, then downvote it.
