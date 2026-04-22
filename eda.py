import matplotlib.pyplot as plt

def plot_sales(df):
    plt.figure()
    plt.plot(df["Month"], df["Sales"], marker='o')
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.grid()
    plt.show()


def plot_profit(df):
    plt.figure()
    plt.bar(df["Month"], df["Profit"])
    plt.title("Monthly Profit")
    plt.xlabel("Month")
    plt.ylabel("Profit")
    plt.show()