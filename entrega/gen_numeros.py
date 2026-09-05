import json
R = json.load(open("results.json"))
w, n = [], {"IMG-01": "One", "IMG-02": "Two", "IMG-03": "Three"}
for im in R["imagenes"]:
    s = n[im["id"]]
    lab = im["top1"].split(",")[0].replace("_", "\\_")
    w.append(f"\\newcommand{{\\img{s}TopUno}}{{{lab}}}")
    w.append(f"\\newcommand{{\\img{s}PTopUno}}{{{im['p_top1']:.3f}}}")
st = R["estabilidad_pearson"]
w.append(f"\\newcommand{{\\stabMin}}{{{min(st.values()):.3f}}}")
w.append(f"\\newcommand{{\\stabMax}}{{{max(st.values()):.3f}}}")
w.append("\\newcommand{\\cfgMaxEvals}{2000}")
open("paper/numeros.tex", "w").write("% generado por gen_numeros.py\n" + "\n".join(w) + "\n")
print(len(w), "macros")
