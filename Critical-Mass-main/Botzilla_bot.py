import copy
from collections import deque

# ---------------------------------
# Helpers
# ---------------------------------

def opponent(player_id):
    return 1 - player_id

def in_bounds(r, c, rows, cols):
    return 0 <= r < rows and 0 <= c < cols

def neighbors(r, c, rows, cols):
    dirs = [(-1,0), (1,0), (0,-1), (0,1)]
    result = []
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if in_bounds(nr, nc, rows, cols):
            result.append((nr, nc))
    return result

def critical_mass(r, c, rows, cols):
    return len(neighbors(r, c, rows, cols))

def valid_moves(state, player_id):
    rows = len(state)
    cols = len(state[0]) if rows else 0
    moves = []
    for r in range(rows):
        for c in range(cols):
            owner, _count = state[r][c]
            if owner is None or owner == player_id:
                moves.append((r, c))
    return moves

# ---------------------------------
# Apply move + chain reaction
# ---------------------------------

def apply_move(state, move, player_id):
    rows = len(state)
    cols = len(state[0]) if rows else 0

    board = copy.deepcopy(state)
    r, c = move

    owner, count = board[r][c]
    board[r][c] = (player_id, count + 1)

    q = deque()
    if board[r][c][1] >= critical_mass(r, c, rows, cols):
        q.append((r, c))

    while q:
        cr, cc = q.popleft()
        owner, count = board[cr][cc]
        cm = critical_mass(cr, cc, rows, cols)

        if count < cm:
            continue

        # explode current cell
        board[cr][cc] = (None, 0)

        for nr, nc in neighbors(cr, cc, rows, cols):
            n_owner, n_count = board[nr][nc]
            board[nr][nc] = (owner, n_count + 1)

            if board[nr][nc][1] >= critical_mass(nr, nc, rows, cols):
                q.append((nr, nc))

    return board

# ---------------------------------
# Evaluation
# ---------------------------------

def count_orbs(state, player_id):
    total = 0
    for row in state:
        for owner, count in row:
            if owner == player_id:
                total += count
    return total

def count_cells(state, player_id):
    total = 0
    for row in state:
        for owner, count in row:
            if owner == player_id and count > 0:
                total += 1
    return total

def corner_bonus(state, player_id):
    rows = len(state)
    cols = len(state[0]) if rows else 0
    corners = [(0,0), (0,cols-1), (rows-1,0), (rows-1,cols-1)]
    score = 0
    for r, c in corners:
        owner, count = state[r][c]
        if owner == player_id and count > 0:
            score += 8
    return score

def near_explosion_bonus(state, player_id):
    rows = len(state)
    cols = len(state[0]) if rows else 0
    score = 0

    for r in range(rows):
        for c in range(cols):
            owner, count = state[r][c]
            if owner == player_id and count > 0:
                cm = critical_mass(r, c, rows, cols)
                if count == cm - 1:
                    score += 6
                elif count == cm - 2:
                    score += 2
    return score

def danger_penalty(state, player_id):
    rows = len(state)
    cols = len(state[0]) if rows else 0
    opp = opponent(player_id)
    penalty = 0

    for r in range(rows):
        for c in range(cols):
            owner, count = state[r][c]
            if owner == player_id and count > 0:
                for nr, nc in neighbors(r, c, rows, cols):
                    n_owner, n_count = state[nr][nc]
                    if n_owner == opp:
                        cm = critical_mass(nr, nc, rows, cols)
                        if n_count == cm - 1:
                            penalty += 6
    return penalty

def evaluate(state, player_id):
    opp = opponent(player_id)

    my_orbs = count_orbs(state, player_id)
    opp_orbs = count_orbs(state, opp)

    my_cells = count_cells(state, player_id)
    opp_cells = count_cells(state, opp)

    score = 0
    score += 3 * (my_orbs - opp_orbs)
    score += 5 * (my_cells - opp_cells)
    score += corner_bonus(state, player_id)
    score += near_explosion_bonus(state, player_id)
    score -= danger_penalty(state, player_id)

    return score

# ---------------------------------
# Main decision
# ---------------------------------

def choose_best_move(state, player_id):
    moves = valid_moves(state, player_id)

    # prioritize cells with more existing orbs
    moves.sort(key=lambda m: state[m[0]][m[1]][1], reverse=True)

    best_move = moves[0]
    best_score = -10**18
    opp = opponent(player_id)

    for move in moves:
        new_state = apply_move(state, move, player_id)

        # Immediate win check
        my_cells_after = count_cells(new_state, player_id)
        opp_cells_after = count_cells(new_state, opp)

        if opp_cells_after == 0 and my_cells_after > 0:
            return move

        my_score = evaluate(new_state, player_id)

        # Small opponent lookahead
        opp_moves = valid_moves(new_state, opp)
        opp_best = -10**18

        for om in opp_moves[:12]:   # speed-safe
            after_opp = apply_move(new_state, om, opp)
            opp_best = max(opp_best, evaluate(after_opp, opp))

        final_score = my_score - opp_best

        # extra preference for corners
        rows = len(state)
        cols = len(state[0]) if rows else 0
        if move in [(0,0), (0,cols-1), (rows-1,0), (rows-1,cols-1)]:
            final_score += 5

        if final_score > best_score:
            best_score = final_score
            best_move = move

    return best_move

# ---------------------------------
# REQUIRED FUNCTION
# ---------------------------------

def get_move(state, player_id):
    """
    Smart heuristic-based Chain Reaction bot.
    Returns (row, col)
    """
    moves = valid_moves(state, player_id)
    if not moves:
        return (0, 0)

    return choose_best_move(state, player_id)