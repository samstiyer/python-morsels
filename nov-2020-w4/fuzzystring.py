
"""
This week I'd like you to write a FuzzyString class which acts like a string, but does comparisons in a case-insensitive way.

For example:

>>> greeting = FuzzyString('Hey TREY!')
>>> greeting == 'hey Trey!'
True
>>> greeting == 'heyTrey'
False
>>> greeting
'Hey TREY!'

I'd like you to make sure equality and inequality match case-insensitively at first. I'd also like you to ensure that the string representations of your class match Python's string objects' default string representations.

For the first bonus, try to ensure the other comparison operators work as expected:

Bonus 1

>>> o_word = FuzzyString('Octothorpe')
>>> 'hashtag' < o_word
True
>>> 'hashtag' > o_word
False

Bonus 2

For the second bonus, ensure your FuzzyString class works with string concatenation and the in operator:

>>> o_word = FuzzyString('Octothorpe')
>>> 'OCTO' in o_word
True
>>> new_string = o_word + ' (aka hashtag)'
>>> new_string == 'octothorpe (AKA hashtag)'
True

Bonus 3

For the third bonus, also make your string normalize unicode characters when checking for equality:

>>> ss = FuzzyString('ss')
>>> '\u00df' == ss
True
>>> e = FuzzyString('\u00e9')
>>> '\u0065\u0301' == e
True
>>> '\u0301' in e
True
"""
from functools import total_ordering
import unicodedata


@total_ordering
class FuzzyString:
    def __init__(self, s: str) -> None:
        self._s = s

    @property
    def s(self) -> str:
        return unicodedata.normalize("NFKD", self._s.casefold())

    def __repr__(self) -> str:
        return f"{self._s!r}"

    def __str__(self) -> str:
        return self._s

    def __eq__(self, other_s: str) -> bool:
        return self.s == unicodedata.normalize("NFKD", other_s.casefold())

    def __ne__(self, other_s: str) -> bool:
        return self.s != unicodedata.normalize("NFKD", other_s.casefold())

    def __lt__(self, other_s: str) -> bool:
        if self.s < other_s.lower():
            return True
        else:
            return False

    def __gt__(self, other_s: str) -> bool:
        if self.s > other_s.lower():
            return True
        else:
            return False

    def __add__(self, other_s: str):
        self._s = self._s + other_s
        return self

    def __contains__(self, other_s: str) -> bool:
        if other_s.lower() in self.s:
            return True
        else:
            return False
