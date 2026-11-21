# BloomBox Port Store — compatibilidad y verificaciones

El catálogo **general** se consulta directamente desde [OpenPortsGames](https://openportsgames.com/api/ports.json) (datos CC BY 4.0). **Nunca** se eliminan ports del catálogo por no funcionar con Husk.

`catalog/port-verifications.json` contiene **únicamente** pruebas realizadas por el equipo BloomBox. Las insignias no usan el atributo `verified` de OpenPortsGames: ese atributo significa otra cosa.

## Formato de los registros

```json
{
  "id": "2-ship-2-harkinian-android",
  "state": "verified",
  "portVersion": "5.0.1-android.3",
  "testedAt": "2026-11-21",
  "bloomboxVersion": "3.1.0",
  "huskVersion": "VERSION_REAL",
  "device": "iPhone 14 Pro / iOS 27",
  "notesEs": "Prueba completada con APK original y archivos legales.",
  "notesEn": "Tested with original APK and legally owned game data."
}
```

Estados: `verified` (comprobado), `issues` (funciona con errores), `incompatible` (no funciona). Sin registro equivale a `Sin verificar`.

**Regla estricta:** `verified` debe coincidir con el ID y la versión **exacta** del catálogo de origen. Si OpenPortsGames publica otra versión, BloomBox deja de mostrar la insignia de verificado hasta repetir las pruebas. Se puede revocar la verificación eliminando o reemplazando el registro.

No crear registros basados en suposiciones o solo por disponer del APK. No redistribuir APK ni contenido comercial desde este repositorio.
