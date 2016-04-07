from django.shortcuts import render
from .models import carousel,event,Film_link,Website_caption,Contact_info,FAQ,Visiter_message
# Create your views here.

def index(request):
    cs = carousel.objects.filter()
    json = []
    for c in cs:
        c_text = c.carousel_text
        c_im = c.carousel_pic.__str__().replace('mainapp/static/','')
        #print(c_im,'\r\n')
        json.append([c.carousel_header,c_text,c_im])
        
    ev = event.objects.filter()
    jsonev = []
    for e in ev:
        e_pic = e.event_pic.__str__().replace('mainapp/static/','')
        jsonev.append([e.event_name,e.event_text,e_pic])
    #get data from Film_link
    fi = Film_link.objects.filter()
    jsonfi = []
    for f in fi:
        jsonfi.append(f.videolink)
        
    #get contact info
    cts = Contact_info.objects.filter()
    jsonct = []
    for ct in cts:
        jsonct.append([ct.name,ct.phone,ct.email,ct.address,ct.facebook,ct.youtube,ct.position_lat,ct.position_lon])
        
    
    return render(request, 'mainapp/index.html',{'carouseldat':json,'eventdat':jsonev,'videodat':jsonfi,'contactdat':jsonct,},)