"""Conservative update gate; threshold calibration is an experiment responsibility."""
from dataclasses import dataclass

@dataclass
class GateDecision:
    allow_update: bool
    reason: str

def should_adapt(drift_score: float, threshold: float, confidence: float,
                 min_confidence: float = 0.70, updates_used: int = 0,
                 update_budget: int = 100) -> GateDecision:
    if updates_used >= update_budget:
        return GateDecision(False, "update budget exhausted")
    if confidence < min_confidence:
        return GateDecision(False, "confidence below minimum")
    if drift_score < threshold:
        return GateDecision(False, "drift threshold not reached")
    return GateDecision(True, "candidate update permitted; guard checks still required")
