import img2pdf
import argparse, os


def img2pdf_converter(images, path, save = False):
    list_of_files = os.listdir(os.getcwd())
    images = []
    for item in list_of_files:
        if item.endswith('.jpg'):
            images.append(item)
    sorted_images = sorted(images)
    pdf = img2pdf.convert(sorted_images)

    if save:
        with open("img2pdf.pdf","wb") as f:
            f.write(pdf)


    return pdf





if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--images', required=True, help = 'list of image names')
    parser.add_argument('--path', required=False, type = str, help = 'path to save pdf')
    parser.add_argument('--save', dest='save', action='store_true')
    parser.set_defaults(save=False)
    args = parser.parse_args()
    img2pdf_converter(args.images, args.path, args.save)