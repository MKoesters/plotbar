import plotbar
from plotbar.plotly import Plot, Figure


def main():
    p1 = Plot()
    data_sc = [
        {'x': 1, 'y': 1},
        {'x': 2, 'y': 4},
        {'x': 3, 'y': 9},
        {'x': 4, 'y': 16},
        {'x': 5, 'y': 25},
    ]
    data_bp = [
        {'x': 1, 'y': 4},
        {'x': 1, 'y': 5},
        {'x': 1, 'y': 6},
        {'x': 1, 'y': 7},

    ]
    layout1 = {
        'name': 'Scatter'
    }
    p1.plot(data_sc, layout1)
    p1.boxplot(data_bp, layout1)

    p2 = Plot()
    layout2 = {
        'name': 'Boxplot'
    }
    p2.boxplot(data_bp, layout2)

    f = Figure(
        [
            [p1, p2, p1, p2],
            [p1, None, p2, None],
        ]
    )
    f.show(auto_open=False)

if __name__ == '__main__':
    main()
