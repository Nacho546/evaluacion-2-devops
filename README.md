# evaluacion-2-devops
# Evaluación 2 - Implementación de Pipeline CI/CD Seguro

## 1. Arquitectura del Proyecto
Microservicio desarrollado en **FastAPI** junto a una base de datos relacional **PostgreSQL**, orquestados mediante **Docker Compose**.

- **Endpoints principales**:
  - `GET /`: Mensaje de bienvenida del servicio.
  - `GET /health`: Endpoint de monitoreo y health check del sistema.

## 2. Pipeline de CI/CD (GitHub Actions)
El flujo automatizado se ejecuta en cada `push` y `pull_request` sobre la rama `main` y consta de tres fases secuenciales:

1. **Pruebas Unitarias (`unit-tests`)**:
   - Entorno: Ubuntu Runner con Python 3.11.
   - Herramienta: PyTest y HTTPX TestClient para validar respuestas de los endpoints.

2. **Escaneo de Seguridad y Vulnerabilidades (`security-scan`)**:
   - Herramienta: **Aquasec Trivy**.
   - Objetivo: Detección estática de vulnerabilidades (SAST/SCA) en la imagen Docker base y dependencias de sistema operativo con severidad crítica (`CRITICAL`).

3. **Despliegue en Entorno Simulado (`deploy-simulated`)**:
   - Registro de metadata del commit (SHA, rama, autor) para trazabilidad.
   - Despliegue de contenedores usando `docker compose up -d --build`.
   - Smoke test automatizado consultando el endpoint `/health` mediante `curl`.
   - Limpieza automática de recursos (`docker compose down -v`).

## 3. Gestión Continua de Dependencias
- Configuración de **Dependabot** (`.github/dependabot.yml`) para monitoreo semanal automatizado de vulnerabilidades y actualizaciones en dependencias `pip` y contenedores `docker`.
