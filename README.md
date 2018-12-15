# Echo-Generation
## Introduction
Echo is a phenomenon that occurs due to the reflection of the sound wave in a wall, we hear the
summation of the original signal and delayed and decayed versions of this signal.

## Problem statement
It is required to design an echo generation and cancellation system.

## Problem approach

> **Generation:** A simple generation model that models the echo as the original signal, and one delayed and attenuated version
of it. The values of delay and attenuation can be variables in order to model echos in different
environments.

> **Cancellation:** Simply by using the inverse of that model!

## How to use

You can any program to record a wav file, or use the sample file included *salam.wav*. 

## How the code works

> **The code achieves the following tasks:**

* Reads an audio file.
* Adds an echo to it and then creates an audio file called Echo.
* Removes the echo and then creates an audio file called Fixed (Definitely identical to the original file).
* Plots the original signal, the echo signal and the fixed version. 

## How to use the code

* Firstly, start by installing dependancies using pip or conda

> pip install matplotlib scipy numpy 

**Or:**

> cond install matplotlib scipy numpy

* Then just run the code if you are planning to try out the sample *salam.wave*, an alternative to this is by recording your own audio file 
and then just change this line of the code:

**[Rate, Signal] = wav.read('file.wav')** 

with:

**[Rate, Signal] = wav.read('your file name.wav')**
