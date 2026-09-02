# PT03 · Extracto de la Declaración de Aplicabilidad (SoA)

**Taller:** SI-084 Semana 03 · **Elaborado por:** Angel Vargas Gutierrez — Código 2020066922
**Alcance:** controles de ISO/IEC 27001:2022 Anexo A relacionados con los riesgos R-001, R-006, R-007, R-011 y R-012
del registro `40_hallazgos/PT03_registro_riesgos.csv`, cargados en SimpleRisk como IDs 1001-1005.

| Control | Título | ¿Aplica? | Justificación | Estado | Riesgo que trata |
|---|---|---|---|---|---|
| A.8.8 | Management of technical vulnerabilities | Sí | Se detectó un sistema operativo fuera de soporte (EOL) en el contenedor si084_dvwa, con CVSS 10.0 sobre una vulnerabilidad conocida y no parcheable dentro de ese ciclo de vida. | No implementado | R-011 (ID 1001) |
| A.8.9 | Configuration management | Sí | El portal de clientes (si084_juiceshop) no aplica una configuración base seguridad-por-defecto: faltan cabeceras HTTP de seguridad y permite métodos HTTP innecesarios. | No implementado | R-006, R-001 (ID 1002, 1003) |
| A.8.16 | Monitoring activities | Sí | La divulgación de información por TCP/ICMP Timestamps solo se detectó mediante escaneo activo; no existe monitoreo que hubiera alertado sobre esta exposición de reconocimiento. | Parcial (cubierto por el propio ejercicio de escaneo periódico) | R-012, R-007 (ID 1004, 1005) |
| A.5.17 | Authentication information | Sí | La base de datos ERP (si084_db) usa credenciales de laboratorio simples (root/contraseña estática); en un entorno productivo requeriría rotación y gestión de secretos. | No implementado | Contexto de si084_db (activo de mayor criticidad, sin hallazgo explotable en este ciclo) |
| A.8.24 | Use of cryptography | Sí | El tráfico entre los contenedores objetivo y sus clientes no fuerza TLS (Juice Shop, portal y DVWA sirven por HTTP plano); MySQL sí ofrece TLS opcional (detectado por nmap) pero no es obligatorio. | No implementado | Contexto general de exposición de si084_juiceshop y si084_portal |
| A.7.4 | Physical security monitoring | No | El entorno completo (si084-lab) es virtualizado dentro de contenedores Docker sobre un laptop de laboratorio; no existe infraestructura física propia que auditar bajo este control. | N/A | — |

## Riesgo residual y aceptación

- **R-011 (1001)** — tratamiento: Mitigar (actualizar/migrar la imagen base). Hasta su implementación, el riesgo residual permanece igual al inherente (4.8, Medio). Corresponde firmar la aceptación temporal a la **Gerencia de Operaciones**, dueña del activo.
- **R-006 / R-001 (1002, 1003)** — tratamiento: Mitigar (cabeceras y métodos HTTP vía proxy inverso). Firma de aceptación temporal: **Gerencia Comercial**.
- **R-012 / R-007 (1004, 1005)** — tratamiento: Aceptar, dentro del criterio de aceptación definido en `PT03_criterio_evaluacion.md` (valor normalizado 3.2 ≤ 6). Firma de aceptación: **Gerencia Comercial**, sin plazo de tratamiento obligatorio.
