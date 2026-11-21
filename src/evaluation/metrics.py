"""Small metric helpers; use established libraries for full benchmark reporting."""
import numpy as np

def confusion_matrix(pred, target, num_classes, ignore_index=255):
    pred = np.asarray(pred).reshape(-1)
    target = np.asarray(target).reshape(-1)
    valid = (target != ignore_index) & (target >= 0) & (target < num_classes)
    ids = num_classes * target[valid].astype(np.int64) + pred[valid].astype(np.int64)
    return np.bincount(ids, minlength=num_classes**2).reshape(num_classes, num_classes)

def mean_iou(confusion):
    confusion = np.asarray(confusion, dtype=np.float64)
    intersection = np.diag(confusion)
    union = confusion.sum(0) + confusion.sum(1) - intersection
    valid = union > 0
    return float(np.mean(intersection[valid] / union[valid])) if valid.any() else float("nan")
