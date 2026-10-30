# Contexto IA · Erick Quio

**Preparación de contexto para flujos de agentes.** Fork de
[Langflow](https://github.com/langflow-ai/langflow), conservando su licencia MIT.
El aporte local es una utilidad de texto y un adaptador de componente experimental.
No representa una contribución aceptada por upstream.

## Qué resuelve

`erick_context.py` normaliza Unicode a NFC, compacta espacios dentro de cada línea,
elimina líneas vacías y aplica un presupuesto de caracteres. Devuelve texto y metadatos:
longitudes de entrada, normalizada y final, y un indicador de truncamiento.

```mermaid
flowchart LR
    A[Texto de entrada] --> B[Unicode NFC]
    B --> C[Normalizar espacios]
    C --> D[Presupuesto de caracteres]
    D --> E[Contexto y metadatos]
```

## Probar sin instalar Langflow

Python 3.10 o posterior:

```bash
uv run --no-project python erick_context.py erick_sample.txt --max-chars 120
uv run --no-project --with pytest python -m pytest test_erick_context.py -q
```

La utilidad no llama modelos ni APIs. **Caracteres no equivale a tokens**.
El recorte es por punto de código Unicode y puede cortar una frase; no es un resumidor.
La normalización está pensada para prosa, no para código o tablas cuya indentación importe.

## Adaptador Langflow

`erick_context_component.py` define `ErickContextPrep` con una entrada de texto,
un límite configurable y una salida `Message`. Usa la API `lfx` del proyecto.

1. Instala y ejecuta Langflow según la documentación original.
2. Coloca `erick_context.py` en una carpeta incluida en el `PYTHONPATH` del servidor.
3. Copia el contenido de `erick_context_component.py` al editor de un componente personalizado.
4. Conecta una entrada de texto y una salida de chat; prueba primero con la muestra.

**Estado verificado:** la lógica independiente tiene pruebas para Unicode,
espacios, límites y entradas vacías. El adaptador se validó sintácticamente;
su ejecución dentro de Langflow queda pendiente de una prueba de integración.

## Siguiente mejora

Añadir un presupuesto por tokens con un tokenizer explícito y conservar párrafos
según la estrategia de recuperación del agente.
