from django.shortcuts import render, redirect, get_object_or_404
from .models import Noticia, MarquetingVideo, MarquetingFoto, Cancion, Video, Foto, Resena, Contratacion, Contacto, Eslogan, Estrellas
from .forms import ResenaForm


def index(request):
    """La pagina de inicio para La Voz del Mariachy"""
    calific=get_object_or_404(Estrellas, id=1)
    if request.method != 'POST':
        form=ResenaForm()
        noticias=Noticia.objects.all().order_by('-fecha')
        marquetings_video=MarquetingVideo.objects.all().order_by('-fecha')
        marquetings_foto=MarquetingFoto.objects.all().order_by('-fecha')
        canciones=Cancion.objects.all().order_by('-fecha')
        videos=Video.objects.all().order_by('-fecha')
        fotos=Foto.objects.all().order_by('-fecha')
        contratacion=Contratacion.objects.all()
        contactos=Contacto.objects.all().order_by('-fecha')
        eslogans=Eslogan.objects.all().order_by('-fecha')
    else:
        form=ResenaForm(data=request.POST)
        if form.is_valid():
            form.save()
            resenas=Resena.objects.all()
            valor=sum(r.calificacion for r in resenas)/len(resenas) if resenas else 0
            calificacion=round(valor, 1)
            calificacion_aprox=round(valor)
            cantidad=len(resenas)
            calific.calificacion=calificacion
            calific.calificacion_aprox=calificacion_aprox
            calific.cantidad=cantidad
            calific.save()
            return redirect('mexicano:index')
    context={
        'noticias':noticias,
        'marquetings_video':marquetings_video,
        'marquetings_foto':marquetings_foto,
        'canciones':canciones,
        'videos':videos,
        'fotos':fotos,
        'contratacion':contratacion,
        'contactos':contactos,
        'eslogans':eslogans,
        'form':form,
        'calificacion':calific,
    }
    return render(request, 'mexicano/index.html', context)

def noticias(request):
    eslogans=Eslogan.objects.all().order_by('-fecha')
    noticias=Noticia.objects.all().order_by('-fecha')
    context={'noticias':noticias, 'eslogans':eslogans}
    return render(request, 'mexicano/noticias.html', context)

def resenas(request):
    eslogans=Eslogan.objects.all().order_by('-fecha')
    resenas=Resena.objects.all().order_by('-fecha')
    context={'resenas':resenas, 'eslogans':eslogans}
    return render(request, 'mexicano/resenas.html', context)

def imagen(request, foto_id):
    imagen=Foto.objects.get(id=foto_id)
    context={
        'imagen':imagen,
    }
    return render(request, 'mexicano/imagen.html', context)

def proxima_imagen(request, img_id, proxima):
    imagen_actual=Foto.objects.get(id=img_id)
    fecha_actual=imagen_actual.fecha
    if proxima=='true':
        proxima_img=Foto.objects.filter(fecha__gt=fecha_actual).order_by('fecha').first()
        if proxima_img:
            context={
                'imagen':proxima_img,
            }
            return render(request, 'mexicano/imagen.html', context)
        else:
            context={
                'imagen':imagen_actual,
            }
            return render(request, 'mexicano/imagen.html', context)
    elif proxima=='false':
        img_anterior=Foto.objects.filter(fecha__lt=fecha_actual).order_by('-fecha').first()
        if img_anterior:
            context={
                'imagen':img_anterior,
            }
            return render(request, 'mexicano/imagen.html', context)
        else:
            context={
                'imagen':imagen_actual,
            }
            return render(request, 'mexicano/imagen.html', context)

def proximo_video(request, vid_id, proxima):
    video_actual=Video.objects.get(id=vid_id)
    fecha_actual=video_actual.fecha
    if proxima=='true':
        proximo_vid=Video.objects.filter(fecha__gt=fecha_actual).order_by('fecha').first()
        if proximo_vid:
            context={
                'video':proximo_vid,
            }
            return render(request, 'mexicano/video.html', context)
        else:
            context={
                'video':video_actual,
            }
            return render(request, 'mexicano/video.html', context)
    elif proxima=='false':
        vid_anterior=Video.objects.filter(fecha__lt=fecha_actual).order_by('-fecha').first()
        if vid_anterior:
            context={
                'video':vid_anterior,
            }
            return render(request, 'mexicano/video.html', context)
        else:
            context={
                'video':video_actual,
            }
            return render(request, 'mexicano/video.html', context)

def video(request, video_id):
    video=Video.objects.get(id=video_id)
    context={
        'video':video,
    }
    return render(request, 'mexicano/video.html', context)