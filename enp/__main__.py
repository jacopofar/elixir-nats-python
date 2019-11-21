from time import sleep
from datetime import datetime

from pynats import NATSClient

INTERVAL = 2.5

if __name__ == '__main__':
    print(f'Starting, will write a message every {INTERVAL} seconds')
    with NATSClient() as client:
        while True:
            payload = ('Hello I am the Python test payload for '
                       f'{datetime.now().isoformat()}')
            print(f'Sending: {payload}')
            client.publish(
                "test-subject",
                payload=payload.encode()
            )
            sleep(INTERVAL)
