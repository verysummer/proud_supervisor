# proud_supervisor

## make your supervisor proud by nothing more than a push of a button -- you deserve it!

### ways to start the proud supervisor:
1. unplug and plug back in, or
2. python play_sound.py, or
3. sudo reboot
(2 and 3 with ssh)

### change volume:

`alsamixer`

### play mp3:

`omxplayer <file>.mp3` 

### stop running process:

`ps aux | grep python` (searches for 'python' in all processes)

`sudo kill -9 <pid process id>` (the id of the process you want to kill)

### output log saved in: logs/play_sound_log

start program upon start with crontab (set to regularly do stuff)
`sudo crontab -e`
add in crontab:
`@reboot sh /home/pi/src/proud_supervisor/launcher.sh > /home/pi/logs/cronlog 2>&1`

### Local development mode
In order to run the code locally, GPIO has to be mocked, since it's not compatible with kernels
outside of the raspberry pi.

To get setup do:
```bash
pip install fake_rpi
```

Then, to execute the script, run it as follows:

```bash
fake_gpio.sh play_sound.py
```

This wraps the script with the appropriate mock code and executes it.
Does not alter the script used as an input, but instead creates a temporary copy.

