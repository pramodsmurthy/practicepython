"""
Reads a json file, extracts birthdays info from file, plots birthdays based on months.
"""
from bokeh.plotting import figure, show, output_file
from OnlineExamples.birthdayDictsJson import read_file
from OnlineExamples.birthdayMonthExt import count_months

def plot_months(month_count):
    months = list(month_count.keys())
    counts = list(month_count.values())
    output_file("plot.html")
    print(months)
    print(counts)
    p = figure(x_range = months)
    p.vbar(x=months, top=counts, width=0.5)
    show(p)

def main():
    file_loc = "C:\\Users\\pkrishna\\eclipse-workspace\\python\\OnlineExPractice\\OnlineExamples\\dicts.json"
    birthdays = read_file(file_loc)
    month_count = count_months(birthdays)
    plot_months(month_count)    

if __name__ == "__main__":
    main()