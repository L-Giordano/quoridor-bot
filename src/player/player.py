
import copy
import numpy as np
from src.player.paths import f_paths
from src.utils.response_formatter import format_action_your_turn
from src.graph.graphs import Q_graph
from src.player.wall import create_wall
from src.utils.board_printer import board_printer

async def play(request_data):

    board_printer(request_data)


    matrix_board=str_board_to_matrix(request_data['data']['board'])

    p_data=player_data(request_data,'player',matrix_board)
    o_data=player_data(request_data,'opp',matrix_board)

    all_paths=f_paths(p_data,o_data)

    selected_play= select_play(all_paths,request_data,o_data,p_data)


    response=format_action_your_turn(request_data,selected_play)

    return response

def str_board_to_matrix(str_board):    
    matrix = np.array(list(str_board), dtype=str)
    matrix = matrix.reshape(17,17)
    return matrix


def pawns_pos(board, side):
    positions=[]
    for i in range(9):
        for j in range(9):
            if board[i*2][j*2]==side:
                positions.append((i,j))
        
    return positions

def goal_positions(board,side):
    goal_row=16 if side=='N' else 0
    goal_pos=[]
    for i in range(9):
        if board[goal_row][i*2]==" ":
            goal_pos.append((goal_row//2,i))
    return goal_pos

def player_data(request_data,player,board):

    side=None

    if player=='player':
        side=request_data['data']['side']
    else:
        side='N' if request_data['data']['side']=='S' else 'S'

    opp_side='N' if side=='S' else 'S'

    q_graph=Q_graph()
    q_graph.set_board(board)
    q_graph.set_opp(opp_side)
    q_graph.create_graph()

    return{
        'side': side,
        'opp_side':'N' if side=='S' else 'N',
        'player_pos':pawns_pos(board, side),
        'player_goal_pos':goal_positions(board,side),
        'q_graph':q_graph
    }

def select_play(all_paths, request_data,o_data,p_data):

    for i in range(len(all_paths)):

        if ((all_paths[i]['player']!=request_data['data']['side'])
            and(request_data['data']['remaining_moves']>0)):

            o_wall_graph= copy.deepcopy(o_data['q_graph'])
            p_wall_graph= copy.deepcopy(p_data['q_graph'])

            
            wall=create_wall(all_paths[i]['data'],o_wall_graph,p_wall_graph,o_data,p_data)

            if (wall==None):
                continue
            else:
                return {
                    'action':'wall',
                    'data':{
                        'row':wall[1],
                        'col':wall[2],
                        'orientation':wall[0]
                    }
                }
        else:
          
            return {
                'action':'move',
                'data':{
                    'from_row':all_paths[i]['data']['from_row'],
                    'from_col':all_paths[i]['data']['from_col'],
                    'to_row':all_paths[i]['data']['to_row'],
                    'to_col':all_paths[i]['data']['to_col']
                }
            }
