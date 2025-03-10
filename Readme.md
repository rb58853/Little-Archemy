# Numeric Alchemy Bot
## Date
December 1, 2022

## Summary
This document aims to discuss the Applied Mathematics project where a chemistry bot was created for Telegram, initially intended for the Numerical Mathematics course. This consists of recreating the game Little Alchemy but its elements will be concepts and contents of the subject matter.

## Keywords
bot, Telegram, alchemy, Little Alchemy, numerical

## 1. Introduction
Numerical Mathematics is the theory and practice of efficient calculation, it is the estimation of the error of the approximate solution of many mathematical application problems. Telegram is a messaging application focused on speed and security, among its multiple tools it allows the creation and use of so-called bots. These are computer programs that perform automated specific tasks and, generally, repetitive ones in a network. The objective of the project is to combine both numerical mathematics and Telegram bots through the concept of the Little Alchemy game.

## 2. Development

### 2.1 User Manual (Student)

To view the official bot help, simply write the `/help` command and a message will be displayed explaining briefly each of the available commands. Among the commands that make up the game we find:

* `/about`: Briefly describes the bot's purpose and operation.
* `/parents`: Shows a message with basic elements (elements that all users have unlocked from the beginning), plus those that the user has discovered and were approved. Then the elements shown in this message are available to create new ones.
* `/my items`: Displays a message with exactly the discovered elements along with the credits awarded for the discovery and the parent elements of each one.
* `/pending items`: Shows the list of elements pending approval by administrators. It will be a message with a format similar to `/my items`, without the credits field but with the related element description.
* `/leaderboard`: Provides access to the bot's user ranking table based on credits.
* `/new item`: Is the command that allows creating a new element through a message with the following format:
```markdown
/new item
Name: name of the element to create
Parents: separated by commas, the exact names of the parent elements must be written, which must be among the elements in the /parents list
Description: justification of the element to create, important part for approval
```

### 2.2 Administrator Manual
The administrator, besides being able to be a normal user and access these functionalities, will also be responsible for approving pending elements from users who do not possess this power. The commands that enable these options are:

* `/list`: Shows the list of elements, along with their descriptions and parents, proposed by students. Then it will be possible to accept or reject them.
* `/set admin`: Allows an administrator to grant the same privileges to another user, passing the @username as an argument.

