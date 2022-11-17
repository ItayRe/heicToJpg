import os
from PIL import Image
import pillow_heif


def heic_to_jpg_func():
    """
    Convert an entire folder and converts the HEIC files to a JPEG
    """
    # The main folder path
    main_folder = r'main_folder_path'

    # The secondary folders name if necessary
    secondary_folders_names = ['sub-folder1', 'sub-folder2', 'sub-folder3']

    # Loop over each sub-folder
    for sec_name in secondary_folders_names:

        # Creating the sub-folder path
        sec_folder = main_folder + sec_name + r'\\'

        # Iterating over each file in the sub-folder
        for file_name in os.listdir(sec_folder):

            # Checks if a file is HEIC
            if file_name[-4:] == 'HEIC' or file_name[-4:] == 'heic':
                # Creating the file path
                file = sec_folder + file_name

                # Reading the HEIC file
                heif_file = pillow_heif.open_heif(file)

                # Save the file as Image object
                image = Image.frombytes(
                    heif_file.mode,
                    heif_file.size,
                    heif_file.data,
                    "raw",
                    heif_file.mode,
                    heif_file.stride,
                )

                # Save the file as JPEG
                new_file_name = file_name.split('.')[0]
                new_file_name = new_file_name + '.JPEG'
                new_file_name_path = sec_folder + new_file_name
                image.save(new_file_name_path, "JPEG")

                # Remove the old file (HEIC file). Sometimes it's not work so just delete it manually.
                os.remove(sec_folder)


if __name__ == '__main__':
    heic_to_jpg_func()
