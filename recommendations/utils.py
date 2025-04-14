
import numpy as np





from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import seaborn as sns



def visualize(user_embeddings,ad_embeddings):
    all_vectors = np.array(user_embeddings + ad_embeddings)
    labels = ["user"] * len(user_embeddings) + ["ad"] * len(ad_embeddings)

    # Project
    tsne = TSNE(n_components=2, perplexity=5, random_state=42)
    coords = tsne.fit_transform(all_vectors)

    # Plot
    plt.figure(figsize=(10, 7))
    sns.scatterplot(x=coords[:, 0], y=coords[:, 1], hue=labels, palette=["blue", "orange"])

    for i, label in enumerate(labels):
        if label == "user":
            plt.text(coords[i, 0], coords[i, 1], f"U{i}", fontsize=7, color="blue")
        else:
            plt.text(coords[i, 0], coords[i, 1], f"A{i - len(user_embeddings)}", fontsize=7, color="orange")

    plt.title("Users & Ads in Topic Embedding Space")
    plt.xlabel("Dim 1")
    plt.ylabel("Dim 2")
    plt.grid(True)
    plt.legend()
    plt.show()
    