import subprocess
import logging
from datetime import datetime

# Setup logging to file
log_filename = f'retag_and_push_docker_images_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'
logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Setup logging to console
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

def get_docker_images():
    result = subprocess.run(['docker', 'images', '--format', '{{.Repository}}:{{.Tag}} {{.ID}}'], capture_output=True, text=True)
    images = [line.split() for line in result.stdout.splitlines()]
    logging.info(f'Fetched docker images: {images}')
    return images

def retag_and_push_images(images, username):
    for image, image_id in images:
        if username not in image:
            repository, tag = image.split(":")
            new_tag = f'{username}/{repository.split("/")[-1]}:{tag}'
            logging.info(f'Retagging {image} to {new_tag}')
            try:
                subprocess.run(['docker', 'tag', image_id, new_tag], check=True)
                logging.info(f'Successfully retagged {image} to {new_tag}')
                subprocess.run(['docker', 'push', new_tag], check=True)
                logging.info(f'Successfully pushed {new_tag} to Docker Hub')
            except subprocess.CalledProcessError as e:
                logging.error(f'Failed to retag or push {image}. Error: {e}')
        else:
            logging.info(f'Skipping {image} as it already contains {username}')

def main():
    username = 'vpackets'
    images = get_docker_images()
    retag_and_push_images(images, username)
    logging.info('Retagging and pushing complete.')

if __name__ == '__main__':
    main()