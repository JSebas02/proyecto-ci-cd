# Reporte del Pipeline CI/CD

## Información del proyecto

- Lenguaje: Python 3.12
- Framework: Flask
- Herramienta de pruebas: Pytest
- Cobertura: Pytest-Cov
- Análisis estático: Flake8
- CI/CD: GitHub Actions

---

# Diagrama del Pipeline

```mermaid
flowchart LR
A[Push a GitHub] --> B[GitHub Actions]
B --> C[Instalar dependencias]
C --> D[Flake8]
D --> E[Pruebas]
E --> F[Cobertura]
F --> G[Resultado]
```

---

# Métricas de calidad

- Total de pruebas: **18**
- Pruebas unitarias: **12**
- Pruebas de integración: **6**
- Cobertura total: **95%**
- Cobertura de services.py: **100%**
- Cobertura de app.py: **89%**

---

# Complejidad

El proyecto presenta una complejidad baja debido a que la lógica de negocio está separada de la capa de presentación y cada función realiza una única responsabilidad.

---

# Issues encontrados

Durante el desarrollo se presentaron los siguientes inconvenientes:

- Error al activar el entorno virtual en PowerShell debido a la política de ejecución.
- Error de importación de la carpeta `src` solucionado mediante el archivo `pytest.ini`.
- Verificación correcta de la API REST mediante pruebas manuales y automatizadas.

---

# Justificación del umbral

Se estableció una cobertura mínima superior al 80% para garantizar que la mayor parte del código esté validada mediante pruebas automáticas.

La cobertura final obtenida fue del **95%**, superando ampliamente el requisito solicitado.

---

# Conclusiones

La implementación del pipeline CI/CD permite automatizar la ejecución de pruebas, verificar la calidad del código mediante Flake8 y generar reportes de cobertura en cada actualización del repositorio.

Esto facilita detectar errores tempranamente y mantener la estabilidad del proyecto.