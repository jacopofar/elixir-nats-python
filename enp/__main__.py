from time import sleep
from datetime import datetime
from threading import Thread
from signal import signal, SIGINT
from sys import exit

from pynats import NATSClient

INTERVAL = 2.5

if __name__ == '__main__':
    print(f'Starting, will write a message every {INTERVAL} seconds')
    with NATSClient() as client:

        def listen_cb(msg: bytes):
            print(f'Received: {msg.payload.decode()}')
        sub = None
        def listen_forever():
            sub = client.subscribe(
                'test-subject-two',
                callback=listen_cb,
            )
            while True:
                client.wait(count=1)
        listen_thread = Thread(target=listen_forever)
        listen_thread.start()

        # client has no timeout, gets stuck by default
        def handler_sigint(signal_received, frame):
            print('SIGINT received, exiting...')
            # the thread may not be started yet
            if sub is not None:
                client.unsubscribe(sub)
            client.close()
            exit(0)

        signal(SIGINT, handler_sigint)
        while True:
            payload = ('Hello I am the Python test payload for '
                       f'{datetime.now().isoformat()}')
            print(f'Sending: {payload}')
            client.publish(
                'test-subject',
                payload=payload.encode()
            )

            sleep(INTERVAL)
