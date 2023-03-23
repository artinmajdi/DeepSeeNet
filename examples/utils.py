import logging

import docopt


def get_args(args):
    return ''.join(f'    {k}: {args[k]}\n' for k in args)


def parse_args(doc, **kwargs):
    argv = docopt.docopt(doc, **kwargs)
    if argv['--verbose']:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)
    logging.debug('Arguments:\n%s', get_args(argv))
    return argv