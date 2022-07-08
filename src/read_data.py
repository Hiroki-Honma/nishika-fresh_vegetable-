import pandas as pd
import japanize_matplotlib
import os


def main():
    cwd = os.path.split(os.path.dirname(__file__))[0]
    data_path = os.path.join(os.path.join(cwd, "../data"))
    modified_data_path = os.path.join(os.path.join(cwd, "../modified_data"))
    res_path = os.path.join(os.path.join(cwd, "../result"))
    # save_path = os.path.join(os.path.join(res_path, 'BasicPrinciplesOfBayesianStatistics'))

    if not os.path.exists(res_path):
        os.mkdir(res_path)

    if not os.path.exists(modified_data_path):
        os.mkdir(modified_data_path)

    df_train = pd.read_csv(os.path.join(data_path, "train.csv"))
    df_train.rename(columns={'area':'area_1'}, inplace=True)
    print(df_train.columns)

    df_train.to_csv(
        os.path.join(modified_data_path, "train.csv"), encoding="shift-jis", index=False
    )
    pd.read_csv(os.path.join(data_path, "test.csv")).to_csv(
        os.path.join(modified_data_path, "test.csv"), encoding="shift-jis", index=False
    )
    pd.read_csv(os.path.join(data_path, "weather.csv")).to_csv(
        os.path.join(modified_data_path, "weather.csv"),
        encoding="shift-jis",
        index=False,
    )
    pd.read_csv(os.path.join(data_path, "weather.csv")).to_csv(
        os.path.join(modified_data_path, "weather.csv"),
        encoding="shift-jis",
        index=False,
    )
    pd.read_csv(os.path.join(data_path, "sample_submission.csv")).to_csv(
        os.path.join(modified_data_path, "sample_submission.csv"),
        encoding="shift-jis",
        index=False,
    )


if __name__ == "__main__":
    main()
