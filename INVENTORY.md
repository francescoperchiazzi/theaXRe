# Inventory (apps/theaxre)

Snapshot of the `/apps/theaxre` folder (contents and sizes).

## Summary

- Total files: 55
- Total size: ~286 MB

## Top-level

| Path | Type | Purpose | Size |
|---|---:|---|---:|
| `index.html` | HTML | App (UI + JS) | ~252 KB |
| `sxretch.css` | CSS | Base styles (forked from sXRetch) | ~92 KB |
| `theaxre.css` | CSS | TheaXRe stylesheet entrypoint | ~28 KB |
| `translations.json` | JSON | i18n dictionary (30 languages; excludes `en`) | ~180 KB |
| `README.md` | MD | App docs | ~8 KB |
| `theaxre_qa_report.md` | MD | QA report (April 2026 snapshot) | ~6 KB |
| `INVENTORY.md` | MD | Folder snapshot | ~4 KB |
| `tools/i18n_audit.py` | PY | i18n audit utility | ~2.7 KB |

## Assets

### Models / AR files

| Path | Type | Size |
|---|---:|---:|
| `assets/usdz_celeste.usdz` | USDZ | ~36 MB |
| `assets/glb_celeste.glb` | GLB | ~36 MB |
| `assets/usdz_celeste_diorama.usdz` | USDZ | ~36 MB |
| `assets/glb_celeste_diorama.glb` | GLB | ~36 MB |
| `assets/usdz_demo_bruno.usdz` | USDZ | ~6.4 MB |
| `assets/glb_demo_bruno.glb` | GLB | ~6.4 MB |
| `assets/usdz_figma_visionOS.usdz` | USDZ | ~5.3 MB |
| `assets/glb_figma_visionOS.glb` | GLB | ~5.3 MB |
| `assets/glb_figma_export_window-and-window-controls.glb` | GLB | ~3.5 MB |

### Images (UI / examples / templates)

| Path | Type | Size |
|---|---:|---:|
| `assets/img_figma-visionOS_06.png` | PNG | ~7.6 MB |
| `assets/img_bruno_sketch_03.jpg` | JPG | ~4.3 MB |
| `assets/img_ui_value_03.png` | PNG | ~4.4 MB |
| `assets/img_ui_value_04.png` | PNG | ~4.0 MB |
| `assets/img_ui_value_05.png` | PNG | ~3.8 MB |
| `assets/img_clippingmask.png` | PNG | ~1.7 MB |
| `assets/demo_panel_04.png` | PNG | ~444 KB |
| `assets/img_figma-visionOS_05.png` | PNG | ~2.8 MB |
| `assets/demo_panel_03.png` | PNG | ~2.7 MB |
| `assets/img_figma_export_window-and-window-controls.png` | PNG | ~2.6 MB |
| `assets/img_ui_value_02.png` | PNG | ~2.1 MB |
| `assets/demo_panel_01.png` | PNG | ~2.0 MB |
| `assets/img_vr-room_value_01.png` | PNG | ~1.8 MB |
| `assets/img_bruno_crib_01.jpg` | JPG | ~1.3 MB |
| `assets/img_ui_value_01.png` | PNG | ~1.3 MB |
| `assets/demo_panel_02.png` | PNG | ~724 KB |
| `assets/img_figma-visionOS_03.png` | PNG | ~820 KB |
| `assets/img_bruno_sketch_02.jpg` | JPG | ~800 KB |
| `assets/pdf_TheaXRe_Grid_Template.pdf` | PDF | ~708 KB |
| `assets/img_figma-visionOS_02.png` | PNG | ~672 KB |
| `assets/img_bruno_sketch_01.jpg` | JPG | ~612 KB |
| `assets/img_bruno_crib_02.jpg` | JPG | ~531 KB |
| `assets/img_celeste_demo_01.jpg` | JPG | ~524 KB |
| `assets/img_celeste_demo_02.jpg` | JPG | ~524 KB |
| `assets/img_celeste_demo_03.jpg` | JPG | ~524 KB |
| `assets/img_celeste_demo_04.jpg` | JPG | ~524 KB |
| `assets/img_figma-visionOS_04.png` | PNG | ~504 KB |
| `assets/demo_panel_05.png` | PNG | ~443 KB |
| `assets/img_TheaXRe_Grid_Template.png` | PNG | ~29 KB |
| `assets/demo_panel_06.png` | PNG | ~19 KB |

### Icons

| Path | Type | Size |
|---|---:|---:|
| `assets/ico_theaxre.png` | PNG | ~8 KB |
| `assets/ico_theaxre_thumbnail_placeholder_dark-mode.png` | PNG | ~4 KB |
| `assets/ico_theaxre_thumbnail_placeholder_light-mode.png` | PNG | ~2.1 KB |
| `assets/ico_theaxre.svg` | SVG | ~2 KB |

## Notes

- The USDZ/GLB files dominate the total size: great for demos, but heavy for transfer.
- `.DS_Store` should typically be excluded from version control.
- ML Background removal has been completely removed from the codebase.
- A 6-slot Theatre setup is currently in place (1 backdrop + 5 depth planes).
- Each plane uses a 4x5 grid for panel positioning, supporting multiple shapes (square, column, row, horseshoe, full stage).
- Features a custom clipping mask tool to cut out shapes manually.
- Includes a Diorama Mode to scale down the generated model for desktop viewing (e.g., 3m becomes 30cm).
- Diorama toggle also adjusts gap defaults (0.25 in diorama, 0.5 in real size) and can auto-regenerate exports.
- Includes SVG perspective diagram and animated grid in the UI.

### Video

| Path | Type | Size |
|---|---:|---:|
| `assets/video_theaxre_demo.mp4` | MP4 | ~25 MB |
| `assets/video_theaxre_usdz.mp4` | MP4 | ~25 MB |
