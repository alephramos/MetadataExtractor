import argparse,os
from PIL import Image
from PIL.ExifTags import TAGS

# MetadaExtractor
# By: @UnaPibageek
# Last change: @a_l_e_p_h



def readMetadata(image):
    img = Image.open(image)
    exif = img._getexif()
    print("Results for "+image)
    try:
        for (k, v) in exif.iteritems():
            print '%s = %s'%(TAGS.get(k), v)
    except:
        print "Metadata not found!"

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='MetadataExtractor',usage='%(prog)s [options]')
    parser.add_argument('-i', '--image',
      required=False, type=str, help='Image')

    parser.add_argument('-d', '--directory',
      required=False, type=str, help='Directory')


    args = parser.parse_args()
    if args.directory and args.image:
        print("Only can use -i --image or -d --directory but not both")
    else:
        if args.image:
            readMetadata(args.image)
        elif args.directory:
            try:
                filenames = next(os.walk(args.directory))[2]
                for filename in filenames:
                    try:
                        img = Image.open(filename)
                        readMetadata(filename)
                    except:
                        print(filename+" is not a valid Image")
            except:
                print(args.directory + " is not a valid directory")