import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

colors = sns.color_palette("bright", 8)
explode = (0, 0.1)

#autopct_generator
def autopct_generator(limit=5):
    def inner_autopct(pct):
        return ('%.0f%%' % pct) if pct > limit else ''
    return inner_autopct

#function to plot percentage by column
def plot_percentage_by_column(data, column, target='target', 
                              explode=None, title=None, 
                              loc_legend="upper right", startangle=90, 
                              shadow=True,figsize=[12, 5],
                              legend_labels=None,
                              autopct=autopct_generator(5),
                               **kwargs):
  if legend_labels:
    gonna_plot = data[column].value_counts()[legend_labels]
  else:
    gonna_plot = data[column].value_counts()
  fig = plt.figure(figsize=figsize)
  plt.pie(gonna_plot, 
        colors=colors,
        explode=explode,
        startangle=startangle,
        shadow=shadow,
        wedgeprops={'edgecolor': 'black'}, 
        autopct=autopct,
        )
  if title:
    plt.title(title, fontsize="x-large", fontweight="bold")
  plt.legend(labels=gonna_plot.keys(), loc=loc_legend)
  return fig

#function to plot percentage by category
def plot_percentage_by_category(data, category, target='target', 
                                explode=(0, 0.1), title=None, 
                                loc_legend="upper right", 
                                y_title=1, startangle=90,
                                figsize=[12, 5], 
                                legend_labels = None,
                                autopct=autopct_generator(5),
                                shadow=True, **kwargs):
  percentage = data[[category, target]].value_counts().groupby(level=0).apply(lambda x: 100 * x / float(x.sum()))

  if legend_labels:
    list_temp = legend_labels
  else:
   list_temp = data[category].dropna().unique()

  fig, ax = plt.subplots(nrows=1, ncols=len(list_temp), figsize=figsize)
  for index, element in enumerate(list_temp):
    labels = percentage.loc[element].keys()
    ax[index].pie(percentage.loc[element],
                startangle=startangle, 
                colors=colors, 
                autopct=autopct_generator(),
                shadow=shadow,
                explode=explode,
                wedgeprops={'edgecolor': 'black'}, **kwargs)
    ax[index].set_title(f"Persentase {element}", fontweight="bold")
  
  if title:
    fig.suptitle(title, 
                fontsize=20, 
                fontweight='bold', y=y_title)
  fig.legend(loc=loc_legend, labels=labels, fontsize='x-large')
  return fig

# function for countplot
def plot_countplot(data, x, hue='target', title=None, xlabel=False, **kwargs):
  fig = plt.figure(figsize=(12, 5))
  ax = sns.countplot(data=data, x=x, hue=hue, palette=colors, **kwargs)

  if title:
    ax.set(title=title)

  if xlabel is not False:
    ax.set(xlabel=xlabel)
  plt.legend(fontsize="x-large")
  return fig