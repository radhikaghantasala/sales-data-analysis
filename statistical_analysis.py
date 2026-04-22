def correlation(df):
    return df["Sales"].corr(df["Profit"])


def average_sales(df):
    return df["Sales"].mean()


def max_sales(df):
    return df["Sales"].max()