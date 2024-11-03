from mylib.lib import read_data, calc_stats, create_viz, create_viz_tempo
import os

data_path = "data/spotify.csv"

# test read_data will work from lib.py
def test_read_data():
    df = read_data(data_path)
    assert df is not None
    assert df.shape == (114000, 21)
    df.head()


# test calc_stats will work from lib.py
def test_calc_stats():
    df = read_data(data_path)
    summary_stats = calc_stats(df)
    # assert that calculations match
    assert summary_stats[summary_stats["column"] == "popularity"]["mean"].values[
        0
    ] == round(df["popularity"].mean(), 2)
    assert summary_stats[summary_stats["column"] == "popularity"]["median"].values[
        0
    ] == round(df["popularity"].median(), 2)
    assert summary_stats[summary_stats["column"] == "popularity"]["std_dev"].values[
        0
    ] == round(df["popularity"].std(), 2)
    print("All assertions passed for calc_stats.")


# test visualizations
def test_create_viz():
    df = read_data(data_path)
    create_viz(df, save=True)
    # verify file was created and not empty
    assert os.path.exists("resources/plot.png"), "The plot.png file does not exist."
    assert os.path.getsize("resources/plot.png") > 0, "The plot.png file is empty."


def test_create_viz_tempo():
    df = read_data(data_path)
    create_viz_tempo(df, save=True)
    # verify file was created and not empty
    assert os.path.exists(
        "resources/plot_tempo.png"
    ), "The plot_tempo.png file does not exist."
    assert (
        os.path.getsize("resources/plot_tempo.png") > 0
    ), "The plot_tempo.png file is empty."
    print("All assertions passed for test_create_viz.")


if __name__ == "__main__":
    test_read_data()
    test_calc_stats()
    test_create_viz()
    test_create_viz_tempo()
