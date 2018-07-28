import RPi.GPIO as GPIO 
import time


def monitor_callback(channel):
    measurement = GPIO.input(channel)
    print()
    if measurement:
        print('{} {}: {}'.format(channel, measurement, time.perf_counter()))
    print()
 

class VibrationMonitor:

    def __init__(self, *channels, wait_seconds=0.1):
        self.channels = channels
        self.wait_seconds = wait_seconds
        
        # setup GPIO
        GPIO.setmode(GPIO.BCM)
        for channel in self.channels:
            GPIO.setup(channel, GPIO.IN)
            GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
            GPIO.add_event_callback(channel, monitor_callback)
        
    def monitor(self):
        wait = self.wait_seconds
        while True:
            time.sleep(wait) 


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--channels',
                        nargs='+',
                        type=int,
                        required=True,
                        help='Raspberry Pi GPIO Data BCM channel number(s)')
    args = parser.parse_args()

    monitor = VibrationMonitor(*args.channels)
    monitor.monitor()
