import os
from mylib.lib import read_data
from main import create_all_viz, create_report

data_path = "data/spotify.csv"


def test_create_all_viz():
    df = read_data(data_path)
    create_all_viz(df, save=True)

    # verify file was created and not empty
    assert os.path.exists("resources/plot.png"), "The plot.png file does not exist."
    assert os.path.exists(
        "resources/plot_tempo.png"
    ), "The plot_tempo.png file does not exist."
    assert os.path.getsize("resources/plot.png") > 0, "The plot.png file is empty."
    assert (
        os.path.getsize("resources/plot_tempo.png") > 0
    ), "The plot_tempo.png file is empty."
    print("All assertions passed for test_create_viz.")


def test_generate_report():
    create_report(data_path)
    assert os.path.exists(
        "spotify_report.pdf"
    ), "The spotify_report.pdf file does not exist."
    assert (
        os.path.getsize("spotify_report.pdf") > 0
    ), "The spotify_report.pdf file is empty."
    print("All assertions passed for test_generate_report.")


if __name__ == "__main__":
    test_create_all_viz()
    test_generate_report()
