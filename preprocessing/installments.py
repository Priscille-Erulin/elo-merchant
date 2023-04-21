import pandas as pd


def count_installments_by_card_id(df: pd.DataFrame) -> pd.DataFrame:
    """
    Counts the number of installments per card ID.
    """
    installments_by_card = df.groupby('card_id')['installments'].sum()
    installments_by_card_df = pd.DataFrame(installments_by_card).reset_index()
    installments_by_card_df = installments_by_card_df.rename(
        columns = {'installments': 'total_number_of_installments'}
    )

    return installments_by_card_df


def add_installments_feature(data: pd.DataFrame) -> pd.DataFrame:
    """
    Add the new feature in the train dataset.
    """
    historical_transactions = pd.read_csv("data/historical_transactions.csv")
    installments_by_card_df = count_installments_by_card_id(historical_transactions)
    train = data.merge(installments_by_card_df, on="card_id", how="left")

    return train