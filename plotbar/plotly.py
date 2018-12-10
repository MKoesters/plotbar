import plotly.offline as plt
import plotly.graph_objs as go
from plotly import tools


class Plot:
    def __init__(self, layout=None):
        """Initialize Plot object.

        Args:
            layout (dict): plotly style layout dict.
        """
        self.layout = layout
        self.traces = []

    def boxplot(self, data, layout):
        """Create boxplot.

        Args:
            data (list): list of dicts, wheras each dicts contains one data point
            layout (dict): plotly style layout dict.
        """
        data = self._convert_data(data)
        layout = self._convert_layout(layout)
        bp = go.Box(y=data['y'], **layout)
        self.traces.append(bp)

    def show(self, auto_open=False):
        """Display plot.
        """
        plt.plot(self.traces, auto_open=auto_open)

    def plot(self, data, layout):
        """Create scatter plot.
        """
        data = self._convert_data(data)
        layout = self._convert_layout(layout)
        sc = go.Scatter(**data, **layout)
        self.traces.append(sc)

    def save(self):
        """Save plot as pickle.
        """
        pass

    def load(self):
        """Load plot from pkl.
        """
        pass

    def _convert_data(self, data):
        """Convert data to plotly api.

        Args:
            data (TYPE): Description
        """
        new_data = {}
        for data_point in data:
            for key, value in data_point.items():
                if key not in new_data:
                    new_data[key] = []
                new_data[key].append(value)
        return new_data

    def _convert_layout(self, layout):
        """Convert layout to plotly api

        Args:
            layout (TYPE): Description
        """
        return layout


class Figure:
    def __init__(self, plots):
        """Summary

        Args:
            plots (TYPE): Description
        """
        self.plots = plots

    def show(self, auto_open=False):

        specs, rows, cols, positions = self._get_layout(self.plots)
        fig = tools.make_subplots(
            rows=rows,
            cols=cols,
            specs=specs,
        )
        flat_plots = sum(self.plots, [])
        for plot, coords in zip(flat_plots, positions):
            if plot is None:
                continue
            for trace in plot.traces:
                fig.append_trace(trace, coords[0], coords[1])
        plt.plot(fig, auto_open=auto_open)

    def save(self, filename):
        """Summary

        Args:
            filename (TYPE): Description
        """
        pass

    def load(self, filename):
        """Summary

        Args:
            filename (TYPE): Description
        """
        pass

    def _get_layout(self, plots):
        """Summary

        Args:
            plots (TYPE): Description
        """
        specs = []
        rows = len(plots)
        cols = max([len(p) for p in plots])
        positions = []
        for plot_list in plots:
            if len(plot_list) < cols:
                plot_list += [None] * (cols - len(plot_list))

        for i, row in enumerate(plots):
            # iter subplots reversely
            specs.append([])
            colspan = 1
            COLSPAN = False
            for plot in row[::-1]:
                if plot is None:
                    specs[-1].append(None)
                    colspan += 1
                    COLSPAN = True
                else:
                    if COLSPAN is True:
                        specs[-1].append({'colspan': colspan})
                    else:
                        specs[-1].append({})
                    colspan = 1
                    COLSPAN = False
            specs[-1] = specs[-1][::-1]
        i = 0
        j = 0
        for i, s in enumerate(specs):
            i += 1
            for j, _s in enumerate(s):
                j += 1
                positions.append((i, j))

        return specs, rows, cols, positions
