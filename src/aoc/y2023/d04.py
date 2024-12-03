from dataclasses import dataclass
from functools import cached_property

from aoc.utils import runner


class Card:
    def __init__(self, winners: list[str], numbers: list[str]) -> None:
        self.winners = winners
        self.numbers = numbers

    @cached_property
    def score(self) -> int:
        if not self.matches:
            return 0
        return 2 ** (len(self.matches) - 1)

    @cached_property
    def matches(self) -> set[str]:
        return set(self.winners) & set(self.numbers)

    @staticmethod
    def from_line(text: str) -> "Card":
        groups = text.split(":")[-1].strip()
        winners, numbers = groups.split(" | ")
        winners = winners.split()
        numbers = numbers.split()
        return Card(winners, numbers)


@dataclass
class CardCache:
    number: int
    card: Card
    quantity: int


class CardPile:
    def __init__(self, starting_cards: list[Card]) -> None:
        self.cards: list[CardCache] = []
        for i, card in enumerate(starting_cards, start=1):
            self.cards.append(CardCache(i, card, 1))
        self.processed = False

    def process_cards(self):
        for idx, cache in enumerate(self.cards):
            matches = len(cache.card.matches)
            for i in range(matches):
                next_card = self.cards[idx + i + 1]
                next_card.quantity += cache.quantity

    def total_cards(self) -> int:
        if not self.processed:
            self.process_cards()
        return sum(card.quantity for card in self.cards)


def part1(input_data: str) -> int:
    cards = [Card.from_line(line) for line in input_data.splitlines()]
    return sum(card.score for card in cards)


def part2(input_data: str) -> int:
    cards = [Card.from_line(line) for line in input_data.splitlines()]
    pile = CardPile(cards)
    return pile.total_cards()


if __name__ == "__main__":
    runner([(part1, 13), (part2, 30)])
