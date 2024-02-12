import argparse


def hello():
    return "Hello from anyglobal!"


def main():
    parser = argparse.ArgumentParser(description="Description of your program")
    parser.add_argument("--path", help="Specify the path")
    args = parser.parse_args()

    # Access the specified path using args.path
    if args.path:
        print("Path specified:", args.path)
    else:
        print("No path specified.")

    # Call hello function
    print(hello())


if __name__ == "__main__":
    main()
