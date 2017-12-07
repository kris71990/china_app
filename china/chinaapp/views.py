from django.shortcuts import render
from django.http import Http404
from chinaapp.models import Region, Province, Municipality, Aut_reg, Adm_reg

def index(request):
    return render(request, 'index.html')

def region_detail(request, id):
    try:
        region = Region.objects.get(id=id)
    except Region.DoesNotExist:
        raise Http404('This item does not exist')

    prov = Province(region.region_name)
    prov_info = prov.get_prov_info(region.region_name)
    wiki = prov.get_wiki(region.region_name)
    largest_city = prov_info.get('Largest city', 'Not Available')
    chinese = prov_info.get('Chinese', 'Not Available')
    density = prov_info.get('density', 'Not Available')

    return render(request, 'region_detail.html', {
        'region_name': region.region_name,
        'region_type': region.region_type,
        'prov_info': prov_info,
        'chinese': chinese,
        'density': density,
        'density_rank': prov_info['Densityrank'],
        'population': prov_info['Total'],
        'pop_rank': prov_info['Rank'],
        'governor': prov_info['Governor'],
        'secretary': prov_info['Secretary'],
        'abbrev': prov_info['Abbreviation'],
        'languages': prov_info['Languages and dialects'],
        'divisions': prov_info['Divisions'],
        'ethnic': prov_info['Ethnic composition'],
        'gdp': prov_info[' per capita'],
        'largest_city': largest_city,
        'wiki': wiki,
        'id': id
    })

def muni_detail(request, id):
    try:
        region = Region.objects.get(id=id)
    except Region.DoesNotExist:
        raise Http404('This item does not exist')

    muni = Municipality(region.region_name)
    muni_info = muni.get_muni_info(region.region_name)
    wiki = muni.get_wiki(region.region_name)

    return render(request, 'muni_detail.html', {
        'region_name': region.region_name,
        'region_type': region.region_type,
        'muni_info': muni_info
    })

def aut_reg_detail(request, id):
    try:
        region = Region.objects.get(id=id)
    except Region.DoesNotExist:
        raise Http404('This item does not exist')

    aut_reg = Aut_reg(region.region_name)
    aut_reg_info = aut_reg.get_aut_reg_info(region.region_name)
    wiki = aut_reg.get_wiki(region.region_name)

    return render(request, 'aut_reg_detail.html', {
        'region_name': region.region_name,
        'region_type': region.region_type,
        'aut_reg_info': aut_reg_info
    })

def adm_reg_detail(request, id):
    try:
        region = Region.objects.get(id=id)
    except Region.DoesNotExist:
        raise Http404('This item does not exist')
    
    adm_reg = Adm_reg(region.region_name)
    adm_reg_info = adm_reg.get_adm_reg_info(region.region_name)
    wiki = adm_reg.get_wiki(region.region_name)

    return render(request, 'adm_reg_detail.html', {
        'region_name': region.region_name,
        'region_type': region.region_type,
        'adm_reg_info': adm_reg_info
    })


