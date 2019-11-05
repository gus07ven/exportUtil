import argparse


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', help='The path to the export file')
    parser.add_argument('--format', default='json', choices=['json', 'csv'],
                        type=str.lower,help='The format of the export file')
    return parser
