# mytwitterbot.py
# IAE 101, Fall 2020
# Project 04 - Building a Twitterbot
# Name: Sidharth Shamshabad
# netid: sshamshabad
# Student ID: 112888611

import sys
import time
import simple_twit
import random

def main():
    # This call to simple_twit.create_api will create the api object that
    # Tweepy needs in order to make authenticated requests to Twitter's API.
    # Do not remove or change this function call.
    # Pass the variable "api" holding this Tweepy API object as the first
    # argument to simple_twit functions.
    api = simple_twit.create_api()
    simple_twit.version()
    
    # Project 04 Exercises

    # # Exercise 1 - Get and print 10 tweets from your home timeline
    # print('Exercise 1:')
    # home_tweets = simple_twit.get_home_timeline(api, 10)
    # for tweet in home_tweets:
    #     print('Name: ' + str(tweet.author.name))
    #     print('ID: ' + str(tweet.id))
    #     print('Tweet: ' + str(tweet.full_text))
    #     print()
    #
    # # Exercise 2 - Get and print 10 tweets from another user's timeline
    # print('Exercise 2:')
    # elon_tweets = simple_twit.get_user_timeline(api, 'elonmusk', 10)
    # for tweet in elon_tweets:
    #     print('Name: ' + str(tweet.author.name))
    #     print('ID: ' + str(tweet.id))
    #     print('Tweet: ' + str(tweet.full_text))
    #     print()
    # # print(simple_twit.get_user(api, 'elonmusk'))
    # # Exercise 3 - Post 1 tweet to your timeline.
    # print('Exercise 3:')
    # post_tweet = 'This is a test tweet for exercise 3'
    # simple_twit.send_tweet(api, post_tweet)
    # print(post_tweet)
    # print()
    #
    # # Exercise 4 - Post 1 media tweet to your timeline.
    # print('Exercise 4:')
    # post_media_tweet_text = 'This is a test tweet text for exercise 4'
    # simple_twit.send_media_tweet(api, post_media_tweet_text, 'test31.png')
    # print(post_media_tweet_text)

    # YOUR BOT CODE BEGINS HERE
    marvel_lines = ['We\'re Fighting An Army Of Robots And I Have A Bow And Arrow. None Of This Makes Sense.',
                    'Whatever It Takes...', 'If You\'re Nothing Without The Suit, Then You Shouldn\'t Have It.',
                    'I Have Nothing To Prove To You.', 'She\'s Not Alone.', 'I Can Do This All Day.',
                    'That\'s My Secret Cap; I\'m Always Angry.', 'Wakanda Forever!', 'I Am Iron Man.', 'We Have A Hulk.'
                    'There Was An Idea...', 'We Are Groot!', 'If We Can\'t Protect The Earth, You Can Be Damn Well Sure We\'ll Avenge It!',
                    'Dormammu, I\'ve Come To Bargain.', 'Part of the journey is the end.',
                    'No amount of money ever bought a second of time.', 'SteveRogersSad.png', 'captain-america-civil-war.png',
                    'captain-marvel.png', 'thor-horse.png', 'thor-adopted.png', 'tony-spaceship.png', 'spiderman-fury.png', 'captain-marvel-w-friend.png',
                    ]

    while True:
        pick = random.choice(marvel_lines)
        print(pick)
        if pick.split('.')[-1] == 'png':
            simple_twit.send_media_tweet(api, 'An iconic marvel image', pick)
        else:
            simple_twit.send_tweet(api, pick)
        time.sleep(900)

# end def main()

if __name__ == "__main__":
       main()
