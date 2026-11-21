# BloomBox Android Port Store — compatibility records

The Port Store lists **all Android ports** from [OpenPortsGames](https://openportsgames.com/), whether or not they run on Husk or BloomBox. This repository does not mirror APK binaries or the upstream catalog.

The overlay is [android-port-verifications.json](android-port-verifications.json). BloomBox joins entries by exact upstream port ID and exact release version. Neither an OpenPortsGames verification flag nor a downloadable APK implies compatibility with iOS or Husk.

## Adding a verified port

Example entry (illustrative, NOT tested):

~~~json
{
  "id": "example-android-port",
  "version": "1.2.3",
  "status": "verified",
  "testedAt": "2026-11-21",
  "bloomboxVersion": "3.1.0",
  "huskVersion": "test-build-id",
  "notes": "Installed, launched, and reached gameplay on a specified device.",
  "notesEn": "Installed, launched, and reached gameplay on a specified device."
}
~~~

Use the exact port ID and version in the upstream API. Record the iPhone model, iOS version, JIT state, and test conditions in notes whenever known.

Allowed statuses:

- **verified**: installed, launched, and essential gameplay or functionality passed.
- **issues**: works partly but has reproducible failures documented in notes.
- **incompatible**: installation or startup was tested and failed.

For every upstream version change, BloomBox falls back to **unverified** until a matching record is published. A badge never automatically transfers across versions.

## Rules

- Never award badges without a real device test; unknown is NOT incompatible.
- Do not claim full compatibility if only a launcher was tested.
- Revoke a previous positive verdict if that exact build is found to fail.
- Only reference official upstream downloads. No mirrors of proprietary game assets.
- Maintain a single current verification record per port ID.
- Preserve catalog attribution to OpenPortsGames (CC BY 4.0 for its own entries) and original authors for separately imported records.

## Sources

- https://openportsgames.com/api/ports.json
- https://github.com/Kymie131/openportsgames/blob/main/LICENSE-DATA
