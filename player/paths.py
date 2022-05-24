import random
import time
import networkx as nx
from graphs.graphs import Q_graph

def f_paths(player_data,opp_data):

    player_paths=calc_path(player_data)

    opp_paths=calc_path(opp_data)

    player_score=path_score(player_paths,player_data['side'])
    opp_score=path_score(opp_paths,opp_data['side'])

  
    all_scores=player_score+opp_score
    all_scores.sort(key=lambda path:path['score'])


    return (all_scores)

def calc_path(player_data):
    player_pos=player_data['player_pos']
    goal_pos=player_data['player_goal_pos']
    q_graph=player_data['q_graph']

    paths=[]

    for i in range(len(player_pos)):
        for j in range(len(goal_pos)):
            try:
                paths.append(list(nx.astar_path(q_graph,player_pos[i], goal_pos[j], weight=1)))
            except Exception as e:
                print('aca ',e)
                pass
    return paths 
    
def path_score(paths, side):

    scored_paths=[]
    for i in range(len(paths)):

        score={
            'player':side,
            'steps': len(paths[i]),
            'data':{
                'from_row':paths[i][0][0],
                'from_col':paths[i][0][1],
                'to_row':paths[i][1][0],
                'to_col':paths[i][1][1],
            },
            'score':len(paths[i])
        }

        scored_paths.append(score)
    return scored_paths

