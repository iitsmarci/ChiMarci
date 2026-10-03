import urllib.request
import json
import math

url = "https://raw.githubusercontent.com/Bowserinator/Periodic-Table-JSON/master/PeriodicTableJSON.json"
response = urllib.request.urlopen(url)
data = json.loads(response.read())

italian_names = {
    1: "Idrogeno", 2: "Elio", 3: "Litio", 4: "Berillio", 5: "Boro", 6: "Carbonio", 7: "Azoto", 8: "Ossigeno", 9: "Fluoro", 10: "Neon",
    11: "Sodio", 12: "Magnesio", 13: "Alluminio", 14: "Silicio", 15: "Fosforo", 16: "Zolfo", 17: "Cloro", 18: "Argo",
    19: "Potassio", 20: "Calcio", 21: "Scandio", 22: "Titanio", 23: "Vanadio", 24: "Cromo", 25: "Manganese", 26: "Ferro", 27: "Cobalto", 28: "Nichel", 29: "Rame", 30: "Zinco", 31: "Gallio", 32: "Germanio", 33: "Arsenico", 34: "Selenio", 35: "Bromo", 36: "Kripton",
    37: "Rubidio", 38: "Stronzio", 39: "Ittrio", 40: "Zirconio", 41: "Niobio", 42: "Molibdeno", 43: "Tecnezio", 44: "Rutenio", 45: "Rodio", 46: "Palladio", 47: "Argento", 48: "Cadmio", 49: "Indio", 50: "Stagno", 51: "Antimonio", 52: "Tellurio", 53: "Iodio", 54: "Xeno",
    55: "Cesio", 56: "Bario", 57: "Lantanio", 58: "Cerio", 59: "Praseodimio", 60: "Neodimio", 61: "Promezio", 62: "Samario", 63: "Europio", 64: "Gadolinio", 65: "Terbio", 66: "Disprosio", 67: "Olmio", 68: "Erbio", 69: "Tulio", 70: "Itterbio", 71: "Lutezio",
    72: "Afnio", 73: "Tantalio", 74: "Tungsteno", 75: "Renio", 76: "Osmio", 77: "Iridio", 78: "Platino", 79: "Oro", 80: "Mercurio", 81: "Tallio", 82: "Piombo", 83: "Bismuto", 84: "Polonio", 85: "Astato", 86: "Radon",
    87: "Francio", 88: "Radio", 89: "Attinio", 90: "Torio", 91: "Protoattinio", 92: "Uranio", 93: "Nettunio", 94: "Plutonio", 95: "Americio", 96: "Curio", 97: "Berkelio", 98: "Californio", 99: "Einsteinio", 100: "Fermio", 101: "Mendelevio", 102: "Nobelio", 103: "Laurenzio",
    104: "Rutherfordio", 105: "Dubnio", 106: "Seaborgio", 107: "Bohrio", 108: "Hassio", 109: "Meitnerio", 110: "Darmstadtio", 111: "Roentgenio", 112: "Copernicio", 113: "Nihonio", 114: "Flerovio", 115: "Moscovio", 116: "Livermorio", 117: "Tennesso", 118: "Oganesson"
}

group_map = {
    "alkali metal": "alkali",
    "alkaline earth metal": "alkaline-earth",
    "transition metal": "transition",
    "post-transition metal": "post-transition",
    "metalloid": "metalloid",
    "polyatomic nonmetal": "non-metal",
    "diatomic nonmetal": "non-metal",
    "noble gas": "noble",
    "lanthanide": "lanthanide",
    "actinide": "actinide",
    "unknown, probably transition metal": "transition",
    "unknown, probably post-transition metal": "post-transition",
    "unknown, probably metalloid": "metalloid",
    "unknown, predicted to be noble gas": "noble"
}

out = []
out.append('export type ElementData = {')
out.append('  n: number;')
out.append('  sym: string;')
out.append('  name: string;')
out.append('  mass: string;')
out.append('  group: string;')
out.append('  r: number;')
out.append('  c: number;')
out.append('  ox?: string;')
out.append('  elneg?: string;')
out.append('  conf?: string;')
out.append('};')
out.append('')
out.append('export const elements: ElementData[] = [')

for el in data["elements"][:118]:
    n = el["number"]
    sym = el["symbol"]
    name = italian_names.get(n, el["name"])
    
    mass_val = el["atomic_mass"]
    if n in [43, 61, 84, 85, 86, 87, 88, 89] or n >= 93:
        mass = f"({round(mass_val)})"
    else:
        mass = f"{mass_val:.3f}".rstrip('0').rstrip('.')
        
    category = el.get("category", "")
    group = "transition" # fallback
    for k, v in group_map.items():
        if k in category:
            group = v
            break
            
    if n == 1:
        group = "non-metal"
        
    r = el["period"]
    c = el["xpos"]
    
    # f-block adjustment for visual table if needed? The original array had:
    # La: r=6, c=3, but in reality 57-71 are f-block.
    # Actually, in the original UI, the f-block wasn't displayed correctly, it was just missing! 
    # Let's map lanthanides to r=8 and actinides to r=9, and columns 4 to 18 to render them at the bottom.
    if group == "lanthanide":
        r = 9
        c = n - 57 + 4
    elif group == "actinide":
        r = 10
        c = n - 89 + 4
        
    ox = el.get("oxidation_states")
    if ox:
        if isinstance(ox, list):
            ox_str = ", ".join(map(str, ox))
        else:
            ox_str = str(ox)
    else:
        ox_str = "N/D"
        
    elneg = el.get("electronegativity_pauling")
    elneg_str = f"{elneg:.2f}" if elneg else "N/D"
    
    conf = el.get("electron_configuration_semantic", "N/D")
    
    if n >= 104:
        ox_str = "N/D"
        elneg_str = "N/D"
        conf = "N/D"

    out.append(f'  {{ n: {n}, sym: "{sym}", name: "{name}", mass: "{mass}", group: "{group}", r: {r}, c: {c}, ox: "{ox_str}", elneg: "{elneg_str}", conf: "{conf}" }},')

out.append('];')

with open("src/data/periodicTable.ts", "w", encoding="utf-8") as f:
    f.write("\n".join(out))
