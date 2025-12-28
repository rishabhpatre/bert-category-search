from pathlib import Path


RAW_FILE = Path("data/raw_categories.txt")
OUTPUT_FILE = Path("data/categories.py")


def generate_description(name: str) -> str:
    name_lower = name.lower()

    if "repair" in name_lower:
        return f"{name} related repair, servicing, maintenance and support services"
    if "dealer" in name_lower:
        return f"{name} related dealers, sellers and authorised distributors"
    if "doctor" in name_lower or "hospital" in name_lower:
        return f"{name} related medical consultation, treatment and healthcare services"
    if "restaurant" in name_lower or "hotel" in name_lower:
        return f"{name} related food, dining, stay and hospitality services"

    return f"{name} related services, providers and business offerings"


def build_categories():
    categories = []

    with open(RAW_FILE, "r", encoding="utf-8") as f:
        for idx, line in enumerate(f, start=1):
            name = line.strip()
            if not name:
                continue

            categories.append(
                {
                    "id": idx,
                    "name": name,
                    "description": generate_description(name)
                }
            )

    return categories


def write_categories_py(categories):
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("CATEGORIES = [\n")
        for cat in categories:
            f.write(f"    {cat},\n")
        f.write("]\n")


if __name__ == "__main__":
    categories = build_categories()
    write_categories_py(categories)
    print(f"Generated {len(categories)} categories")
