from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import random
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
      "-------------------------------INSTAGRAM BOT V.1.1------------------------------------\n"
      "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


# Function for getting a random hashtag from hashtags.txt
def get_random_hashtag():
    with open("hashtags.txt") as hashtag_file:
        hashtag_text = hashtag_file.readlines()
    return random.choice(hashtag_text).strip()


# Insert comments here
COMMENTS = ["comment_example1", "comment_example2", "comment_example3"]


# Pulls credentials from credentials.txt
with open("credentials.txt") as cred_file:
    CREDENTIALS = cred_file.readlines()
    USERNAME = CREDENTIALS[1].strip()
    PASSWORD = CREDENTIALS[2].strip()

# This number will most likely never be reached
# This variable is so the program will interact with the daily maximum amount of posts
POSTS = 5000

# Define the XPATH
# I know these are a bit long but this was the easiest way if any changes need to be made
LIKE2 = "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button"
LIKE = "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[3]/div/div/section[1]/span[1]/button"
FIRST_PIC = "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div[1]/div[2]"
FIRST_NEXT = "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div/button"
SECOND_NEXT = "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button"
COMMENT_BUTTON = "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/div/textarea"
POST_COMMENT = "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/div/div[2]/div"
LIMITED_COMMENTS = "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/div[3]/div"
LIMIT = "/html/body/div[2]/div/div/div[2]/div/div[2]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/button[2]"


# Random wait time, can be adjusted
WAIT = random.randint(2, 5)

# This while loop is here in order for the program to run again after limits or exceptions
# This means that the program will run indefinitely until manually stopped
while True:

    # Included this in the loop in order to get a new hashtag every time the program runs
    hashtag = get_random_hashtag()

    # Sets up browser
    s = Service(r'')  # Insert your path to chromedriver.exe here
    browser = webdriver.Chrome(service=s)
    browser.implicitly_wait(10)

#   Log in and navigate to hashtag page
    browser.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
    time.sleep(WAIT)
    browser.find_element(by=By.NAME, value='username').send_keys(USERNAME)
    time.sleep(WAIT)
    browser.find_element(by=By.NAME, value='password').send_keys(PASSWORD)
    time.sleep(WAIT)
    browser.find_element(by=By.TAG_NAME, value='form').click()
    # Had trouble clicking some pop-ups so redirects directly to hashtag page
    time.sleep(random.randint(12, 21))
    browser.get('https://www.instagram.com')
    time.sleep(random.randint(5, 18))
    browser.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
    print("------------------------------------------------------------------------------------\n"
          f"Hashtag: {hashtag}\n"
          "------------------------------------------------------------------------------------")
    time.sleep(WAIT)


#   Selects first picture and begins the process of liking and commenting
    try:
        browser.find_element(by=By.XPATH, value=FIRST_PIC).click()
        time.sleep(3)
        try:
            browser.find_element(by=By.XPATH, value=LIKE2).click()
        except NoSuchElementException:
            browser.find_element(by=By.XPATH, value=LIKE).click()
        time.sleep(1)
        # Check for limited comments
        try:
            browser.find_element(by=By.XPATH, value=LIMITED_COMMENTS)
            time.sleep(WAIT)
            browser.find_element(by=By.XPATH, value=FIRST_NEXT).click()
            print("Post 1: Comments Limited")
            time.sleep(WAIT)
        except NoSuchElementException:
            # Comments on post if comments are not limited
            try:
                browser.find_element(by=By.XPATH, value=COMMENT_BUTTON).clear()
                time.sleep(1)
                browser.find_element(by=By.XPATH, value=COMMENT_BUTTON).click()
                time.sleep(WAIT)
                browser.find_element(by=By.XPATH, value=COMMENT_BUTTON).send_keys(random.choice(COMMENTS))
                time.sleep(WAIT)
                browser.find_element(by=By.XPATH, value=POST_COMMENT).click()
                time.sleep(WAIT)
                # After comment posted checks if daily comment limit was reached
                try:
                    browser.find_element(by=By.XPATH, value=LIMIT).click()
                    time.sleep(WAIT)
                    browser.find_element(by=By.XPATH, value=FIRST_NEXT).click()
                    print("***DAILY COMMENT LIMIT REACHED***")
                    # If daily comment limit was reached goes into like only mode
                    for i in range(2, POSTS + 1):
                        try:
                            browser.find_element(by=By.XPATH, value=LIKE2).click()
                        except NoSuchElementException:
                            browser.find_element(by=By.XPATH, value=LIKE).click()
                        time.sleep(WAIT)
                        browser.find_element(by=By.XPATH, value=SECOND_NEXT).click()
                        time.sleep(WAIT)
                        print(f"Post {i} Complete: *Like only*")
                # If comment limit is not reached goes to next post
                except NoSuchElementException:
                    browser.find_element(by=By.XPATH, value=FIRST_NEXT).click()
                    time.sleep(WAIT)
                    print("Post 1: Complete")
            # If comments are disabled program doesn't comment and moves to next post
            except NoSuchElementException:
                browser.find_element(by=By.XPATH, value=FIRST_NEXT).click()
                time.sleep(1)
                print("Post 1: Comments Disabled")

        # This loop begins on second post and continues until either limit or exception
        for i in range(2, POSTS+1):
            try:
                browser.find_element(by=By.XPATH, value=LIKE2).click()  # 1st like
            except NoSuchElementException:
                browser.find_element(by=By.XPATH, value=LIKE).click()
            time.sleep(WAIT)
            # Check for limited comments
            try:
                browser.find_element(by=By.XPATH, value=LIMITED_COMMENTS)
                time.sleep(WAIT)
                browser.find_element(by=By.XPATH, value=SECOND_NEXT).click()
                time.sleep(WAIT)
                print(f"Post {i}: Comments Limited")
            # Comments on post if comments are not limited
            except NoSuchElementException:
                try:
                    browser.find_element(by=By.XPATH, value=COMMENT_BUTTON).click()
                    time.sleep(WAIT)
                    browser.find_element(by=By.XPATH, value=COMMENT_BUTTON).send_keys(random.choice(COMMENTS))
                    time.sleep(WAIT)
                    browser.find_element(by=By.XPATH, value=POST_COMMENT).click()
                    time.sleep(WAIT)
                    # After comment posted checks if daily comment limit was reached
                    try:
                        browser.find_element(by=By.XPATH, value=LIMIT).click()
                        time.sleep(WAIT)
                        browser.find_element(by=By.XPATH, value=SECOND_NEXT).click()
                        print(f"***DAILY COMMENT LIMIT REACHED***")
                        # If daily comment limit was reached goes into like only mode
                        for j in range(2, POSTS + 1):
                            browser.find_element(by=By.XPATH, value=LIKE).click()  # {i} like
                            time.sleep(WAIT)
                            browser.find_element(by=By.XPATH, value=SECOND_NEXT).click()
                            time.sleep(WAIT)
                            print(f"Post {j} Complete: *Like only*")
                    # If comment limit is not reached goes to next post
                    except NoSuchElementException:
                        browser.find_element(by=By.XPATH, value=SECOND_NEXT).click()
                        time.sleep(WAIT)
                        print(f"Post {i}: Complete")
                # If comments are disabled program doesn't comment and moves to next post
                except NoSuchElementException:
                    browser.find_element(by=By.XPATH, value=SECOND_NEXT).click()
                    time.sleep(WAIT)
                    print(f"Post {i}: Comments Disabled")

    # Eventually both like limit and comment limit will be reached
    # When this happens the browser closes and the program sleeps for the random sleep time
    except Exception as e:
        # Prints the exception so you know what happened
        print(e)
        browser.close()
        # Chooses random sleep time between 24 and 26 hours, can be changed
        SLEEP = random.randint(1140, 1560)
        # Sleeps until timer is up, then runs again
        print("***SLEEPING***")
        for minute in range(1, SLEEP):
            print(f"SLEEP: {minute} of {SLEEP} minutes.")
            time.sleep(60)
