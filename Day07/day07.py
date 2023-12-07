import numpy as np
from collections import Counter
from itertools import groupby

cards = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
hands = {
    (5): 0,
    (4, 1): 1,
    (3, 2): 2,
    (3, 1, 1): 3,
    (2, 2, 1): 4,
    (2, 1, 1, 1): 5,
    (1, 1, 1, 1, 1): 6,
}
joker = cards['J']

def parse_cards(card):
    return int(card) if card.isdigit() else cards[card]

def count_occurrences(hand, jokers=0):
    # count occurrences of each card
    occurrences = sorted(Counter(hand).values(), reverse=True)
    if not occurrences:
        occurrences = [0]
    # add number of jokers to the most common card
    occurrences[0] += jokers
    return tuple(occurrences)

def calculate_winning(hand):
    # sort by hand power
    hand = sorted(hand, key=lambda line: count_occurrences(line[0][1], len(line[0][2])))
    # group by hand type
    hand = groupby(hand, key=lambda line: count_occurrences(line[0][1], len(line[0][2])))
    # sort cards in groups
    hand = [sorted(group, key=lambda line: line[0][0]) for _, group in hand]
    hand = [line for group in hand for line in group]
    # calculate total winnings
    return np.sum(([line[1] for line in hand]) * np.arange(1, len(hand) + 1))

if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()

    # [parsed cards, score]
    cards = [
        [
            [parse_cards(cards) for cards in " ".join(line.split()[0]).split()],
            int(line.split()[1]),
        ]
        for line in lines
    ]
    # [[original hand, hand without jokers, only jokers], score]
    cards_1 = [[[hand[0], hand[0], []], hand[1]] for hand in cards]
    cards_2 = [
        [
            [
                [card if card != joker else 0 for card in hand[0]],
                [card for card in hand[0] if card != joker],
                [0 for card in hand[0] if card == joker],
            ],
            hand[1],
        ]
        for hand in cards
    ]

    print(f"Part 1 answer: {calculate_winning(cards_1)}")
    print(f"Part 2 answer: {calculate_winning(cards_2)}")
