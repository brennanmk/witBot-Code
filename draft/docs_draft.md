# WitBot Reference

## Blocks
Block | Description
- | -
**Basic Blocks** |
![Robot Drive Time Block](/static/img/blocks/robot_drive_time.png) | Move the robot forwards or backwards at the current speed for a certain number of seconds.
![Robot Drive Block](/static/img/blocks/robot_drive.png) | Move the robot forwards or backwards at the current speed.
![Robot Turn Time Block](/static/img/blocks/robot_turn_time.png) | Turn the robot right or left in place at the current speed for a certain number of seconds.
![Robot Turn Block](/static/img/blocks/robot_turn.png) | Turn the robot right or left in place at the current speed.
![Robot Stop Block](/static/img/blocks/robot_stop.png) | Stop the robot.
![Robot Motor Power Block](/static/img/blocks/robot_power.png) | Set the motor speed for the robot, on a scale of 0-100.
![Robot Line Sensor Block](/static/img/blocks/robot_line.png) | Get the current value of the robot's line sensor - this will be either true or false.
![Robot Distance Sensor Block](/static/img/blocks/robot_distance.png) | Get the distance from the robot's ultrasonic sensor to the nearest obstacle in the units specified (either inches or centimeters). The number will be negative if there is an error.
![Robot LED Block](/static/img/blocks/robot_led.png) | Turn the built-in LED on or off on the robot. This is useful for debugging when something isn't working the way it's supposed to.
**Advanced Blocks** |
![Robot Motor Power Block](/static/img/blocks/robot_motor.png) | Set the power of an individual motor. This lets you control the speed of the motors more precisely than the drive/turn blocks. The power value needs to be between -100 and 100.
![Robot GPIO Out Block](/static/img/blocks/robot_gpio_out.png) | Turns a GPIO pin on or off. These use BCM pin numbers, which you can read more about below.
![Robot GPIO In Block](/static/img/blocks/robot_gpio_in.png) | Get the value of a GPIO pin, true or false. This uses BCM pin numbers, which you can read more about below.

---

## Saving and Loading
The editor will automatically save your work as you write code, so you don't have to worry about loosing your work. You can tell whether or not your session has been saved by the label in the toolbar.

If you want to be able to save multiple scripts, under the 'Tools' option in the toolbar you may download your current script as a text file, and re-upload it, using the `Export` and `Import` buttons, respectively. Unless you really know what you're doing, it is advised to avoid modifying these text files on your own, as doing so can corrupt your scripts.

---

## Raspberry Pi Zero
### Pins
The WitBot is powered by a Raspberry Pi Zero W, which uses a section of pins called 'GPIO' (**G**eneral **P**urpose **I**nput and **O**utput). 

Each of these pins has 2 numbers used to refer to it:
- A **Board** number, indicated on the chart below by the number in the circle. Every pin has one of these. This numbering system is *not* used by the Blockly interface or pin definition file.
- A **BCM** number, indicated by the rectangle next to the circle on the chart below. For instance, a pin labeled `GPIO14` has BCM pin number 14. Unlike board pins, only pins which can be used for GPIO have these - so, power pins are left out. The WitBot uses these to refer to pins.

![Raspberry Pi Zero Pinout](/static/img/pinout.png)

*(Source: TODO find source of image)*

If you want to edit the pins your robot uses, bear in mind the distinction between BCM and Board pins. The pin definitions themselves are located in the `pins.ini` file, and can be edited with any plain old text editor.
The default pins are:
```
[motor_right]
pwm = 12
dira = 24
dirb = 23

[motor_left]
pwm = 13
dira = 22
dirb = 27

[ultrasonic]
trig = 26
echo = 19

[line]
sense = 6

[misc]
led = 2
```

## Troubleshooting
### Ultrasonic sensor
The ultrasonic sensor will usually be the easiest to find problems with. If the readout on the control panel says '[Timeout]cm', it means something is wrong

Typically, the issue is caused by one of the following problems, in order from least to most hard to repair:
- The pins on the ultrasonic sensor are wired incorrectly. Check the pins above and make sure your wiring is right
- The resistor circuit is wired incorrectly. Check the setup guide to make sure everything is in place
- The pins used on the pi are burnt out or broken - try changing the pins in the config file and the circuit
- The sensor itself is broken, and needs to be replaced
