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
        for i, p in enumerate(plots):
            i += 1
            if len(p) == cols:
                specs.append([{} for i in range(cols)])
                positions += [(i, j+1) for j in range(len(p))]
            elif  len(p) == 1:
                s = [{'colspan': cols}]
                s += [None for x in range(cols - 1)]
                positions.append((i, 1))
                specs.append(s)
            elif len(p) % cols == 0:
                l = len(p) / cols
                spec.append([{'colspan': l} for plot in p])
                positions += [(i, j+1) for j in range(len(p))]
            else:
                raise Exception('Strange layout')
        return specs, rows, cols, positions
