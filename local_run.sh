#!/bin/bash
cat use_fake_gpio.py play_sound.py > mock.py 
python mock.py
rm mock.py
