from PIL import Image, ImageDraw, ImageFont
from random import randint


class MemeEngine():
    """The Meme Engine Module is responsible for manipulating
                and drawing text onto images.

    Arguments:
        output_dir {str} -- the folder location for the output images.
    """

    def __init__(self, output_dir: str) -> None:
        self.output_dir = output_dir

    def make_meme(self, img_path: str, text: str,
                  author: str, width: int = 500) -> str:
        """Create a Meme image With a Text Greeting

        Arguments:
            img_path {str} -- the file location for the input image.
            text {str} -- The Quote body to be added to the meme image.
            author {str} -- TThe Quote's author to be added to the meme image.
            width {int} -- The pixel width value. Default=None.
        Returns:
            str -- the file path to the output image.
        """

        with Image.open(img_path) as img:
            # resize image to desired width
            if width:
                ratio = width/float(img.size[0])
                height = int(ratio*float(img.size[1]))
                img = img.resize((width, height), Image.NEAREST)

            # print Quote on meme image
            if (text, author):
                message = f'{text}\n   - {author}'
                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype(
                    'MemeGenerator/fonts/SwedenSansSemiBold.ttf', size=20)
                # randomize text start location; naively try to fit in image
                (x, y) = map(lambda elem: randint(0, elem),
                             (width // 2, int(height / (5/4))))
                draw.multiline_text((x, y), message, font=font, fill='white')

            # save temporary meme image
            tmp = f'{randint(0,1000000)}.jpg'
            out_path = f'{self.output_dir}/{tmp}'
            img.save(out_path)

        return out_path
