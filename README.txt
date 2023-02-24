This is my first version of an Instagram interaction bot.

Copyright (c) 2023 Joseph Lopez
Do not use for profit or unethical purposes

Steps:
    0. Install requirements (requirements.txt)
    1. Insert your login credential in credentials.txt
    2. Insert list of hashtags in hashtags.txt
    3. Insert your comments in the COMMENTS list of insta_bot.py (line 13)
    4. Insert your path in insta_bot.py (Where the comment states insert path here, line 55)

How it works:
    The program logins in to instagram using the credentials in credentials.txt and navigates to a random hashtag
    in hashtags.txt. Once the hashtags pages is reached the program clicks the first post and starts the process
    of both liking and commenting on posts. When commenting on a post the program chooses a random comment from the
    COMMENTS list. Before commenting the program will check if comments are limited. If comments are limited
    the program moves on to the next post. After commenting the program will check if the daily comment limit was
    reached. If the daily comment limit was reached the program will only like posts until the daily like limit is
    reached. There is no exception if the daily like limit is reached, because if the daily like limit is reached
    the daily comment limit will most likely be reached as well. If both limits are reached the program sleeps for
    12 to 17 hours and runs again on a new hashtag provided in hashtags.txt. The only way to stop this program is to
    manually stop it. If you don't want it to run 24/7 just get rid of the sleep timer and the while loop.
