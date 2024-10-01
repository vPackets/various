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

def retag_and_push_images(images, username, specified_images):
    for image, image_id in images:
        repository, tag = image.split(":")
        if f"{repository}:{tag}" in specified_images:
            new_tag = f'{username}/{repository.split("/")[-1]}:{tag}' if not repository.startswith(username) else f'{repository}:{tag}'
            logging.info(f'Retagging {image} to {new_tag}')
            print(f'Retagging {image} to {new_tag}')
            try:
                subprocess.run(['docker', 'tag', image_id, new_tag], check=True)
                logging.info(f'Successfully retagged {image} to {new_tag}')
                print(f'Successfully retagged {image} to {new_tag}')
                subprocess.run(['docker', 'push', new_tag], check=True)
                logging.info(f'Successfully pushed {new_tag} to Docker Hub')
                print(f'Successfully pushed {new_tag} to Docker Hub')
            except subprocess.CalledProcessError as e:
                logging.error(f'Failed to retag or push {image}. Error: {e}')
                print(f'Failed to retag or push {image}. Error: {e}')
        else:
            logging.info(f'Skipping {image} as it is not in the specified images list')
            print(f'Skipping {image} as it is not in the specified images list')

def main():
    username = 'vpackets'
    specified_images = [
        'vpackets/cisco_cat9kv:17.12.01p',
        '8201-32fh_clab276:24.1.1',
        'vpackets/8201-32fh_clab276:24.1.1',
        'vpackets/cisco_cat8kv:17.11.01a',
        'vpackets/8201-32fh_242:24.2.1.23l',
        '8201-32fh_242:24.2.1.23l',
        'vpackets/alpine-tools-containerlab-isp-02:latest',
        'vpackets/alpine-tools-containerlab-isp-01:latest',
        'vpackets/ubuntu-22.04-frr-deb:latest',
        'vpackets/ubuntu-22.04-frr:latest',
        'vrnetlab/vr-csr:17.03.08',
        'vpackets/net-tools:latest',
        'vpackets/alpine-tools:0.0.1',
        'vpackets/alpine-tools:latest',
        'vpackets/net-tools:0.0.1',
        'ios-xr/xrd-control-plane:7.10.2',
        'vrnetlab/vr-vmx:21.2R1.10',
        '8202-32fh-m_215:7.10.1',
        '8201-32fh_214:7.10.1',
        'vrnetlab/vr-csr:17.03.04',
        'vrnetlab/vr-n9kv:10.4.1',
        'ceos:4.30.3M',
        '8101-32h_210:7.10.1',
        'frr-srv6-usid-ubuntu22:rev1.2',
        'ubuntu-frr-22.04:latest',
        'networkop/cx:5.3.0',
        'ghcr.io/hellt/cisco_xrv9k:7.3.1',
        'ghcr.io/hellt/cisco_csr1000v:17.03.03',
        'networkop/cx:4.4.0',
        'networkop/kernel:4.19'
    ]
    images = get_docker_images()
    retag_and_push_images(images, username, specified_images)
    logging.info('Retagging and pushing complete.')
    print('Retagging and pushing complete.')

if __name__ == '__main__':
    main()