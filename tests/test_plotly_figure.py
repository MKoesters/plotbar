import plotbar
from plotbar.plotly import Plot, Figure


def test_plotly_figure():
    p1 = Plot()
    data_sc = [
        {'x': 1, 'y': 1},
        {'x': 2, 'y': 4},
        {'x': 3, 'y': 9},
        {'x': 4, 'y': 16},
        {'x': 5, 'y': 25},
    ]
    layout1 = {
        'name': 'Scatter'
    }
    p1.plot(data_sc, layout1)

    p2 = Plot()
    data_bp = [
        {'x': 1, 'y': 4},
        {'x': 2, 'y': 5},
        {'x': 3, 'y': 6},
        {'x': 4, 'y': 7},

    ]
    layout2 = {
        'name': 'Boxplot'
    }
    p2.boxplot(data_bp, layout2)

    f = Figure(
        [
            [p1, p2],
            [p2]
        ]
    )
    f.show(auto_open=False)
