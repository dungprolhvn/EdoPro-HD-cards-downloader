import argparse
import time

from downloader import download_all, download_selected

def main():
    parser = argparse.ArgumentParser(description="YGO Card Image Downloader")
    parser.add_argument('-f', '--target-folder', type=str, default=r"C:\ProjectIgnis\pics", help='Directory to save images')
    parser.add_argument('-a', '--download-attempts', type=int, default=3, help='Number of download attempts for each image in case of failure')
    parser.add_argument('-r', '--retry', type=int, default=3, help='Number of download retries (for images that are failed to download after all attempt)')
    args = parser.parse_args()

    IMAGES_SAVE_LOCATION = args.target_folder
    IMAGES_DOWNLOAD_ATTEMPTS = args.download_attempts
    RETRY = args.retry
    
    
    start = time.time()
    print("Download started!")
    success, failure, failure_images_id = download_all(IMAGES_SAVE_LOCATION, IMAGES_DOWNLOAD_ATTEMPTS)
    with open('result.txt', 'w', encoding='utf-8') as f:
        f.writelines(f"{id}\n" for id in failure_images_id)
    end = time.time()
    total_time = (end - start) / 60
    print(f"Downloaded {success} images in {total_time} minutes.\nFailed to download {failure} images.\nFailure card images id are stored to result.txt")

    retry = 0
    while retry < RETRY and failure_images_id:
        print("-----------------------------------")
        print("Retrying to download failed images. Click Ctrl + C to stop")
        success, failure, failure_images_id = download_selected(IMAGES_SAVE_LOCATION, IMAGES_DOWNLOAD_ATTEMPTS, failure_images_id)
        with open('result.txt', 'w', encoding='utf-8') as f:
            f.writelines(f"{id}\n" for id in failure_images_id)
        print(f"RETRY #{retry + 1}:\nDownloaded {success} images in {total_time} minutes.\nFailed to download {failure} images.\nFailure card images id are stored to result.txt")
        retry += 1

    
if __name__ == '__main__':
    main()


