# Evaluación 2 - Pipeline CI/CD Seguro y DevSecOps (DOY0101)

## Información del Proyecto
- **Asignatura:** DevOps Engineering (DOY0101)
- **Integrantes:*Ignacio Pilar Marcos Necul*
  - Ignacio Bastián Pilar Garrido -  - Sección: [801D]
- **Docente:** Guillermo Torres

---

## 1. Arquitectura y Stack Tecnológico
Microservicio REST desarrollado en **FastAPI** respaldado por una base de datos relacional **PostgreSQL**, orquestado mediante contenedores Docker.

- **Stack:** Python 3.11, FastAPI, PostgreSQL, Docker Compose, PyTest, Aquasec Trivy, GitHub Actions.
- **Endpoints:**
  - `GET /`: Endpoint raíz con estado de bienvenida.
  - `GET /health`: Endpoint de verificación de salud (*health check*) para pruebas de humo en despliegue.

### Ejecución Local
```bash
# Clonar repositorio
git clone [https://github.com/Nacho546/evaluacion-2-devops.git](https://github.com/Nacho546/evaluacion-2-devops.git)
cd evaluacion-2-devops

# Levantar infraestructura
docker compose up -d --build

# Verificar salud
curl http://localhost:8000/health
