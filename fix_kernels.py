import json
from pathlib import Path

notebooks = Path(".").rglob("*.ipynb")

for nb in notebooks:
    with open(nb, "r", encoding="utf-8") as f:
        data = json.load(f)

    if "kernelspec" in data.get("metadata", {}):
        data["metadata"]["kernelspec"]["name"] = "geo_env"
        data["metadata"]["kernelspec"]["display_name"] = "Python (geo_env)"

        with open(nb, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=1)
        print(f"✔ Kernel actualizado en: {nb}")
