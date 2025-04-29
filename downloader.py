import errno
import json
import os
import requests
import tempfile
import time

API_URL = 'https://db.ygoprodeck.com/api/v7/cardinfo.php'


def check_valid_directory(images_save_location):
    """This function check if the given directory is valid (writeable)
    
    for saving downloaded images
    Args:
        images_save_location (str): The absolute path of the directory (folder) to save the images
    
    Authors:
        Nguyen Dinh Dung
    """
    try:
        if not os.path.exists(images_save_location):
            os.makedirs(images_save_location)
        testfile = tempfile.TemporaryFile(dir=images_save_location)
        testfile.close()
    except PermissionError:
        print("The program does not have permission to write at the destination folder.")
        raise
    except OSError as e:
        print(f"OS error: {e}")
        raise
    

def download_all(images_save_location, attempts):
    """This function download all HD card images from YGOPRODeck and save it
    to the given directory

    Args:
        images_save_location (str): The absolute path of the directory (folder) to save the images
        attempts (int): Maximum number of download attempts for an image in case of a failure

    Returns:
        tuple: A tuple containing the number of successful downloads, failure downloads,
                and a list containing card image ids that the program failed to download
    
    Authors:
        Nguyen Dinh Dung
    """
    check_valid_directory(images_save_location)
        
    response = requests.get(API_URL)
    data = response.json()
    all_cards = data['data']
    success_count = 0
    failure_card_image_ids = []
    for card in all_cards:
        for image in card['card_images']:
            id = image['id']
            url = image['image_url']
            # three download attempts
            for attempt in range(attempts):
                try:
                    response = requests.get(url)
                    destination = os.path.join(images_save_location, f'{id}.jpg')
                    with open(destination, 'wb') as img_f:
                        img_f.write(response.content)
                    print(f"{id} Downloaded HD image for {card['type']} card: {card['name']}")
                    success_count += 1
                    # pause execution due to api rate limit
                    time.sleep(0.05)
                    break
                except Exception as e:
                    print(f"{id} Some error occured while downloading {card['type']} card: {card['name']}")
                    print(e)
                    if attempt == attempts -  1:
                        failure_card_image_ids.append(id)
                        
    print("DONE!")
    return (success_count, len(failure_card_image_ids), failure_card_image_ids)


def download_selected(images_save_location, attempts, card_image_ids):
    """This function download all HD card images with id in card_image_ids from YGOPRODeck 
    and save it to the given directory

    Args:
        images_save_location (str): The absolute path of the directory (folder) to save the images
        attempts (int): Maximum number of download attempts for an image in case of a failure
        card_image_ids (list): The list containing card images id to download
    
    Returns:
        tuple: A tuple containing the number of successful downloads, failure downloads,
                and a list containing card image ids that the program failed to download
    
    Authors:
        Nguyen Dinh Dung
    """
    check_valid_directory(images_save_location)

    success_count = 0
    failure_card_image_ids = []
    for id in card_image_ids:
        url = f"https://images.ygoprodeck.com/images/cards/{id}.jpg"
        for attempt in range(attempts):
            try:
                response = requests.get(url)
                destination = os.path.join(images_save_location, f'{id}.jpg')
                with open(destination, 'wb') as img_f:
                    img_f.write(response.content)
                print(f"{id} Downloaded HD image")
                success_count += 1
                time.sleep(0.05)
                break
            except Exception as e:
                print(f"{id} Some error occurred while downloading image")
                print(e)
                if attempt == attempts - 1:
                    failure_card_image_ids.append(id)

    print("DONE!")
    return (success_count, len(failure_card_image_ids), failure_card_image_ids)
        
            




