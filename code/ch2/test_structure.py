from cards import Card


def test_to_dict():
    # GIVEN / Arrange a Card object with known contents
    c1 = Card("something", "brian", "todo", 123)

    # WHEN / Act we call to_dict() on the object
    c2 = c1.to_dict()

    # THEN / Assert the result will be a dictionary with known content
    c2_expected = {
        "summary": "something",
        "owner": "brian",
        "state": "todo",
        "id": 123,
    }
    assert c2 == c2_expected
