ComfyUI Image Resolutions
=========================

This repository provides a small custom node for ComfyUI that makes it easy to select optimized image resolutions and aspect ratios. The node exposes a set of curated resolution presets (including model-specific sets) and returns the selected resolution along with width and height values for use in ComfyUI pipelines.

Highlights
- Simple node to pick resolutions and aspect ratios
- Preset groups for general use and model-optimized sets
- Python node implementation and matching client-side JS helper to filter ratio options dynamically

Files
- `sdxl_image_resolutions.py`: Python node implementation (registers `SDXLImageResolutions`)
- `js/sdxl_image_resolutions.js`: Client-side helper to dynamically populate aspect ratio options
- `__init__.py`: Module export for ComfyUI to import mappings

License
- See LICENSE.md

