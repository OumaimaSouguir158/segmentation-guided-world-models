# Preprocessing

- Preserve original dataset splits and sequence identifiers.
- Resize with aspect ratio preserved; document interpolation for RGB and nearest-neighbor for labels.
- Map labels to a common class taxonomy only with an explicit mapping table.
- Treat void/ignore labels consistently.
- Normalize images using source-training statistics; do not recompute using test labels.
- Record corruptions, weather categories, time-of-day and domain metadata as evaluator-side metadata.
- Store dataset paths locally; never commit raw data or credentials.
