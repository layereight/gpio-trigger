# gpio-trigger

* trigger arbitrary action when a gpio button is pressed on a Raspberry Pi
* currently only supports curling a URL

## Usage

```
gpio-trigger.py <gpio_pin_number> <url_to_call>
```

* example:
```
gpio-trigger.py 13 http://localhost:3000/api/v1/commands/?cmd=volume&volume=plus
```
