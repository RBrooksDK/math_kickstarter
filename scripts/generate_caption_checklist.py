"""Generate caption upload checklist for all Math Kickstarter videos."""
import json
from pathlib import Path

ROOT = Path(r"G:\Mit drev\Video\Math_kickstarter")
REPO = Path(__file__).resolve().parents[1]
links = json.loads((REPO / "scripts" / "video_links.json").read_text(encoding="utf-8"))

# Map topic/subfolder to english and danish srt filenames (from Drive sync)
CAPTIONS = {
    "basic_arithmetic_and_equations/order_of_operations": (
        "english_order_of_opertations.srt",
        "dansk_regnearternes_hierarki.srt",
    ),
    "basic_arithmetic_and_equations/fractions": (
        "english_fractions.srt",
        "dansk_brøker.srt",
    ),
    "basic_arithmetic_and_equations/exponents_and_radicals": (
        "english_exponents_and_radicals.srt",
        "dansk_eksponenter_og_rødder.srt",
    ),
    "basic_arithmetic_and_equations/parentheses": (
        "english_parentheses.srt",
        "dansk_parenteser.srt",
    ),
    "basic_arithmetic_and_equations/equations": (
        "english_equations.srt",
        "dansk_ligninger.srt",
    ),
    "basic_arithmetic_and_equations/quadratic_equations": (
        "english_quadratic_equations.srt",
        "dansk_andengradsligninger.srt",
    ),
    "basic_arithmetic_and_equations/rearranging_formulae": (
        "english_rearranging_formulae.srt",
        "dansk_omskrivning_af_formler.srt",
    ),
    "functions/functions_and_graphs": (
        "english_functions_and_graphs.srt",
        "dansk_funktioner_og_grafer.srt",
    ),
    "functions/common_function_types": (
        "english_common_function_types.srt",
        "dansk_almindelige_funktionstyper.srt",
    ),
    "functions/inverse_functions": (
        "english_inverse_functions.srt",
        "dansk_inverse_funktioner.srt",
    ),
    "differential_calculus/derivatives_and_tangents": (
        "english_derivatives_and_tangents.srt",
        "dansk_afledte_og_tangenter.srt",
    ),
    "differential_calculus/differentiation_rules": (
        "english_differentiation_rules.srt",
        "dansk_differential_regneregler.srt",
    ),
    "integral_calculus/indefinite_integrals_and_antiderivatives": (
        "english_indefinite_integrals_and_antiderivatives.srt",
        "dansk_ubestemte_integraler_og_stamfunktioner.srt",
    ),
    "integral_calculus/definite_integrals_and_areas": (
        "english_definite_integrals_and_areas.srt",
        "dansk_bestemte_integraler_og_arealer.srt",
    ),
    "vectors/vectors_in_2D": (
        "english_vectors_in_2d.srt",
        "dansk_vektorer_i_2d.srt",
    ),
    "vectors/dot_product": (
        "english_dot_product.srt",
        "dansk_prikproduktet.srt",
    ),
    "vectors/parametric_equation_of_a_line": (
        "english_parametric_equation_of_a_line.srt",
        "dansk_parameterfremstilling_for_en_linje.srt",
    ),
}


def find_srt(folder: Path, name: str) -> Path | None:
    """Find SRT by exact or case-insensitive match."""
    if (folder / name).exists():
        return folder / name
    lower = name.lower()
    for f in folder.glob("*.srt"):
        if f.name.lower() == lower:
            return f
    # fuzzy: match without special chars
    for f in folder.glob("*.srt"):
        if lower.replace("ø", "?") in f.name.lower() or f.stem.lower().startswith(lower.split("_")[0]):
            pass
    for f in folder.glob("*.srt"):
        if "english" in lower and f.name.lower().startswith("english"):
            if name.split("_", 1)[-1].replace("opertations", "operations") in f.name.lower().replace("opertations", "operations"):
                return f
        if "dansk" in lower and f.name.lower().startswith("dansk"):
            return f
    return None


def resolve_srt(topic_path: str, filename: str) -> str:
    folder = ROOT / topic_path.replace("/", "\\")
    if not folder.exists():
        return f"MISSING FOLDER: {folder}"
    # list dir and match
    target = filename.lower()
    for f in folder.glob("*.srt"):
        if f.name.lower() == target:
            return str(f)
    # partial match for encoding issues (ø vs)
    for f in folder.glob("*.srt"):
        if filename.startswith("english") and f.name.lower().startswith("english"):
            return str(f)
        if filename.startswith("dansk") and f.name.lower().startswith("dansk"):
            if "br" in target and "br" in f.name.lower():
                return str(f)
            if "eksponenter" in target and "eksponenter" in f.name.lower():
                return str(f)
            if "regnearternes" in target and "regnearternes" in f.name.lower():
                return str(f)
            if "ligninger" in target and "ligninger" in f.name.lower() and "andengrad" not in f.name.lower() and "andengrad" not in target:
                return str(f)
            if "andengrad" in target and "andengrad" in f.name.lower():
                return str(f)
            if "parenteser" in target and "parenteser" in f.name.lower():
                return str(f)
            if "omskrivning" in target and "omskrivning" in f.name.lower():
                return str(f)
            if "funktioner_og_grafer" in target and "funktioner" in f.name.lower() and "grafer" in f.name.lower():
                return str(f)
            if "almindelige" in target and "almindelige" in f.name.lower():
                return str(f)
            if "inverse" in target and "inverse" in f.name.lower():
                return str(f)
            if "afledte" in target and "afledte" in f.name.lower():
                return str(f)
            if "differential_regneregler" in target and "differential" in f.name.lower():
                return str(f)
            if "ubestemte" in target and "ubestemte" in f.name.lower():
                return str(f)
            if "bestemte" in target and "bestemte" in f.name.lower():
                return str(f)
            if "vektorer" in target and "vektorer" in f.name.lower():
                return str(f)
            if "prikprodukt" in target and "prikprodukt" in f.name.lower():
                return str(f)
            if "parameter" in target and "parameter" in f.name.lower():
                return str(f)
    return f"NOT FOUND (expected {folder / filename})"


def main():
    rows = []
    for key, (en, da) in CAPTIONS.items():
        info = links[key]
        fid = info["file_id"]
        rows.append({
            "video": info["filename"],
            "topic": key,
            "captions_edit": f"https://drive.google.com/u/0/video/captions/edit?id={fid}",
            "english_srt": resolve_srt(key, en),
            "danish_srt": resolve_srt(key, da),
        })

    out_json = REPO / "scripts" / "caption_upload_checklist.json"
    out_json.write_text(json.dumps(rows, indent=2, ensure_ascii=False), encoding="utf-8")

    lines = [
        "# Caption upload checklist",
        "",
        "Upload **two** caption tracks per video (English + Danish).",
        "",
        "For each video:",
        "1. Open the **Add captions** link below (opens the caption editor directly)",
        "2. Click **Add new caption track** → upload SRT → set language → Upload",
        "3. Repeat for the second language (English, then Danish)",
        "",
        "Total: **17 videos × 2 languages = 34 caption uploads**",
        "",
        "---",
        "",
    ]
    for i, r in enumerate(rows, 1):
        lines += [
            f"## {i}. {r['video']}",
            "",
            f"- **Topic:** `{r['topic']}`",
            f"- **Add captions:** [{r['captions_edit']}]({r['captions_edit']})",
            f"- **English SRT:** `{r['english_srt']}` → language: **English**",
            f"- **Danish SRT:** `{r['danish_srt']}` → language: **Danish**",
            "",
        ]

    out_md = REPO / "scripts" / "caption_upload_checklist.md"
    out_md.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {out_json}")
    print(f"Wrote {out_md}")
    for r in rows:
        if "NOT FOUND" in r["english_srt"] or "NOT FOUND" in r["danish_srt"]:
            print("WARN:", r["video"])


if __name__ == "__main__":
    main()
