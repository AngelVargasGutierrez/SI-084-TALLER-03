import pandas as pd

# --- EVIDENCIA TECNICA ---
v = pd.read_csv("../20_evidencia/E03_scan/reporte_greenbone.csv")

# NOTA METODOLOGICA: las imagenes base usadas en si084-lab estan relativamente
# actualizadas, por lo que un filtro CVSS >= 4.0 (como en la version original
# de este script) deja un unico hallazgo (EOL de SO). Se amplia el criterio de
# inclusion a todo hallazgo con relevancia de seguridad, descartando solo las
# pruebas de inventario/huella digital sin relevancia (CPE, hostname, banners,
# traceroute, enumeracion de servicios, chequeos SSH que fallan por no existir
# servidor SSH, etc.). Esta decision se documenta en el informe (Paso D).
NVT_SIN_RELEVANCIA = {
    "CPE Inventory", "Hostname Determination Reporting",
    "OS Detection Consolidation and Reporting", "Traceroute", "Services",
    "SSH Login Failed For Authenticated Checks", "SSH Authorization Check",
    "IP Forwarding Enabled - Active Check", "Apache HTTP Server Detection Consolidation",
    "nginx Detection Consolidation", "HTTP Server Banner Enumeration",
    "HTTP Server type and version", "MariaDB / Oracle MySQL Detection (MySQL Protocol)",
    "Response Time / No 404 Error Code Check",
    "robot.txt / robots.txt exists on the Web Server (HTTP)",
    "security.txt Detection (HTTP)",
    "Web Application Scanning Consolidation / Info Reporting",
}
v = v[~v["NVT Name"].isin(NVT_SIN_RELEVANCIA)]

# --- CONTEXTO DE NEGOCIO: sin esto, el CVSS no significa nada ---
ACTIVOS = {
    "172.18.0.5": dict(nombre="Base de datos ERP (si084_db)",  dueno="Gerencia de Finanzas",
                        clasificacion="Restringida", expuesto=False, criticidad=5),
    "172.18.0.3": dict(nombre="Portal de clientes (si084_juiceshop)", dueno="Gerencia Comercial",
                        clasificacion="Confidencial", expuesto=True,  criticidad=4),
    "172.18.0.4": dict(nombre="Portal corporativo (si084_portal)", dueno="Gerencia Comercial",
                        clasificacion="Publica",     expuesto=True,  criticidad=2),
    "172.18.0.2": dict(nombre="App legada interna (si084_dvwa)", dueno="Gerencia de Operaciones",
                        clasificacion="Interna",     expuesto=False, criticidad=3),
}

def probabilidad(cvss, expuesto):
    """La exposicion a Internet eleva la probabilidad de explotacion."""
    base = 1 if cvss < 4 else 2 if cvss < 7 else 3 if cvss < 9 else 4
    return min(5, base + (1 if expuesto else 0))

def impacto(criticidad, clasificacion):
    """El impacto lo determina el valor del activo, no la severidad tecnica."""
    extra = {"Restringida": 1, "Confidencial": 0, "Interna": 0, "Publica": -1}
    return max(1, min(5, criticidad + extra.get(clasificacion, 0)))

filas = []
for _, r in v.iterrows():
    a = ACTIVOS.get(str(r["IP"]).strip(), None)
    if not a:
        continue
    cvss = float(r["CVSS"]) if str(r["CVSS"]).strip() not in ("", "nan") else 0.0
    p = probabilidad(cvss, a["expuesto"])
    i = impacto(a["criticidad"], a["clasificacion"])
    filas.append({
        "id_riesgo": f"R-{len(filas)+1:03d}",
        "activo": a["nombre"], "dueno_del_riesgo": a["dueno"],
        "clasificacion": a["clasificacion"],
        "amenaza": "Explotacion remota de vulnerabilidad o exposicion de informacion",
        "vulnerabilidad": r["NVT Name"], "cve": r.get("CVEs") or "N/D",
        "cvss": cvss, "probabilidad": p, "impacto": i,
        "riesgo_inherente": p * i,
        "nivel": "Critico" if p*i >= 20 else "Alto" if p*i >= 12
                 else "Medio" if p*i >= 6 else "Bajo",
    })

reg = pd.DataFrame(filas).sort_values("riesgo_inherente", ascending=False)
reg.to_csv("../40_hallazgos/PT03_registro_riesgos.csv", index=False)
print(reg.to_string(index=False))
print("\nDistribucion por nivel:\n", reg["nivel"].value_counts().to_string())
