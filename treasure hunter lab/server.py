import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

player = [0, 0]
treasure = [3, 2]
moves = 0
game_over = False  # 1. Track whether the game has ended globally

def move(direction):
    # This acts as a bridge so the HTML can find it
    move_player(direction)


def move_player(direction):
    global player, moves, game_over
    
    # 2. Stop moving if the game is already over (won or 10 moves reached)
    if game_over:
        return

    if direction == "up" and player[1] > 0:
        player[1] -= 1
        moves += 1
    elif direction == "down" and player[1] < 4:
        player[1] += 1
        moves += 1
    elif direction == "left" and player[0] > 0:
        player[0] -= 1
        moves += 1
    elif direction == "right" and player[0] < 4:
        player[0] += 1
        moves += 1
        
    # Check if player hit the treasure after moving
    if player == treasure:
        game_over = True


def found_treasure():
    # 3. Return True if player is on the treasure
    return player == treasure


def is_game_over():
    global game_over, moves
    # 4. Game is over if they found the treasure OR reached/exceeded 10 moves
    return game_over or moves >= 10


def reset_game():
    global player, moves, game_over
    player = [0, 0]
    moves = 0
    game_over = False  # 5. Allow movement again on reset


def get_game_state():
    return {
        "player": player,
        "found": found_treasure(),
        "moves": moves,
        "game_over": is_game_over(),
    }



class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        url = urlparse(self.path)

        if url.path == "/":
            html = Path("index.html").read_text(encoding="utf-8")

            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(html.encode("utf-8"))

        elif url.path == "/move":
            direction = parse_qs(url.query).get("direction", [""])[0]
            move_player(direction)

            data = get_game_state()

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())

        elif url.path == "/reset":
            reset_game()

            data = get_game_state()

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())


server = HTTPServer(("localhost", 3000), MyHandler)
print("Server running at http://localhost:3000")
server.serve_forever()