"""Main module for the plugin."""
from dslinter.checkers.hyperparameters import HyperparameterChecker
from dslinter.checkers.imports import ImportChecker
from dslinter.checkers.sample import SampleChecker


def register(linter):
    """
    Register checkers of the plugin with the linter.

    :param linter: Linter to add the checkers to.
    """
    linter.register_checker(SampleChecker(linter))
    linter.register_checker(ImportChecker(linter))
    linter.register_checker(HyperparameterChecker(linter))
