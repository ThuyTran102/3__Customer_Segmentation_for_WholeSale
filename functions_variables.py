import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


########## 1.
def def_Draw_Histograms_Univariate(dataframe, features, nrows, ncols):
    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(16, 7))
    for i, feature in enumerate(features):
        row_index = i // ncols
        col_index = i % ncols
        ax = axes[row_index, col_index]
        sns.histplot(dataframe[feature], bins=20, kde=True, ax=ax)   #, color='midnightblue'
        ax.set_title(f"Distribution of {feature.replace('_',' ').title()}", color='DarkBlue')   
        ax.set_xlabel(feature.replace('_',' ').title())
        # ax.set_yscale('log') 
    plt.suptitle("Histogram and KDE chart for each numerical variable", color='DarkBlue')
    plt.tight_layout()
    plt.show()
              


########## 2.
def def_Draw_Boxplot_Univariate(dataframe, features, nrows, ncols):
    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(16,7))
    for i, feature in enumerate(features):
        row = i // ncols
        col = i % ncols
        ax = axes[row, col]
        sns.boxplot(data=dataframe[feature], orient='h', ax=ax)
    plt.suptitle("Boxplot chart for each numerical variable")
    plt.show()



########## 3. 
def def_Draw_Countplot_Univariate(dataframe, features, nrows=1, ncols=2):
    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(8, 3))
    
    # Ensure axes is always a 2D array for consistent indexing
    if nrows == 1 and ncols == 1:
        axes = [[axes]]
    elif nrows == 1:
        axes = [axes]
    elif ncols == 1:
        axes = [[ax] for ax in axes]

    # Flatten the axes array for easy iteration
    axes = [ax for row in axes for ax in row]

    for i, feature in enumerate(features):
        sns.countplot(data=dataframe, x=feature, ax=axes[i], palette="tab10")
        axes[i].set_xlabel(feature.replace('_', ' ').title())
        axes[i].set_ylabel("Count")
        axes[i].set_xticklabels(axes[i].get_xticklabels(), rotation=0)

        # Add annotations
        for p in axes[i].patches:
            height = p.get_height()
            axes[i].annotate(f'{height}', 
                             (p.get_x() + p.get_width() / 2., height), 
                             ha='center', va='bottom')

    plt.suptitle("Bar chart for each categorical variable", y=1.05)
    plt.tight_layout()
    plt.show()
