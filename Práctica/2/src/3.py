from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt
import polars as pl
from sklearn.linear_model import LinearRegression

# Configuration
FILTER_DATES = True  # True = remove date range, False = use all data
EXCEL_FILE = Path(__file__).parent.parent / "META.xlsx"
START_DATE = datetime(year=2024, month=2, day=2)  # noqa: DTZ001
END_DATE = datetime(year=2024, month=4, day=24)  # noqa: DTZ001


def load_data(file_path: Path, filter_dates: bool = False) -> pl.DataFrame:
    df = pl.read_excel(file_path)

    if filter_dates:
        # Only parse if the column came in as text; Excel date cells are
        # already read as a temporal dtype by polars.
        if df.schema["Date"] == pl.String:
            df = df.with_columns(pl.col(name="Date").str.to_datetime(format="%m/%d/%Y"))
        else:
            df = df.with_columns(pl.col(name="Date").cast(dtype=pl.Datetime))

        df = df.filter(
            ~((pl.col(name="Date") >= START_DATE) & (pl.col(name="Date") <= END_DATE)),
        )

    return df


def linear_regression(df: pl.DataFrame):
    days_passed = df["Dias"].to_numpy().reshape(-1, 1)
    money = df["Precio U$D"].to_numpy()

    model = LinearRegression()
    model.fit(X=days_passed, y=money)

    slope = model.coef_[0]
    intercept = model.intercept_

    print(f"Linear Regression Model: y = {slope}x + {intercept}")

    predictions = model.predict(X=days_passed)
    r_squared = model.score(X=days_passed, y=money)

    print(f"R² = {r_squared}")

    return days_passed, money, predictions


def plot_results(days_passed, money, predictions) -> None:
    plt.scatter(days_passed, money, color="blue", label="Actual data")
    plt.plot(days_passed, predictions, color="red", label="Regression line")

    plt.xlabel(xlabel="Number of Days Passed")
    plt.ylabel(ylabel="Money")
    plt.title(label="Linear Regression: Money vs Days Passed")

    plt.legend()
    plt.show()


# Main execution
df = load_data(EXCEL_FILE, filter_dates=FILTER_DATES)

days_passed, money, predictions = linear_regression(df)

plot_results(days_passed, money, predictions)
