def plot_customer_segments(data):
    import matplotlib.pyplot as plt
    import seaborn as sns

    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='feature1', y='feature2', hue='segment', data=data)
    plt.title('Customer Segments')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.legend(title='Segment')
    plt.show()

def plot_feature_importance(importances, feature_names):
    import matplotlib.pyplot as plt
    import numpy as np

    indices = np.argsort(importances)[::-1]
    plt.figure(figsize=(12, 6))
    plt.title('Feature Importances')
    plt.bar(range(len(importances)), importances[indices], align='center')
    plt.xticks(range(len(importances)), np.array(feature_names)[indices], rotation=90)
    plt.xlim([-1, len(importances)])
    plt.show()