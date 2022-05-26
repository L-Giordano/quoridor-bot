import sys
import asyncio
import logging

from client.ws_client import Client


logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        client = Client(sys.argv[1])
        try:
            asyncio.get_event_loop().run_until_complete(client.start())
            client.start()
        except KeyboardInterrupt:
            logging.info('Exiting...')
        except asyncio.TimeoutError as e:
            logging.error('error {}'.format(str(e)))
            logging.info('Exiting...')

    else:
        logging.error('Please provide your auth_token and try again')
        logging.info('Exiting...')
