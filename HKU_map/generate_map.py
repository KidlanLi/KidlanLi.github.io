import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(SCRIPT_DIR)

try:
    import prettymaps
except Exception:
    sys.stderr.write("Failed to import prettymaps. Please run: pip install -r requirements.txt\n")
    raise

OUTPUT_DIR = os.path.join(SCRIPT_DIR, 'output')
os.makedirs(OUTPUT_DIR, exist_ok=True)

PLACE_QUERY = 'Haking Wong Building, The University of Hong Kong, Hong Kong'
OUTPUT_PNG = os.path.join(OUTPUT_DIR, 'hku_haking_wong.png')


def main() -> None:
    plot = prettymaps.plot(
        PLACE_QUERY,
        radius=800,
        figsize=(12, 12),
        preset='minimal'
    )

    plot.fig.savefig(
        OUTPUT_PNG,
        dpi=200,
        bbox_inches='tight',
        facecolor=plot.fig.get_facecolor()
    )
    print(f"Saved map to: {OUTPUT_PNG}")


if __name__ == '__main__':
    main()
