from argparse import ArgumentParser
from lib.benchmark import benchmark
"""
Data paths
"""
parser = ArgumentParser()
parser.add_argument('-g', '--gt', help='Path to a folder containing folders of ground-truth masks')
parser.add_argument('-m', '--mask', help='Path to a folder containing folders of masks to be evaluated')
parser.add_argument('-n', '--num_processes', default=16, type=int, help='Number of concurrent processes')
parser.add_argument('-s', '--strict', help='Make sure every video in the ground-truth has a corresponding'
    ' video in the prediction', action='store_true')

# https://github.com/davisvideochallenge/davis2017-evaluation/blob/d34fdef71ce3cb24c1a167d860b707e575b3034c/davis2017/evaluation.py#L85
# https://github.com/hkchengrex/vos-benchmark/blob/acb47337f2c5677c0e6556590baad0563dfbb000/benchmark.py#L23
parser.add_argument('-d', '--dataset', help='Dataset name. If set to "DAVIS16", "DAVIS2017", "MOSXAV-VAL", and '
    '"MOSXAV-TEST" the first and last frames will be skipped. Otherwise, they will not be skipped. '
    'This evaluation is only suitable for semi-supervised evaluation. The "Other" dataset is not currently supported, '
    'but development is ongoing. "MOSXAV-VAL" and "MOSXAV-TEST" are the validation and test sets of MOSXAV.',
    choices=['DAVIS2016', 'DAVIS2017', 'MOSXAV-VAL', 'MOSXAV-TEST', 'XACV', 'Other'], default='MOSXAV-VAL')
args = parser.parse_args()

benchmark([args.gt], [args.mask], args.dataset, args.strict, args.num_processes, verbose=True)
