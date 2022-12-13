import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Advent of Code solutions")
    parser.add_argument("day", help="The day to run", type=int)
    parser.add_argument("--demo", action="store_true", help="Run the demo input")
    args = parser.parse_args()

    day = args.day
    demo = args.demo

    exec_res = {}
    exec(f"from day{day}.day{day} import main", exec_res)

    exec_res["main"](demo)
