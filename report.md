# Homework 1 Report

## Basics
External resources used on this assignment:
* 
https://realpython.com/regex-python/#grouping-constructs-and-backreferences
Classmates you talked to about this assignment:
* 
Ayman Khan, Prashan Babu
How many hours did you spend on this assignment?
* 
2-3 hours

## Report

### Regex Description
_Clearly describe how you make use of each of the required regular expression features in your make_message function._




#### Regular expression groups

I used groups to find specific words in a sentence such as greetings or cursing words.

#### Character classes

I used character classes to detect different version of a word. I used it for cursing words as they can be written by omitting a specific letter or character.

#### Quantifiers
I used the question mark for optional words like "I'm". 


### Analysis
_Describe at least one interaction with your bot that worked well, and at least one interaction with your bot that works poorly (or not as one might expect). You should include a transcript of your conversations in your writeup. This should include explanation not just of what happened, but why it happened, and why that was good or bad._

#### An interaction that went well
##### Transcript
You're chatting with artemisx
you: what up
bot: hey, how are you today?
you: just chilling
bot: Glad to hear that! How old are you?
you: I'm not 10
bot: Sorry! That's beyond my knowledge.
you: I'm 10 years old
bot: As Pierre Corneille said, value doesn't wait the number of years. You can still be anything you want.
you: examples
Examples:  ['How do I make my time productive', 'I am tired of failing', "What's the purpose of life", 'How can I be better?', ' I am heartbroken ', 'Tell me a joke', 'I give up']
you: How do I make my time productive?
bot: If you fulfill your obligations every day you don’t need to worry about the future.
you: I am tired of life
bot: You are not everything you could be, and you know it.
you: I'm also heartbroken
bot: Letting go means to come to the realization that some people are a part of your history but not a part of your destiny
you: Tell me a joke
bot: Why was Cinderella so bad at soccer?
 She kept running from the ball.
you: this bot is limited. Yes or no?
bot: Sorry! That's beyond my knowledge.


##### What happened and why? What was it good?
The interaction was decent. The bot is very limited in what it can do but it can detect patterns quite well and return the appropriate response.

#### An interaction that did went poorly
##### Transcript

you: yo
bot: hey, how are you today?
you: chilling
bot: Glad to hear that! How old are you?
you: definitely not 10
bot: Sorry! That's beyond my knowledge.

##### What happened and why? What was it bad?

The bot was supposed to reply with the quotes instead of "sorry! That's beyond my knowledge" for anytime a number is mentionned, regardless of the context. I fixed it.

### Another Chatbot
_Interact with one of your classmate's chatbots, and answer the following questions_

#### What was the chatbot called?
Chef-ramsey

#### Did they implement any features that you would have liked to implement in your chatbot if you had extra time?
 Not really.


#### Which features of regular expressions might they have used to achieve that functionality (regular expression groups, character classes, quantifiers, anchors, etc.)?
 I think they mostly used regular expression groups and maybe quantifiers

