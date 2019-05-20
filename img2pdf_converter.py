import os
import img2pdf
import argparse


def img2pdf_converter(images, path, save = False):

    pdf_result = img2pdf.convert(images)

    if save:
        with open(os.path.join(path,"img2pdf.pdf"),"w") as f:
            f.write()


    return pdf_result





if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--images', required=True, help = 'list of image names')
    parser.add_argument('--path', required=False, type = str, help = 'path to save pdf')
    parser.add_argument('--save', dest='save', action='store_true')
    parser.set_defaults(save=False)
    args = parser.parse_args()
    img2pdf_converter(args.images, args.path, args.save)