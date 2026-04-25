# TheaXRe

A browser-based XR scenography tool for presepe builders, set designers, puppet theatre makers, and anyone who composes spatial scenes from a desk.

## For Bruno

This tool is a birthday gift for Bruno Perchiazzi, who turns 80 in May 2026. A geometra (a technical draughtsman-surveyor) who spent his career at [Aeritalia](https://en.wikipedia.org/wiki/Aeritalia) and [CIRA](https://www.cira.it/en), his university architecture studies were interrupted by the student movements of 1968, but architecture never left him. Instead, it found another home in the presepe (the Neapolitan nativity scene tradition), where he has spent decades composing ancient hilltop towns and candlelit streets from cork, plaster, and moss. TheaXRe lets him see those compositions standing in real space, at real scale, before a single piece of cork is cut.

### The Art of the Presepe

Bruno's work is a masterclass in architectural storytelling. His most notable exhibition, the traditional Neapolitan Crib hosted at the [Chapel Royal in Dublin Castle](https://dublincastle.ie/the-chapel-royal/), exemplifies his meticulous approach to the craft. 

His methodology is deeply rooted in his architectural background. Before the final scene is constructed, he begins with a precise 1:10 diorama phase—a miniature prototype where spatial relationships, lighting, and composition are rigorously tested. This is where the magic of forced perspective is perfected, creating an illusion of vast, winding cityscapes and infinite depth within a strictly confined physical space. It is this exact process of spatial prototyping that TheaXRe aims to augment, allowing the diorama phase to be experienced at true scale through mixed reality.

## The lineage

It started with Celeste watching Mary Poppins jump into a chalk drawing and asking if we could do that with a computer. By the end of that afternoon, her drawing was floating in our living room, which became sXRetch—a simple tool to turn a single image into an XR prop.

TheaXRe is what came next. It takes that same impulse and expands it into multi-plane scenography, allowing multiple drawings to be arranged in depth to form a complete stage.

## What it does

TheaXRe is a client-side authoring tool that lets you upload multiple drawings or photographs, arrange them across different depth planes, and adjust their scale and position. You can then export the composed scene as a single 3D file that can be opened instantly on a smartphone, projecting your stage design into your physical room at real scale.

- Depth planes for spatial composition
- 4x5 position grid per panel
- Panel shape selection (Square, Column, Row, Horseshoe/Arch, Full Stage)
- Custom clipping mask tool for manual cutouts
- Diorama Mode for desktop-scale preview
- Gap control between planes (defaults: 0.25 in Diorama, 0.5 in Real Size)
- Dual GLB and USDZ export
- AR preview on iOS and Android
- Backdrop can be skipped (export will hide the backdrop plane)
- GLB can be imported into game engines (e.g. Godot) for rapid prototyping
- SVG perspective diagram and animated grid in the UI
- Printable PDF drawing template for sketching physical panels
- 31 languages supported (100% native i18n coverage, RTL support)
- 100% client-side processing, no upload required

## Technical Logic

TheaXRe is built on a custom client-side pipeline that composes 2D images into 3D space:

### The 4x5 Grid System
Instead of a simple positional offset, each depth plane features a 4x5 grid. This allows users to place their cutouts precisely within the stage's frame. The grid translates the 2D column/row coordinates into 3D space (X and Y offsets) relative to the stage's center.

### Shape Handling
Panels can be assigned specific shapes that dictate how they occupy the grid:
- **Square**: Typically occupies a 2x2 area.
- **Column**: A vertical 1x4 layout, perfect for pillars or side wings.
- **Row**: A horizontal 5x1 layout for elements like headers or floor pieces.
- **Horseshoe (Arch) / Full Stage**: Occupies the entire 4x5 grid. The horseshoe shape applies a specific CSS `clip-path` (and a canvas cutout during export) to create an archway, allowing the backdrop or planes behind it to be visible through the center.

### Custom Clipping Mask
To remove unwanted backgrounds without relying on heavy Machine Learning models, TheaXRe includes a custom canvas-based masking tool. Users can draw a polygon around their subject by clicking to place points. The app uses the HTML5 Canvas API (`globalCompositeOperation = 'source-in'`) to apply this polygon as a clipping mask, rendering the area outside the polygon as transparent before passing the image to the 3D generation step. The UI includes a dedicated “Clipping Mask” explainer section with a reference image (`assets/img_clippingmask.png`).

### Dual USDZ / GLB Export Process
When the user generates the scene, the app simultaneously creates two formats to ensure maximum compatibility:
- **GLB**: Built manually by constructing a glTF JSON structure and a binary chunk (BIN). The app calculates the 3D quads for each plane, applies the masked images as textures, and packages them into a valid `.glb` file.
- **USDZ**: Generated by creating an uncompressed ZIP archive containing a `.usda` (Universal Scene Description text file) and the texture images. The USDA file defines the spatial hierarchy, materials, and geometry mapping for iOS Quick Look.
Both exports are executed 100% client-side using JavaScript `Blob` and `ArrayBuffer` manipulations.

## Local run

TheaXRe is a static web application. It runs entirely in the browser without a backend.
To run it locally, you just need a local web server (to avoid CORS issues with modules).

```bash
# Using Python 3
python3 -m http.server 8000
```
Then open `http://localhost:8000/apps/theaxre/` in your browser.

## Structure

- `index.html` - The main interface and application logic.
- `theaxre.css` - Styling and layout (forked from sXRetch).
- `translations.json` - i18n dictionary for 31 languages.
- `assets/` - Icons, video demos (`video_theaxre_*.mp4`), Celeste demo drawings, Bruno's sketches and crib photos, drawing templates, and example models (including diorama exports and Figma/visionOS demos).
- `tools/i18n_audit.py` - A utility script to check translation coverage.

## Privacy

TheaXRe is fully client-side. Your images are never uploaded to any server. The 3D files (USDZ and GLB) are generated locally in your browser. 

At runtime, the app fetches a few third-party resources:
- Google Fonts (IBM Plex Sans, Noto Sans for specific scripts)
- `@google/model-viewer` from unpkg.com

These services may log your IP address according to their own privacy policies, compliant with GDPR.

## Security

TheaXRe includes a minimal Content Security Policy (CSP) via a meta tag in `index.html`.

## Credits & legal

Concept, design, and development by Francesco Perchiazzi.
Illustrations by Celeste Perchiazzi.
Built for Bruno Perchiazzi, the reason this exists.

Released under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International ([CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/)).

Credits to:
- Apple (USDZ format)
- Google (Model-Viewer)
- Disney (Mary Poppins, Robert Stevenson, 1964)
