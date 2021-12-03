from pkg_resources import DistributionNotFound, get_distribution

from .runner import LeetCode

try:
    __version__ = get_distribution("leetcode_runner").version
except DistributionNotFound:
    __version__ = "(local)"
