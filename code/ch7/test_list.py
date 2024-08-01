"""
Test Cases
* `list` from an empty database
* `list` from a non-empty database
* 'list' with filtering by owner, state, owner+state
"""
from cards import Card


def test_list_no_cards(cards_db):
    """Empty db, empty list"""
    assert cards_db.list_cards() == []


def test_list_several_cards(cards_db):
    """
    Given a variety of cards, make sure they get returned.
    """
    orig = [
        Card("foo"),
        Card("bar", owner="me"),
        Card("baz", owner="you", state="in prog"),
    ]

    for c in orig:
        cards_db.add_card(c)

    the_list = cards_db.list_cards()

    assert len(the_list) == len(orig)
    for c in orig:
        assert c in the_list

def test_list_owner_state(cards_db):
    orig = [
        Card("foo"),
        Card("bar", owner="me"),
        Card("baz", owner="you", state="in prog"),
    ]

    for c in orig:
        cards_db.add_card(c)

    the_list = cards_db.list_cards(owner="you", state="in prog")

    assert len(the_list) == 1

    for card in orig:
        if card.owner == "you" and card.state == "in prog":
            assert card in the_list

def test_list_owner(cards_db):
    orig = [
        Card("foo"),
        Card("bar", owner="me"),
        Card("baz", owner="you", state="in prog"),
    ]

    for c in orig:
        cards_db.add_card(c)

    the_list = cards_db.list_cards(owner="me")

    assert len(the_list) == 1
    for card in orig:
        if card.owner == "me":
            assert card in the_list

def test_list_state(cards_db):
    orig = [
        Card("foo"),
        Card("bar", owner="me"),
        Card("baz", owner="you", state="in prog"),
    ]

    for c in orig:
        cards_db.add_card(c)

    the_list = cards_db.list_cards(state="in prog")

    assert len(the_list) == 1
    for card in orig:
        if card.owner == "in prog":
            assert card in the_list
