from pynats import NATSClient

if __name__ == '__main__':
    print('Starting...')
    with NATSClient() as client:
        client.publish(
            "test-subject",
            payload=b"Hello I am the Python test payload")
