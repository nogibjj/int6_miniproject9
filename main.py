from fpdf import FPDF
from mylib.lib import read_data, calc_stats, create_viz, create_viz_tempo
import os

# create/save all visualizaiton
def create_all_viz(df, save):
    create_viz(df, save)
    create_viz_tempo(df, save)
    print("Visualizations saved to resources")


# create pdf report based on stats and visualizations
def create_report(data_path):
    # read data and get info
    df = read_data(data_path)
    dataset_name = os.path.basename(data_path)
    num_cols = df.shape[1]
    col_names = df.columns.tolist()

    # generate stats and visualizations if not already saved
    if not os.path.exists("resources/plot.png"):
        create_viz(df)
    if not os.path.exists("resources/stats_df.png"):
        calc_stats(df)

    # create empty PDF
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # title
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, txt=f"Summary Report for {dataset_name}", ln=True, align="C")

    # data summary
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, txt=f"Dataset: {dataset_name}", ln=True, align="L")
    pdf.cell(200, 10, txt=f"Number of Columns: {num_cols}", ln=True, align="L")
    pdf.cell(200, 10, txt="Columns/Variables:", ln=True, align="L")
    col_names_str = ", ".join(col_names)

    # format
    pdf.set_font("Arial", size=10)
    pdf.multi_cell(0, 10, txt=col_names_str)

    # summary stats
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, txt="Summary Statistics:", ln=True, align="L")
    pdf.image("resources/stats_df.png", x=10, y=None, w=180)

    # data viz
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, txt="Visualizations:", ln=True, align="L")
    pdf.image("resources/plot.png", x=10, y=None, w=180)
    pdf.image("resources/plot_tempo.png", x=10, y=None, w=180)

    # save report as PDF
    pdf_file = "spotify_report.pdf"
    pdf.output(pdf_file)
    print(f"Summary report written to {pdf_file}")
