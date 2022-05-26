QUORIDOR-BOT

This bot is the result of the challenge of EDA/2022 from EvenBrite.
The challege was to create a bot thats plays QUORIDOR by connecting with a websocket.
To know about quoridor rules. Quoridor
To know about challenge rules EDA/2022

My strategy
My strategy to play was really simple. I use graphs to find the best path for each pawn in the board(both opponent’s and own pawns). Every path has a score (distance to de goal), and the bot select the path with lower score.

If the lowest path belongs to the opponent, the bot try to play a wall (if it’s posibble) and block the opponent path. In case that the lowest path belongs to the player the bot make the move.
