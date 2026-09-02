# PT03 · Criterio de evaluación de riesgos

**Taller:** SI-084 Semana 03 — Evaluación de riesgos con SimpleRisk y detección técnica con OpenVAS/Greenbone
**Elaborado por:** Angel Vargas Gutierrez — Código 2020066922
**Herramienta:** SimpleRisk (Configure → Risk Configuration → Classic Risk Formula)

## Fórmula

RIESGO = Probabilidad (Likelihood) x Impacto, normalizado a escala 0-10.

## Escala de Probabilidad (1-5)

| Nivel | Etiqueta | Definición operativa |
|---|---|---|
| 1 | Remota | Probabilidad de explotación menor al 10% en un año. No se han observado intentos ni existe exposición directa a redes no confiables. |
| 2 | Improbable | Probabilidad entre 10% y 30% en un año. Requiere condiciones específicas (acceso interno, cadena de varios pasos) para ser explotada. |
| 3 | Posible | Probabilidad entre 30% y 60% en un año. Vulnerabilidad conocida y publicada (CVE con exploit disponible), pero con algún control compensatorio parcial. |
| 4 | Probable | Probabilidad entre 60% y 90% en un año. Vulnerabilidad explotable de forma remota, sin autenticación, y el activo está expuesto a la red. |
| 5 | Casi certeza | Probabilidad mayor al 90% en un año. Exploit trivial o automatizado (scanners masivos), activo expuesto a Internet, sin ningún control compensatorio. |

## Escala de Impacto (1-5)

| Nivel | Etiqueta | Definición operativa |
|---|---|---|
| 1 | Insignificante | Sin pérdida de datos ni interrupción de servicio. Información pública. Costo de remediación menor a USD 1,000. |
| 2 | Menor | Afecta un único proceso o servicio, interrupción menor a 24 horas, sin exposición de datos clasificados como Confidencial o Restringida. |
| 3 | Moderado | Afecta un área funcional completa, interrupción de 1 a 3 días, o exposición de información Interna. |
| 4 | Mayor | Afecta múltiples áreas o procesos críticos, interrupción mayor a 3 días, o exposición de información Confidencial (p. ej. datos de clientes). |
| 5 | Catastrófico | Compromete la continuidad del negocio, exposición de información Restringida (p. ej. base de datos financiera/ERP), incumplimiento normativo o pérdida reputacional grave. |

## Criterio de aceptación

- **Riesgo ≤ 6** (sobre 10, normalizado): aceptable. Se documenta la aceptación y el dueño del riesgo la firma, sin plan de tratamiento obligatorio.
- **Riesgo > 6**: requiere plan de tratamiento con plazo definido, registrado en SimpleRisk (Plan Your Mitigations), y control mapeado al Anexo A de ISO/IEC 27001:2022.

Este umbral corresponde a la banda Media/Alta de la configuración por defecto de SimpleRisk
(Bajo ≥ 0.0, Medio ≥ 4.0, Alto ≥ 7.0, Muy Alto ≥ 10.1 sobre escala normalizada 0-10).

## Dueños de riesgo por área

| Área | Dueño (rol) | Activo(s) asociado(s) |
|---|---|---|
| Finanzas | Gerencia de Finanzas | si084_db (Base de datos ERP) |
| Comercial | Gerencia Comercial | si084_juiceshop (Portal de clientes), si084_portal (Portal corporativo) |
| Operaciones | Gerencia de Operaciones | si084_dvwa (App legada interna) |
| TI | Jefatura de TI | Infraestructura Docker / Greenbone / SimpleRisk |
