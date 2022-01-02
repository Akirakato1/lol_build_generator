#library script
from PIL import Image
from numpy import array as nparray
from numpy import mean as npmean

def get_rune_sequence_guide():
    im=get_image("RuneSequenceGuide",directory_rune)
    print("Sequencing is in the order of:\n [Primary tree type, keystone, 1st rune, 2nd rune, 3rd rune, Secondary tree type, 1st rune, 2nd rune, 1st shard, 2nd shard, 3rd shard]")
    print("Since secondary tree only allows for 2 runes to choose out of the 3 rows available, one of the row will be empty")
    print("For the row corresponding to no selection of rune, the placeholder value is 5")
    print("For all other selections, the sequence value is the 0 indexed number counting from the left")
    print("For example, Domination's icon is second from the left, so counting from 0, its value 1")
    print("Cheapshot's icon is the first one from the left so its value is 0.")
    print("A sample rune page sequence for \n[dominate, electroctue, sudden impact, eyeball collection, raveenous hunteress, sorcery, transendence, gathering storms, adaptiving, adaptive, health]")
    print("will look like this: 102202502000")
    return im

def generate_rune_page(sequence, directory=None, bg_color=background_color):
    background=Image.new(mode="RGB", size=(unit*10+3*boundary_width, unit*5+2*boundary_width), color=bg_color)
    first_tree=int(sequence[0])
    first_runes=[int(i) for i in sequence[2:5]]
    keystone=int(sequence[1])
    second_tree=int(sequence[5])
    second_runes=[int(i) for i in sequence[6:9]]
    small_runes=[int(i) for i in sequence[9:12]]
    
    primary=get_image(tree[first_tree]+"Square",directory_rune).resize((unit*5,unit*5))
    secondary=get_image(tree[second_tree]+"Square",directory_rune).resize((unit*5,unit*5))
    
    if first_tree<2 and keystone<2:
        keystone-=1
    if first_tree==1 and first_runes[2]<2:
        first_runes[2]-=1
    if second_tree==1 and second_runes[2]<2:
        second_runes[2]-=1
    
    primary=place_tree(primary, first_tree, unit)
    primary=place_keystone(primary,first_tree, keystone, unit, 1)
    primary=place_runes(primary, first_tree, first_runes, unit, 2)
    
    secondary=place_tree(secondary, second_tree, unit)
    secondary=place_runes(secondary, second_tree, second_runes, unit, 1)
    secondary=place_shards(secondary, small_runes, unit, 4)
    
    Image.Image.paste(background, primary, (boundary_width, boundary_width))
    Image.Image.paste(background, secondary, (unit*5+2*boundary_width, boundary_width))
    
    if type(directory)!=type(None):
        background.save(directory)
    
    return background

def generate_item_page(loi, directory=None, bg_color=background_color):
    background=Image.new(mode="RGB", size=(unit*6+7*boundary_width, unit+2*boundary_width), color=bg_color)
    for i in range(min(6,len(loi))):
        Image.Image.paste(background, get_image(loi[i],directory_item),((i+1)*(unit+boundary_width)-unit,boundary_width))
    
    if type(directory)!=type(None):
        background.save(directory)
    
    return background

def generate_summoner_page(los, directory=None, bg_color=background_color):
    background=Image.new(mode="RGB", size=(unit*2+3*boundary_width, unit+2*boundary_width), color=bg_color)
    for i in range(min(2,len(los))):
        Image.Image.paste(background, get_image(los[i],directory_summoner),((i+1)*(unit+boundary_width)-unit,boundary_width))
    
    if type(directory)!=type(None):
        background.save(directory)
    
    return background

def place_shards(image, small_runes, unit, start_height):
    for i in range(3):
        image=paste_with_mask(image, get_image(rune_shards[i][small_runes[i]],directory_rune), (int((i+1.25)*unit), int((start_height+0.25)*unit)))
    return image

def place_keystone(image, index_tree, index_keystone, unit, start_height):
    for i in range(5):
        if i!=index_keystone+1:
            image=paste_with_mask(image, grayscale(get_image(keystones[tree[index_tree]][i],directory_rune)), (i*unit,start_height*unit))
        else:
            image=paste_with_mask(image, get_image(keystones[tree[index_tree]][i],directory_rune), (i*unit,unit))
    return image

def place_tree(image, index_tree, unit):
    for i in range(5):
        if i!=index_tree:
            image=paste_with_mask(image, grayscale(get_image(tree[i],directory_rune)), (i*unit,0))
        else:
            image=paste_with_mask(image, get_image(tree[i],directory_rune), (i*unit,0))
    return image
    
def place_runes(image, index_tree, index_runes, unit, start_height):
    for j in range(3):
        for i in range(5):
            name=runes[tree[index_tree]][j][i]
            if i!=index_runes[j]+1:
                image=paste_with_mask(image, add_ring(grayscale(get_image(name,directory_rune)),name), (i*unit,(j+start_height)*unit))
            else:
                image=paste_with_mask(image, add_ring(get_image(name,directory_rune),name), (i*unit,(j+start_height)*unit))
    return image

def add_ring(im, name):
    if name!="Blank":
        return paste_with_mask(im,get_image("Ring",directory_rune))
    else:
        return im

def get_image(name, directory):
    return Image.open(directory+name+".png")

def replace_background(image, background, bg_color=(0,0,0)):
    arr=nparray(image)
    background.putalpha(100)
    back=nparray(background)[:,:,:3]
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            if arr[i][j][0]==bg_color[0] and arr[i][j][1]==bg_color[1] and arr[i][j][2]==bg_color[2]:
                arr[i][j]=back[i][j]
    return Image.fromarray(arr)

def paste_with_mask(bg, im, xy=(0,0)):
    arr=nparray(im)
    bgarr=nparray(bg)
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            if sum(arr[i][j])!=0:
                bgarr[i+xy[1]][j+xy[0]][0]=arr[i][j][0]
                bgarr[i+xy[1]][j+xy[0]][1]=arr[i][j][1]
                bgarr[i+xy[1]][j+xy[0]][2]=arr[i][j][2]
    
    return Image.fromarray(bgarr)

def grayscale(im):
    arr=nparray(im)
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            val=int(npmean(arr[i][j]))
            arr[i][j][0]=val
            arr[i][j][1]=val
            arr[i][j][2]=val
            
    return Image.fromarray(arr)

def change_opacity(im, alpha):
    image=nparray(im)
    for i in range(logo.shape[0]):
        for j in range(logo.shape[1]):
            image[i][j][0]=image[i][j][0]+int((255-image[i][j][0])*alpha)
            image[i][j][1]=image[i][j][1]+int((255-image[i][j][1])*alpha)
            image[i][j][2]=image[i][j][2]+int((255-image[i][j][2])*alpha)
    return Image.fromarray(image)

#place im2 in given direction on im1
def concat_images(im1, im2, direction, bg_color=background_color):
    if direction=="above":
        return concat_images(im2, im1, "below", bg_color)
    elif direction=="left":
        return concat_images(im2, im1, "right", bg_color)
    elif direction=="right":
        background=Image.new(mode="RGB", size=(im1.size[0]+im2.size[0],max(im1.size[1],im2.size[1])), color=bg_color)
        Image.Image.paste(background, im1, (0,0))
        Image.Image.paste(background, im2, (im1.size[0],0))
        return background
    elif direction=="below":
        background=Image.new(mode="RGB", size=(max(im1.size[0],im2.size[0]),im1.size[1]+im2.size[1]), color=bg_color)
        Image.Image.paste(background, im1, (0,0))
        Image.Image.paste(background, im2, (0,im1.size[1]))
        return background
    else:
        print("Incorrect direction: Pick from [below, above, right, left]")
        return None

def MED_character(str1,str2):
    cost=0
    len1=len(str1)
    len2=len(str2)

    #output the length of other string in case the length of any of the string is zero
    if len1==0:
        return len2
    if len2==0:
        return len1

    accumulator = [[0 for x in range(len2)] for y in range(len1)] #initializing a zero matrix

    # initializing the base cases
    for i in range(0,len1):
        accumulator[i][0] = i;
    for i in range(0,len2):
        accumulator[0][i] = i;

    # we take the accumulator and iterate through it row by row. 
    for i in range(1,len1):
        char1=str1[i]
        for j in range(1,len2):
            char2=str2[j]
            cost1=0
            if char1!=char2:
                cost1=2 #cost for substitution
            accumulator[i][j]=min(accumulator[i-1][j]+1, accumulator[i][j-1]+1, accumulator[i-1][j-1] + cost1 )

    cost=accumulator[len1-1][len2-1]
    return cost

def find_closest_word(word, low, tuples=False):
    score=[]
    if tuples:
        for t in low:
            score.append((t,MED_character(word, t[0])))
    else:
        for w in low:
            score.append((w,MED_character(word, w)))
    score.sort(key=lambda x:x[1])
    return score[0][0]
    
def find_closest_runes(user_input, show_parsed_runes=False):
    user_low=user_input.split(",")
    for i in range(len(user_low)):
        user_low[i]=find_closest_word(user_low[i],runes_low,True)
        
    if show_parsed_runes:
        print(list(map(lambda x:x[0],user_low)))
        
    tuples=list(map(lambda x:x[1],user_low))
    f=list(map(lambda x:x[1][0],user_low))
    formats=[[[0,1,2,3,4,0,2,3,-1,-1,-1],[0,1,2,3,4,0,2,4,-1,-1,-1],[0,1,2,3,4,0,3,4,-1,-1,-1]],[1,3,2]]
    
    for i in range(len(formats[0])):
        if f==formats[0][i]:
            missing_pair=(formats[1][i],5)
            tuples.insert(missing_pair[0]+4, missing_pair)
            return "".join(list(map(lambda x:str(x[1]),tuples)))
    
    #If no return yet it is malformatted
    print("Format of input incorrect")
    return None

def find_closest_items(user_input, show_parsed_items=False):
    user_low=user_input.split(",")
    for i in range(len(user_low)):
        user_low[i]=find_closest_word(user_low[i],items,False)
    
    if show_parsed_items:
        print(user_low)
        
    return user_low

def find_closest_summoners(user_input, show_parsed_summoners=False):
    user_low=user_input.split(",")
    for i in range(len(user_low)):
        user_low[i]=find_closest_word(user_low[i],summoners,False)
    
    if show_parsed_summoners:
        print(user_low)
        
    return user_low