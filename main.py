import asyncio
import json
from random import randint
import sys
import websockets
import numpy as np
from board import get_board
from board import valid_white_move
from board import valid_black_move
from board import best_move_white
from board import best_move_black
import constant_values


async def send(websocket, action, data):
    message = json.dumps(
        {
            'action': action,
            'data': data,
        }
    )
    print(message)
    await websocket.send(message)


async def start(auth_token):
    uri = "ws://megachess.herokuapp.com/service?authtoken={}".format(constant_values.token)
    while True:
        print('connection to {}'.format(uri))
        async with websockets.connect(uri) as websocket:
            await play(websocket)


async def play(websocket):
    while True:
        try:
            response = await websocket.recv()
            print(f"< {response}")
            data = json.loads(response)
            if data['event'] == 'update_user_list':
                pass
            if data['event'] == 'gameover':
                pass
            if data['event'] == 'ask_challenge':
                if data['data']['username'] == 'dinok':
                    await send(
                        websocket,
                        'accept_challenge',
                        {
                            'board_id': data['data']['board_id'],
                        },
                    )
            if data['event'] == 'your_turn':
                #import ipdb;ipdb.set_trace()
                board = data['data']['board']
                b = get_board(board)
                player_color = data['data']['actual_turn']
                x = valid_white_move(b)
                y = valid_black_move(b)
                j = best_move_white(x)
                k = best_move_white(y)
                print('MY COLOR :',data['data']['actual_turn'])
                print('MOVES LEFT :',data['data']['move_left'])
                print('OPONENT :',data['data']['opponent_username'])
                #print('WHITE',x)
                #print('BLACK',y)

                if player_color == 'white':
                    #import ipdb;ipdb.set_trace()
                    await send(
                        websocket,
                        'move',
                        {
                            'board_id': data['data']['board_id'],
                            'turn_token': data['data']['turn_token'],
                            'from_row': j[0][0],
                            'from_col': j[0][1],
                            'to_row': j[0][2],
                            'to_col': j[0][3],
                        },
                    )
                else:
                    await send(
                        websocket,
                        'move',
                        {
                            'board_id': data['data']['board_id'],
                            'turn_token': data['data']['turn_token'],
                            'from_row': k[0][0],
                            'from_col': k[0][1],
                            'to_row': k[0][2],
                            'to_col': k[0][3],
                        },
                    )

        except Exception as e:
            print('error {}'.format(str(e)))
            break  # force login again


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(start(constant_values.token))