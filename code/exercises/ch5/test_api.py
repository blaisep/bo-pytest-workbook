from cards import Card
import pytest

# def test_start_from_in_prog(cards_db):
#     index = cards_db.add_card(Card("second edition", state="in prog"))
#     cards_db.start(index)
#     card = cards_db.get_card(index)
#     assert card.state == "in prog"
#
#
# def test_start_from_done(cards_db):
#     index = cards_db.add_card(Card("write a book", state="done"))
#     cards_db.start(index)
#     card = cards_db.get_card(index)
#     assert card.state == "in prog"
#
#
# def test_start_from_todo(cards_db):
#     index = cards_db.add_card(Card("create a course", state="todo"))
#     cards_db.start(index)
#     card = cards_db.get_card(index)
#     assert card.state == "in prog"


# @pytest.mark.parametrize(               # FUNCTION parametrize
#     "start_summary, start_state",       # The names of the parameters
#     [
#         ("write a book", "done"),       # The list of test cases, or number of times the FUNCTION will run
#         ("second edition", "in prog"),
#         ("create a course", "todo"),
#     ],
# )

# @pytest.fixture(params=["done", "in prog", "todo"])     # FIXTURE parametrize
# def start_state(request):
#     return request.param                                # pytest calls once for each of the params.

def pytest_generate_tests(metafunc):
    if "start_state" in metafunc.fixturenames:
        metafunc.parametrize("start_state", ["done", "in prog", "todo"])


def test_start(cards_db, start_state):  # The parameters
    initial_card = Card("Write some tests", state=start_state)
    index = cards_db.add_card(initial_card)

    cards_db.start(index)

    card = cards_db.get_card(index)
    assert card.state == "in prog"
