import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
links = json.loads((root / "scripts" / "video_links.json").read_text(encoding="utf-8"))

files = {
    "basic_arithmetic_and_equations/README.md": [
        "basic_arithmetic_and_equations/order_of_operations",
        "basic_arithmetic_and_equations/fractions",
        "basic_arithmetic_and_equations/exponents_and_radicals",
        "basic_arithmetic_and_equations/parentheses",
        "basic_arithmetic_and_equations/equations",
        "basic_arithmetic_and_equations/quadratic_equations",
        "basic_arithmetic_and_equations/rearranging_formulae",
    ],
    "functions/README.md": [
        "functions/functions_and_graphs",
        "functions/common_function_types",
        "functions/inverse_functions",
    ],
    "differential_calculus/README.md": [
        "differential_calculus/derivatives_and_tangents",
        "differential_calculus/differentiation_rules",
    ],
    "integral_calculus/README.md": [
        "integral_calculus/indefinite_integrals_and_antiderivatives",
        "integral_calculus/definite_integrals_and_areas",
    ],
    "vectors/README.md": [
        "vectors/vectors_in_2D",
        "vectors/dot_product",
        "vectors/parametric_equation_of_a_line",
    ],
}

for rel, keys in files.items():
    path = root / rel
    text = path.read_text(encoding="utf-8")
    for key in keys:
        url = links[key]["preview"]
        text = text.replace('src=""', f'src="{url}"', 1)
    path.write_text(text, encoding="utf-8")
    print(f"Updated {rel}")
