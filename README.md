pip install -i https://test.pypi.org/simple/ lol-build-generator==1.0.2

https://test.pypi.org/project/lol-build-generator/1.0.2/

get_rune_sequence_guide()->returns an image of the rune selection guide and console prints a message that describes the process of sequencing runes

generate_rune_page(sequence, directory=None, bg_color=background_color)->takes a rune sequence in String and returns a rune page image. Optionally provide a saving directory for the image or a color for the background/border. A parser is provided to get rune sequence from comma separated runes in text form. 

generate_item_page(loi, directory=None, bg_color=background_color)->takes a list of item names and returns a rune page image. Optionally provide a saving directory for the image or a color for the background/border. These item names must be precise, but you can use the provided parser function to get auto corrected words to feed into this function. 

generate_summoner_page(los, directory=None, bg_color=background_color)->takes a list of summoner names and returns a rune page image. Optionally provide a saving directory for the image or a color for the background/border. These summoner names must be precise, but you can use the provided parser function to get auto corrected words to feed into this function. 

find_closest_items(user_input, show_parsed_items=False)->takes a string of comma separated words and parses them to the closest matching item name using levinstein distance. Optionally can print to console with show_parsed_items. 

find_closest_summoners(user_input, show_parsed_summoners=False)->takes a string of comma separated words and parses them to the closest matching summoner spell name using levinstein distance. Optionally can print to console with show_parsed_items. 

find_closest_runes(user_input, show_parsed_runes=False)->takes a string of comma separated words and parses them to the closest matching summoner spell name using levinstein distance. The user must enter the complete rune set, [Primary tree type, keystone, 1st rune, 2nd rune, 3rd rune, Secondary tree type, 1st rune, 2nd rune, 1st shard, 2nd shard, 3rd shard], in a comma separated fashion. If format is incorrect will return a None type. Optionally can print to console with show_parsed_runes. 

Image manipulation functions:

replace_background(image, background, bg_color=(0,0,0))->replace the background of image with background. background is defined by pixels that are bg_color

paste_with_mask(bg, im, xy=(0,0))->a version of the paste function from Image library but respects image masking, aka pixels that are empty

grayscale(im)-> cretes grayscale image that is still 3 channel instead of single channel like the default library

change_opacity(im, alpha)-> changes opacity of 3 channel images, which does not have an alpha channel by default

concat_images(im1, im2, direction, bg_color=background_color)-> concatenate im2 direction of im1. Directions are ["below","above","left","right"]. For example place im2 above im1 or im2 left im1. Can optionally provide bg_color as tuple (int,int,int).
