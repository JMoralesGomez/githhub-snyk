# Mini API Python con GitLab DevSecOps

Proyecto de referencia con FastAPI, pruebas, empaquetado, contenedor y un pipeline de seguridad de extremo a extremo.

## Funcionalidad

- `GET /health`: estado del servicio.
- `GET /api/v1/sum?a=2&b=3`: suma dos números.

## Desarrollo local

```bash
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
pip install -e ".[dev]"
uvicorn mini_api.main:app --reload
```

Pruebas y controles locales:

```bash
ruff check .
ruff format --check .
mypy src
pytest
bandit -r src
pip-audit
```

## Pipeline

Las etapas son:

1. `validate`: formato, lint y tipos.
2. `test`: pruebas y cobertura.
3. `security`: SAST, dependencias, secretos y sistema de archivos.
4. `build`: paquete Python e imagen OCI.
5. `container_scan`: vulnerabilidades de la imagen.
6. `publish`: publicación de la imagen en GitLab Container Registry.
7. `deploy`: despliegue manual y controlado.
8. `verify`: comprobación posterior al despliegue.

El registro de contenedores debe estar habilitado. Los jobs de imagen requieren un runner capaz de usar Docker-in-Docker.

Para habilitar el despliegue, configure las variables protegidas:

- `DEPLOY_HOST`: servidor de destino.
- `DEPLOY_URL`: URL pública del servicio, por ejemplo `https://api.example.com`.
- `DEPLOY_USER`: usuario SSH.
- `DEPLOY_SSH_PRIVATE_KEY`: llave privada SSH de despliegue.
- `SSH_KNOWN_HOSTS`: huella SSH verificada del servidor, obtenida por un canal confiable.

El servidor debe tener Docker instalado. El despliegue de producción solo aparece para tags con formato `vX.Y.Z` y requiere aprobación manual.

## Inicio rápido en GitLab

```bash
git init
git add .
git commit -m "feat: proyecto Python con pipeline DevSecOps"
git branch -M main
git remote add origin <URL_DEL_REPOSITORIO_GITLAB>
git push -u origin main
```

## Criterio de seguridad

Los análisis fallan ante hallazgos relevantes. El despliegue no guarda secretos en el repositorio, utiliza una imagen inmutable identificada por tag y se ejecuta manualmente desde una rama o tag protegido.
