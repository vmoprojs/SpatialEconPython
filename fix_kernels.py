import nbformat
import os

nuevo_kernel = {
    "name": "geo_env",  # cambia aquí si deseas otro, como "python-geo-env"
    "display_name": "Python (geo_env)",  # este es el nombre visible
    "language": "python"
}

for fname in os.listdir():
    if fname.endswith(".ipynb"):
        with open(fname, "r", encoding="utf-8") as f:
            nb = nbformat.read(f, as_version=4)

        nb.metadata["kernelspec"] = nuevo_kernel

        with open(fname, "w", encoding="utf-8") as f:
            nbformat.write(nb, f)

print("✅ Kernels actualizados a 'geo_env'.")
