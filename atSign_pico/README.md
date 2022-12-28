<img width=250px src="https://atsign.dev/assets/img/atPlatform_logo_gray.svg?sanitize=true">

# at_pico_w

IoT Project --- banking

# Table of Contents

- [Table of Contents](#table-of-contents)
- [Instructions](#instructions)
  - [0. Introduction](#0-introduction)
  - [1. Setting up the Pico w](#1-Setting-up-the-pico-w)
  - [2. Wiring on the Pico w](#2-Wiring-on-the-Pico-w)
  - [3. Taking input from the keypad](#3-Taking-input-from-the-keypad)

# Instructions

## 0. Introduction

This is the hardware part of the project Banking App. You can follow the instruction to get Pico w configured and connected to atSign server, then you can use the keypad to enter your banking information.

## 1. Setting up the Pico w

1. Go to https://github.com/atsign-foundation/at_pico_w/tree/umass2022#prerequisites and follow the step-by-step instructions to configure Pico w properly.

2. A video version is also available here https://www.youtube.com/watch?v=8xJnbsuF4C8&ab_channel=Atsign.

## 2. Wiring on the Pico w

Now let's see how you can wire the keypad with Pico w. Here is an example:

1. A pico header will be used to make sure firm connections.

2. Make sure pins are matched to the connection.

3. Here rows are associated with pins 9,8,7,6 and columns are with pins 5,4,3,2.

4. We can only scan one key pressed at a time.

<image src="https://i.imgur.com/u1PEY98.png" />

```py
# bankingApp.py
# Define PINs according to cabling, change the pins to match with your connections
    keypad_rows = [9,8,7,6]
    keypad_columns = [5,4,3,2]
```

## 3. Taking input from the keypad

Now we can run `bankingApp.py` to start sending data.

As a reminder, make sure the wifi information in `setting.json` is also correct.

```json
{
  "ssid": "****",
  "password": "****",
  "atSign": "@****"
}
```

You will need to format your input as follows:

```
pin(4) + acc(9)

_ _ _ _ + a _ _ _ a _ _ _ a

```

The program will detect when the input is ended and send the associated data to atSign server!
