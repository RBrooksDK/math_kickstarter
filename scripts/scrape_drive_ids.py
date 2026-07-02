"""Scrape public Google Drive folder pages for mp4 file IDs."""
import json
import re
import urllib.request
from html import unescape

LEAVES = {
    # basic_arithmetic_and_equations
    "basic_arithmetic_and_equations/order_of_operations": "1QIWGH20jRXpYjICCl4_ptyLCJvkOPxPZ",
    "basic_arithmetic_and_equations/fractions": "1kWwaa1NWcGjlI7Kh_QmnS0RW0Y0Elbyu",
    "basic_arithmetic_and_equations/exponents_and_radicals": "16r5R5BIgsDtKb8ZB6Iru8SzUtkV2oMlr",
    "basic_arithmetic_and_equations/parentheses": "1ImqZsrnUaFMIK1lZPgqkQIrrtEEACsiW",
    "basic_arithmetic_and_equations/equations": "1bwoJO6vHDl8Qcs-CSQ5sLg2IcfpwbFh0",
    "basic_arithmetic_and_equations/quadratic_equations": "1YcXb0hHb-gBcQNCjru8iU3lCeoJMt4qc",
    "basic_arithmetic_and_equations/rearranging_formulae": "16zn3jQliYYrVJNItQZyyPmxLp3n4Cin8",
    # functions
    "functions/functions_and_graphs": "1i-gj3Mj7Oxukd4--1Ymogj4medKYpQUf",
    "functions/common_function_types": "1nSp_LPb9UrBNm-35C7bbFvFh3Znuw2SB",
    "functions/inverse_functions": "1OnO35D0qkFvrXnitJbzH--Fl9_ahMvEH",
    # differential_calculus
    "differential_calculus/derivatives_and_tangents": "12ZxMDW3GDFKxcXMN4dnGlgxg6LOrfHRO",
    "differential_calculus/differentiation_rules": "1_n8RZVJp7RI80xK-PcJTLnzCrGr_mCfn",
    # integral_calculus
    "integral_calculus/indefinite_integrals_and_antiderivatives": "1v97woqyfpWmqqI-xDoH7j0YL-hBoEQvs",
    "integral_calculus/definite_integrals_and_areas": "1ssvPHpWogqAhhoq9OuvDIfB4brp6wn8I",
    # vectors
    "vectors/vectors_in_2D": "1czhoNVock4EAi_FOC-_e3nCH3lCgduvM",
    "vectors/dot_product": "1U9hqe8qcWP5kZHlF9Lmkeox5MUavnIEm",
    "vectors/parametric_equation_of_a_line": "1aazm5zMwcOsNELbKwlNiCEia7_ZA4SGp",
}


def fetch_html(folder_id: str) -> str:
    url = f"https://drive.google.com/drive/folders/{folder_id}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", errors="ignore")


def parse_rows(html: str) -> list[dict]:
    items = []
    for tr in re.finditer(
        r'<tr[^>]*data-id="(1[a-zA-Z0-9_-]{20,44})"[^>]*>(.*?)</tr>',
        html,
        re.DOTALL | re.IGNORECASE,
    ):
        fid = tr.group(1)
        text = re.sub(r"<[^>]+>", " ", tr.group(2))
        text = unescape(re.sub(r"\s+", " ", text)).strip()
        name = text.split("Ejeren er skjult")[0].strip()
        name = re.sub(r"^(Video|PDF|Komprimeret arkiv)\s*", "", name)
        name = re.sub(r"\s*(Download|Delt).*$", "", name).strip()
        items.append({"id": fid, "name": name})
    return items


def find_mp4(folder_id: str) -> dict | None:
    for item in parse_rows(fetch_html(folder_id)):
        if item["name"].lower().endswith(".mp4"):
            return {
                "file_id": item["id"],
                "filename": item["name"],
                "preview": f"https://drive.google.com/file/d/{item['id']}/preview",
            }
    return None


if __name__ == "__main__":
    out = {}
    for path, folder_id in LEAVES.items():
        out[path] = find_mp4(folder_id)
        print(f"{path}: {out[path]['preview'] if out[path] else 'NOT FOUND'}")
    with open("video_links.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    print("Wrote video_links.json")
