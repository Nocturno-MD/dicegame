import random
import sys
from colorama import init, Fore, Style

# Initialize colorama (works on Windows too)
init(autoreset=True)

# Colors
C_PLAYER1 = Fore.CYAN
C_PLAYER2 = Fore.YELLOW
C_ROLL = Fore.GREEN
C_BUST = Fore.RED
C_WIN = Fore.MAGENTA + Style.BRIGHT
C_RESET = Style.RESET_ALL

# --------------------------------------------------------------


def roll_dice() -> int:
    """Return a random dice value 1–6."""
    return random.randint(1, 6)


def clear_line():
    """Overwrite current line (for live updates)."""
    print("\r" + " " * 80 + "\r", end="")


def print_header():
    print(f"{C_WIN}╔{'═' * 48}╗{C_RESET}")
    print(f"{C_WIN}║{' DICE RACE TO 50 ':^48}║{C_RESET}")
    print(f"{C_WIN}╚{'═' * 48}╝{C_RESET}\n")


def print_scores(p1_name, p1_score, p2_name, p2_score, target=50):
    bar1 = "█" * (p1_score // 2)
    bar2 = "█" * (p2_score // 2)
    print(
        f"{C_PLAYER1}{p1_name:<12}{C_RESET} [{bar1:<25}] {p1_score:>3}/{target}")
    print(
        f"{C_PLAYER2}{p2_name:<12}{C_RESET} [{bar2:<25}] {p2_score:>3}/{target}\n")


def get_choice(player_name) -> str:
    """Ask r/s/q – validates input."""
    while True:
        choice = input(
            f"  {player_name} → (r)oll  (s)tay  (q)uit turn: "
        ).strip().lower()
        if choice in {"r", "s", "q"}:
            return choice
        print(f"   {C_ROLL}Please type r, s, or q.{C_RESET}")


# --------------------------------------------------------------
def play_turn(player_name, current_score, opponent_name, target=50):
    """One full turn. Returns updated score or None if passed."""
    print(f"{Style.BRIGHT}➤ {player_name}'s turn (score: {current_score}){Style.RESET_ALL}")
    turn_total = 0

    while True:
        # --- Roll ---
        roll = roll_dice()
        print(f"   Rolled: {C_ROLL}{roll}{C_RESET}", end="")

        if roll == 1:
            print(f" → {C_BUST}BUST!{C_RESET} Score reset to 0.")
            return 0  # Full reset

        turn_total += roll
        projected = current_score + turn_total
        win_msg = f" → {C_WIN}WIN!{C_RESET}" if projected >= target else ""
        print(f" | Turn: {turn_total} → Total: {projected}{win_msg}")

        # --- Win check ---
        if projected >= target:
            print(f"\n{C_WIN}🎉 {player_name} WINS THE GAME! 🎉{C_RESET}\n")
            return projected

        # --- Player decision ---
        choice = get_choice(player_name)

        if choice == "q":
            print(f"   {player_name} passes the turn.\n")
            return None  # Pass turn, score unchanged

        if choice == "s":
            new_score = current_score + turn_total
            print(f"   {player_name} banks {turn_total} → {new_score}\n")
            return new_score

        # else: 'r' → loop again


# --------------------------------------------------------------
def main():
    print_header()

    # Player names
    p1 = input("Player 1 name: ").strip() or "Player 1"
    p2 = input("Player 2 name: ").strip() or "Player 2"

    score1 = score2 = 0
    target = 50
    current = 1  # 1 = p1, 2 = p2

    while score1 < target and score2 < target:
        print_scores(p1, score1, p2, score2, target)

        if current == 1:
            result = play_turn(p1, score1, p2, target)
            if result is None:
                pass  # turn passed
            else:
                score1 = result
            current = 2
        else:
            result = play_turn(p2, score2, p1, target)
            if result is None:
                pass
            else:
                score2 = result
            current = 1

        # Small pause for readability
        input(f"{Fore.BLUE}Press Enter to continue...{C_RESET}")

    # Final screen
    print_header()
    print_scores(p1, score1, p2, score2, target)
    winner = p1 if score1 >= target else p2
    print(f"{C_WIN}🏆 {winner} IS THE CHAMPION! 🏆{C_RESET}\n")
    print("Thanks for playing!\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{C_ROLL}Game interrupted. Bye!{C_RESET}")
        sys.exit(0)
