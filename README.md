# Simple-Fault-Detector

## What is this about?

This is a simple project to turn an ESP8266 like device into a fault detector. I originally created this to detect errors with my heating control which happens every now and then. A light bulb is connected to the control unit which then blinks. But if I'm not home I don't get to see it.
Now once the light blinks, the ESP powers up and spams UDP packets to my local server. The server then notifies me via e-mail.

As the light just blinks, the ESP has only a few seconds to connect to the network and send the packets, so it needs to be very fast. Sending the e-mails directly from the ESP just is not fast enough.

Here is a simple sketch of the whole system:
![sketch of the system](...)

This is a very simple project and easily extendable, so feel free to use my code however you want. You just need a file called env.py to store credentials and constants. A sample is in the Server directory.

I don't plan on extending this any further, maybe a few quick fixes, but nothing more.
