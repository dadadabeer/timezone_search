import argparse
from sys import argv, exit, stderr
from midterm import app

def main(port):
    try:
        port = int(port)
    except Exception:
        print('Port must be an integer.', file=stderr)
        exit(1)

    try:
        app.run(host='0.0.0.0', port=port, debug=True)
    except Exception as ex:
        print(ex, file=stderr)
        exit(1)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description = 'A timezone application.',
                                     allow_abbrev = False)
    parser.add_argument('port', help='the port at which the server should listen')
    args = parser.parse_args()
    main(args.port)