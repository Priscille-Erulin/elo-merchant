from train import train


def test_train():
    df = train()
    assert set(df.columns) == {"card_id", "target"}
