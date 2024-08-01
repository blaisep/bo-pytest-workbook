import pytest
from cards import Card


@pytest.fixture(params=["done", "in prog", "todo"])     # FIXTURE parametrize
def start_state(request):
    return request.param                                # pytest calls once for each of the params.    
                                                        # It can be as simple as a value or we can do some work each time.


def test_finish(cards_db, start_state):
    c = Card("write a book", state=start_state)
    index = cards_db.add_card(c)
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == "done"
