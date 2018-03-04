from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.response import TemplateResponse
import os
from PIL import Image
import zipfile
import io
import datetime
import shutil


ZIP_MAIN_NAME = 'assets'
ZIP_FILENAME = '%s.zip' % ZIP_MAIN_NAME
SIZE_DICT = {
    'xxxhdpi': 1.0000,
    'xxhdpi' : 0.7500,
    'xhdpi'  : 0.5000,
    'hdpi'   : 0.3750,
    'mdpi'   : 0.2500,
    'ldpi'   : 0.1875
}


def home(request):
    if request.user.is_authenticated:
        if request.method == 'POST' and request.FILES.get('sourcefile', False):
            time_stamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            source_file = request.FILES['sourcefile']
            fs = FileSystemStorage()
            filename = fs.save(source_file.name, source_file)
            uploaded_file_url = fs.url(filename)
            filepath = os.path.join(settings.MEDIA_ROOT ,filename)

            img = Image.open(filepath)
            img_width = img.size[0]
            img_height = img.size[1]

            (img_ldpi, img_mdpi, img_hdpi, img_xhdpi, img_xxhdpi, img_xxxhdpi) = get_images(img, img_width, img_height)

            (zip_ldpi, zip_mdpi, zip_hdpi, zip_xhdpi, zip_xxhdpi, zip_xxxhdpi) = get_folder_names()

            main_save_path     = os.path.join(settings.MEDIA_ROOT, time_stamp)
            ldpi_save_path     = os.path.join(main_save_path, zip_ldpi)
            mdpi_save_path     = os.path.join(main_save_path, zip_mdpi)
            hdpi_save_path     = os.path.join(main_save_path, zip_hdpi)
            xhdpi_save_path    = os.path.join(main_save_path, zip_xhdpi)
            xxhdpi_save_path   = os.path.join(main_save_path, zip_xxhdpi)
            xxxhdpi_save_path  = os.path.join(main_save_path, zip_xxxhdpi)

            os.makedirs(ldpi_save_path, exist_ok=True)
            os.makedirs(mdpi_save_path, exist_ok=True)
            os.makedirs(hdpi_save_path, exist_ok=True)
            os.makedirs(xhdpi_save_path, exist_ok=True)
            os.makedirs(xxhdpi_save_path, exist_ok=True)
            os.makedirs(xxxhdpi_save_path, exist_ok=True)

            img_ldpi.save(os.path.join(ldpi_save_path, filename))
            img_mdpi.save(os.path.join(mdpi_save_path, filename))
            img_hdpi.save(os.path.join(hdpi_save_path, filename))
            img_xhdpi.save(os.path.join(xhdpi_save_path, filename))
            img_xxhdpi.save(os.path.join(xxhdpi_save_path, filename))
            img_xxxhdpi.save(os.path.join(xxxhdpi_save_path, filename))

            s = io.BytesIO()
            zf = zipfile.ZipFile(s, 'w')
            zf.write(os.path.join(ldpi_save_path, filename), os.path.join(os.path.join(ZIP_MAIN_NAME, zip_ldpi), filename))
            zf.write(os.path.join(mdpi_save_path, filename), os.path.join(os.path.join(ZIP_MAIN_NAME, zip_mdpi), filename))
            zf.write(os.path.join(hdpi_save_path, filename), os.path.join(os.path.join(ZIP_MAIN_NAME, zip_hdpi), filename))
            zf.write(os.path.join(xhdpi_save_path, filename), os.path.join(os.path.join(ZIP_MAIN_NAME, zip_xhdpi), filename))
            zf.write(os.path.join(xxhdpi_save_path, filename), os.path.join(os.path.join(ZIP_MAIN_NAME, zip_xxhdpi), filename))
            zf.write(os.path.join(xxxhdpi_save_path, filename), os.path.join(os.path.join(ZIP_MAIN_NAME, zip_xxxhdpi), filename))
            zf.close()

            shutil.rmtree(main_save_path)

            resp = HttpResponse(s.getvalue(), content_type="application/x-zip-compressed")
            resp['Content-Disposition'] = 'attachment; filename=%s' % ZIP_FILENAME

            return resp
        return render(request, 'home.html')
    return render(request, 'home.html')


def get_images(img, img_width, img_height):
    return (
        img.resize((int(img_width*SIZE_DICT['ldpi']), int(img_height*SIZE_DICT['ldpi']) ), Image.ANTIALIAS),
        img.resize((int(img_width*SIZE_DICT['mdpi']), int(img_height*SIZE_DICT['mdpi']) ), Image.ANTIALIAS),
        img.resize((int(img_width*SIZE_DICT['hdpi']), int(img_height*SIZE_DICT['hdpi']) ), Image.ANTIALIAS),
        img.resize((int(img_width*SIZE_DICT['xhdpi']), int(img_height*SIZE_DICT['xhdpi']) ), Image.ANTIALIAS),
        img.resize((int(img_width*SIZE_DICT['xxhdpi']), int(img_height*SIZE_DICT['xxhdpi']) ), Image.ANTIALIAS),
        img
    )


def get_folder_names():
    return (
        'drawable-ldpi',
        'drawable-mdpi',
        'drawable-hdpi',
        'drawable-xhdpi',
        'drawable-xxhdpi',
        'drawable-xxxhdpi'
    )
