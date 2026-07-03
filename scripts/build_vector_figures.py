"""Build tutorial figures from LaTeX/TikZ sources (requires MiKTeX pdflatex)."""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEX_DIR = ROOT / "figures" / "tex"
PDFLATEX = shutil.which("pdflatex") or (
    Path.home() / "AppData/Local/Programs/MiKTeX/miktex/bin/x64/pdflatex.exe"
)

FIGURES = [
    ("vector_a_minus1_3.tex", "vector_a_minus1_3.png"),
    ("function_sqrt_2x.tex", "function_sqrt_2x.png"),
]


def compile_tex(tex_file: Path) -> Path:
    if not PDFLATEX or not Path(PDFLATEX).exists():
        raise RuntimeError("pdflatex not found. Install MiKTeX or TeX Live.")

    result = subprocess.run(
        [
            str(PDFLATEX),
            "-interaction=nonstopmode",
            "-halt-on-error",
            tex_file.name,
        ],
        cwd=tex_file.parent,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(result.stdout, file=sys.stderr)
        print(result.stderr, file=sys.stderr)
        raise RuntimeError(f"pdflatex failed for {tex_file.name}")

    return tex_file.with_suffix(".pdf")


def pdf_to_png(pdf_file: Path, png_file: Path, zoom: float = 4.0) -> None:
    try:
        import fitz  # pymupdf
    except ImportError as exc:
        raise RuntimeError(
            f"pymupdf is not installed for {sys.executable}\n"
            f"Run: {sys.executable} -m pip install pymupdf"
        ) from exc

    doc = fitz.open(pdf_file)
    page = doc[0]
    pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), alpha=False)
    png_file.parent.mkdir(parents=True, exist_ok=True)
    pix.save(png_file)
    doc.close()


def build_figure(tex_name: str, png_name: str) -> None:
    tex = TEX_DIR / tex_name
    pdf = tex.with_suffix(".pdf")
    png = ROOT / "figures" / png_name

    compile_tex(tex)
    pdf_to_png(pdf, png)
    print(f"Wrote {png}")


def build_all() -> None:
    for tex_name, png_name in FIGURES:
        build_figure(tex_name, png_name)


if __name__ == "__main__":
    build_all()
