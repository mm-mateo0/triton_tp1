
# Proyecto Tritón
## TP-1: Sistema de Telemetría Multicloud y Observabilidad Asíncrona

**Integrante:** Mateo Liendro  
**Institución:** UPATECO  
**Proyecto:** Tritón

## 1. Objetivo

Desarrollar una aplicación educativa para recibir eventos de telemetría, procesarlos de forma asíncrona y consultar métricas básicas de funcionamiento.

## 2. Tecnologías

- Python
- FastAPI
- Uvicorn
- API REST
- Logging para registrar eventos

## 3. Funcionamiento

La aplicación propone tres endpoints:

- `GET /health`: verifica el estado del servicio.
- `GET /metrics`: consulta las métricas acumuladas.
- `POST /telemetry`: recibe un evento de telemetría en formato JSON.

## 4. Ejemplo de evento

```json
{
  "provider": "aws",
  "service": "api",
  "event": "request_completed",
  "value": 1
}
```

## 5. Ejecución prevista

Instalar las dependencias indicadas en `requirements.txt` y ejecutar la aplicación con Uvicorn. La documentación interactiva de FastAPI se puede consultar en `/docs`.

## 6. Alcance

Esta documentación describe el diseño previsto de una demostración local. Las integraciones reales con proveedores cloud y las pruebas de funcionamiento deben implementarse y verificarse antes de considerarse completas.

## 7. Repositorio

https://github.com/mm-mateo0/triton_tp1
