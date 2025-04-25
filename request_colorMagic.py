import requests
import matplotlib.pyplot as plt


r = requests.get('https://colormagic.app/api/palette/search?q=rainbow')
cleaned_data = [{"colors": item["colors"], "text": item["text"]} for item in r.json()]


plt.style.use('seaborn-v0_8-whitegrid')


for paleta in cleaned_data:
    fig, ax = plt.subplots(figsize=(len(paleta['colors']), 2))
    
    for i, color in enumerate(paleta['colors']):
        ax.add_patch(plt.Rectangle((i, 0), 1, 1, color=color, ec='black', lw=0.5))
    
    ax.set_xlim(0, len(paleta['colors']))
    ax.set_ylim(0, 1)
    ax.set_title(paleta['text'], fontsize=14, pad=20, fontweight='bold')
    ax.axis('off')
    
    plt.tight_layout()
    plt.show()