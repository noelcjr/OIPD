import argparse

import em.tools.input_output as IO


def register_parser(subparsers):
    parser = subparsers.add_parser('summary', usage=usage(), description=description())
    add_arguments(parser)


def add_arguments(parser):
    parser.add_argument("--input", metavar="FILE", help="Input File.", required=True)
    parser.set_defaults(func=run)


def run(options):
    IO.prepare_pdb_for_charmm(options.inputfile,options.crdout,options.seqfix)


def description():
    return '''
        This command gives a brief or summarized output of the structure as a guide for other commands.
        The output gives information that is relevant to biopython, and that options that will help decide
        command line inputs for other options for this program such as --align and --extract.
        The output gives information on number of models and chains.(TODO: This option is not coded yet)
            --summary              Flag to signal the program to do a summary.
            --input = FILE         Follow this option by the path to a file.'''


def usage():
    return 'pdb_cif.py --summary --input 1HIU.pdb'


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description=description())
    add_arguments(arg_parser)
    args = arg_parser.parse_args()
    args.func(args)
