import json
import logging
import websockets
import asyncio
from src.utils.response_formatter import format_action_challenge
from src.player import play


class Client:

    def __init__(self, TOKEN):
        self.TOKEN = TOKEN
        self.ADRESS = "wss://4yyity02md.execute-api.us-east-1.amazonaws.com/ws?token="  # noqa: E501

    async def send(self, websocket, response):
        message = json.dumps(response)
        await websocket.send(message)

    async def start(self):
        uri = f"{self.ADRESS}{self.TOKEN}"

        while True:

            try:
                logging.info('connecting to server')

                async with websockets.connect(uri) as websocket:
                    # espera la coneccion con el servidor
                    conn_resp = await asyncio.wait_for(websocket.recv(), timeout=3)  # noqa: E501
                    json_conn_resp = json.loads(conn_resp)
                    logging.info('connected to the server')
                    logging.info('connected users:')
                    logging.info('-----------------')
                    for i in range(len(json_conn_resp['data']['users'])):
                        logging.info('*%s', json_conn_resp['data']['users'][i])

                    await self.recive(websocket)

            except asyncio.TimeoutError:
                logging.error('Login error. Your TOKEN maybe wrong. Try Again')
                raise asyncio.TimeoutError

            except Exception as e:
                logging.error('error {}'.format(str(e)))

    async def recive(self, websocket):
        while True:
            try:
                request = await websocket.recv()
                request_data = json.loads(request)

                if request_data['event'] == 'list_users':
                    logging.info('connected users(UPDATE):')
                    for i in range(len(request_data['data']['users'])):
                        logging.info('*s%', request_data['data']['users'][i])

                if request_data['event'] == 'gameover':
                    pass

                if request_data['event'] == 'challenge':

                    logging.info('challenged by ' + request_data['data']['opponent']) # noqa

                    if request_data['data']['opponent'] == 'lgior':
                        await self.send(websocket,
                                        format_action_challenge(request_data))
                        logging.info('challenge accepted')
                    else:
                        pass

                if request_data['event'] == 'your_turn':

                    response = await play.play(request_data)
                    await self.send(websocket, response)

            except Exception as e:
                logging.exception(e, e.with_traceback)
