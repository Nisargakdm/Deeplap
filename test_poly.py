import numpy as np
import cv2
from backend.app.services.geometry_extractor import GeometryExtractor

binary_mask = np.zeros((512, 512), dtype=np.uint8)
y, x = np.ogrid[:512, :512]
dist_from_slick = ((x - 256) / 120.0)**2 + ((y - 256) / 35.0)**2
binary_mask[dist_from_slick < 1.0] = 1

mask_uint8 = (binary_mask > 0.5).astype(np.uint8) * 255
contours, _ = cv2.findContours(mask_uint8, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print(f"Number of contours: {len(contours)}")

for contour in contours:
    print(f"Contour area: {cv2.contourArea(contour)}")
    pts = contour.squeeze()
    print(f"Squeezed shape: {pts.shape}")

bbox = [68.95, 20.45, 69.25, 20.75]
result = GeometryExtractor.mask_to_geojson(binary_mask, bbox)
print(result["geojson"])
