# gpio-trigger

* trigger arbitrary action when a gpio button is pressed on a Raspberry Pi
* supported actions are
  * curling a URL
  * executing a command line

## Usage

```
gpio-trigger.py <gpio_pin_number> <action_type> <action>
```

* example:
```
gpio-trigger.py 13 curl 'http://localhost:3000/api/v1/commands/?cmd=volume&volume=plus'
gpio-trigger.py 5 command '/usr/bin/amixer -c sndrpihifiberry sset SoftMaster 2%-'
```
