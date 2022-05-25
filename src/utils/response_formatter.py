
def format_action_your_turn(request_data, response):
    if response["action"] == 'move':
        msg = {
            "action": "move",
            "data": {
                "game_id": request_data['data']['game_id'],
                "turn_token": request_data['data']['turn_token'],
                "from_row": response['data']["from_row"],
                "from_col": response['data']["from_col"],
                "to_row": response['data']["to_row"],
                "to_col": response['data']["to_col"]
                    }
            }

    if response["action"] == 'wall':
        msg = {
            "action": "wall",
            "data": {
                "game_id": request_data['data']['game_id'],
                "turn_token": request_data['data']['turn_token'],
                "row": response['data']["row"],
                "col": response['data']["col"],
                "orientation": response['data']["orientation"]
                }
            }
    return msg


def format_action_challenge(request_data):
    msg = {
        "action": 'accept_challenge',
        "data": {
                "challenge_id": request_data['data']["challenge_id"]
                }
        }
    return msg
