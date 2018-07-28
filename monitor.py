import RPi.GPIO as GPIO 
import time


def monitor_callback(channel):
    measurement = GPIO.input(channel)
    print('{},{},{}'.format(channel, measurement, time.perf_counter()))
 

class VibrationMonitor:

    def __init__(self, *channels, bouncetime=300):
        self.channels = channels
        
        # setup GPIO
        GPIO.setmode(GPIO.BCM)
        for channel in self.channels:
            GPIO.setup(channel, GPIO.IN)
            GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=bouncetime)
            GPIO.add_event_callback(channel, monitor_callback)
        
    def monitor(self):
        while True:
            pass


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--channels',
                        nargs='+',
                        type=int,
                        required=True,
                        help='Raspberry Pi GPIO Data BCM channel number(s)')
    parser.add_argument('-b', '--bouncetime',
                        type=int,
                        default=300,
                        help='GPIO Event detect "bouncetime" [DEFAULT=300]')
    args = parser.parse_args()

    monitor = VibrationMonitor(*args.channels)
    monitor.monitor()
