from BrandWatch import Watcher
import argparse

api_key = None # e.g. '12345678-1234-1234-1234-1234567890ab'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('brand')
    parser.add_argument('-e', '--exclude')
    args = parser.parse_args()
    
    if not args.exclude:
        w = Watcher(api_key=api_key, brand=args.brand)
    else:
        with open(args.exclude, 'rb') as f:
            exclude = f.read().splitlines()

        w = Watcher(api_key=api_key, brand=args.brand, exclude=exclude)

    w.search()
