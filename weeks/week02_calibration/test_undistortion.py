"""Compare held-out images with their undistorted versions.

Run from weeks/week02_calibration/ after running camera_calibration.py.
The saved camera parameters are reused without recalibration.
"""

import glob
import os
import pickle

import cv2


CALIBRATION_FILE = 'output/calibration_data.pkl'
TEST_IMAGES_PATH = 'test_images/*.jpg'
OUTPUT_DIRECTORY = 'output/test_undistorted'
# Resolution used to estimate the saved camera matrix: (width, height).
CALIBRATION_IMAGE_SIZE = (640, 480)
SHOW_IMAGES = True  # Set False to save results without opening a display window.


def undistort_test_images():
    """Save and optionally display corrections using the fixed calibration."""
    if not os.path.isfile(CALIBRATION_FILE):
        raise FileNotFoundError(
            f'Calibration file not found: {CALIBRATION_FILE}. '
            'Run camera_calibration.py first.'
        )

    images = sorted(glob.glob(TEST_IMAGES_PATH))
    if not images:
        raise FileNotFoundError(f'No test images found at {TEST_IMAGES_PATH}')

    with open(CALIBRATION_FILE, 'rb') as calibration_file:
        calibration_data = pickle.load(calibration_file)
    mtx = calibration_data['camera_matrix']
    dist = calibration_data['distortion_coefficients']

    os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)
    print(f'Found {len(images)} test images. Using saved calibration without refitting.')
    if SHOW_IMAGES:
        print('Original: left. Undistorted: right.')
        print('Press any key for the next image; q or Escape to quit.')

    try:
        for filename in images:
            img = cv2.imread(filename)
            if img is None:
                raise ValueError(f'Could not read image: {filename}')

            height, width = img.shape[:2]
            if (width, height) != CALIBRATION_IMAGE_SIZE:
                raise ValueError(
                    f'{filename}: expected size {CALIBRATION_IMAGE_SIZE}, '
                    f'got {(width, height)}. Use images at the calibration resolution.'
                )

            new_mtx, _ = cv2.getOptimalNewCameraMatrix(
                mtx, dist, (width, height), 1, (width, height)
            )
            # Keep the full image, including invalid borders; do not crop or resize.
            corrected = cv2.undistort(img, mtx, dist, None, new_mtx)

            # Label copies so the saved corrected image contains no annotations.
            original_view = img.copy()
            corrected_view = corrected.copy()
            for view, label in (
                (original_view, 'Original'),
                (corrected_view, 'Undistorted'),
            ):
                cv2.putText(
                    view, label, (15, 30), cv2.FONT_HERSHEY_SIMPLEX,
                    0.8, (0, 255, 0), 2
                )
            comparison = cv2.hconcat([original_view, corrected_view])

            basename = os.path.basename(filename)
            # PNG avoids introducing another round of lossy JPEG compression.
            stem = os.path.splitext(basename)[0]
            for prefix, result in (
                ('undistorted', corrected),
                ('comparison', comparison),
            ):
                output_path = os.path.join(OUTPUT_DIRECTORY, f'{prefix}_{stem}.png')
                if not cv2.imwrite(output_path, result):
                    raise OSError(f'Could not save image: {output_path}')
                print(f'Saved {output_path}')

            if SHOW_IMAGES:
                cv2.imshow('Test images: original | undistorted', comparison)
                key = cv2.waitKey(0) & 0xFF
                if key in (ord('q'), 27):
                    break
    finally:
        if SHOW_IMAGES:
            cv2.destroyAllWindows()

    print('Image inspection finished. No numerical test error was calculated.')


if __name__ == '__main__':
    undistort_test_images()
