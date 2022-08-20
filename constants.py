import itertools as it

RANKS = [rank for rank in range(2, 15)]
SUITS = ["s", "h", "c", "d"]
CARDS = list(range(52))
CARD_PAIRS = list(it.combinations(CARDS, 2))
CARDS_REPR = [str(rank) + suit for suit in SUITS for rank in RANKS]
CARDS_NUM = dict([(CARDS_REPR[i], i) for i in range(52)])
FIVE_CARD_SETS = list(it.combinations(CARDS, 5))
