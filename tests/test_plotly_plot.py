import plotbar
from plotbar.plotly import Plot


def test_multiple_traces():
    p = Plot()

    data = [
        {'x': 1, 'y': 1},
        {'x': 2, 'y': 4},
        {'x': 3, 'y': 9},
        {'x': 4, 'y': 16},
        {'x': 5, 'y': 25},
    ]
    layout = {
        'name': 'Scatter'
    }
    
    p.plot(data, layout)
    assert len(p.traces) == 1
    layout['name'] = 'Boxplot'
    p.boxplot(data, layout)
    assert len(p.traces) == 2
    p.show(auto_open=False)
