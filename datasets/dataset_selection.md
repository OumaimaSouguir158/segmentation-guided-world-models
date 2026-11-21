# Dataset Selection Rationale

| Dataset | Role | Shift value | Practical caveat |
|---|---|---|---|
| Cityscapes | Primary source / in-domain baseline | Urban scenes, sequence/city structure | Registration; large images; official split constraints |
| ACDC | Primary adverse-condition target | Fog, night, rain, snow; corresponding scenes | License terms; evaluate uncertainty labels carefully |
| BDD100K | Expansion target | Weather, time-of-day, geography | Large download; task-specific labels/splits |
| Mapillary Vistas | Geographic/domain diversity | Diverse cities and capture devices | Research license / access request |
| GTA5 | Synthetic source option | Synthetic-to-real | Synthetic appearance; large storage |
| SYNTHIA | Synthetic source option | Synthetic-to-real | Class mapping and split compatibility |

**Initial recommendation:** Cityscapes → ACDC for a controlled adverse-condition study. Do not claim this pair covers all domain shifts. Add BDD100K or Mapillary only after the core pipeline is stable.
