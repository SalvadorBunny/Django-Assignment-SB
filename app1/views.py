from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def empleados(request):
    data={
        'titulo':'EMPLEADOS',
        'persona1':'Commando',
        'imagen1':'empleados/CommandoPortrait1.png',
        'persona2':'Pilot',
        'imagen2':'empleados/PilotPortrait0.png',
        'persona3':'Loader',
        'imagen3':'empleados/LoaderPortrait0.png',
        'desc1':'Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolorem amet soluta deleniti voluptates veritatis Harum repudiandae odit mollitia iusto voluptatem sunt, iure quae et ullam nulla soluta, adipisci eius aperiam.Aliquid, explicabo ratione? Maiores illo quos neque corrupti vero repellendus aliquam deleniti architecto nostrum quasi consequuntur laudantium suscipit praesentium nam accusantium dolores numquam omnis corporis blanditiis ducimus, perferendis voluptate! Consequatur!',
        'desc2':'Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolorem amet soluta deleniti voluptates veritatis Harum repudiandae odit mollitia iusto voluptatem sunt, iure quae et ullam nulla soluta, adipisci eius aperiam.Aliquid, explicabo ratione? Maiores illo quos neque corrupti vero repellendus aliquam deleniti architecto nostrum quasi consequuntur laudantium suscipit praesentium nam accusantium dolores numquam omnis corporis blanditiis ducimus, perferendis voluptate! Consequatur!',
        'desc3':'Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolorem amet soluta deleniti voluptates veritatis Harum repudiandae odit mollitia iusto voluptatem sunt, iure quae et ullam nulla soluta, adipisci eius aperiam.Aliquid, explicabo ratione? Maiores illo quos neque corrupti vero repellendus aliquam deleniti architecto nostrum quasi consequuntur laudantium suscipit praesentium nam accusantium dolores numquam omnis corporis blanditiis ducimus, perferendis voluptate! Consequatur!',
        'extra1' : 'Guardia',
        'extra2' : 'Piloto',
        'extra3' : 'Maletero'
    }
    return render(request,'informacion.html',data)

def clientes(request):
    data ={
        'titulo':'CLIENTES',
        'persona1':'Enforcer',
        'imagen1':'clientes/EnforcerPortrait0.png',
        'persona2':'Miner',
        'imagen2':'clientes/MinerPortrait0.png',
        'persona3':'Sniper',
        'imagen3':'clientes/SniperPortrait0.png',
        'desc1':'Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolorem amet soluta deleniti voluptates veritatis Harum repudiandae odit mollitia iusto voluptatem sunt, iure quae et ullam nulla soluta, adipisci eius aperiam.Aliquid, explicabo ratione? Maiores illo quos neque corrupti vero repellendus aliquam deleniti architecto nostrum quasi consequuntur laudantium suscipit praesentium nam accusantium dolores numquam omnis corporis blanditiis ducimus, perferendis voluptate! Consequatur!',
        'desc2':'Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolorem amet soluta deleniti voluptates veritatis Harum repudiandae odit mollitia iusto voluptatem sunt, iure quae et ullam nulla soluta, adipisci eius aperiam.Aliquid, explicabo ratione? Maiores illo quos neque corrupti vero repellendus aliquam deleniti architecto nostrum quasi consequuntur laudantium suscipit praesentium nam accusantium dolores numquam omnis corporis blanditiis ducimus, perferendis voluptate! Consequatur!',
        'desc3':'Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolorem amet soluta deleniti voluptates veritatis Harum repudiandae odit mollitia iusto voluptatem sunt, iure quae et ullam nulla soluta, adipisci eius aperiam.Aliquid, explicabo ratione? Maiores illo quos neque corrupti vero repellendus aliquam deleniti architecto nostrum quasi consequuntur laudantium suscipit praesentium nam accusantium dolores numquam omnis corporis blanditiis ducimus, perferendis voluptate! Consequatur!',
        'extra1' : 'Policia',
        'extra2' : 'Minero',
        'extra3' : 'Militar'
    }
    return render(request,'informacion.html',data)

def egresados(request):
    data= {
         'titulo':'EGRESADOS',
        'persona1':'Artificer',
        'imagen1':'egresados/ArtificerPortrait1.png',
        'persona2':'Bandit',
        'imagen2':'egresados/BanditPortrait0.png',
        'persona3':'Mercenary',
        'imagen3':'egresados/MercenaryPortrait0.png',
        'desc1':'Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolorem amet soluta deleniti voluptates veritatis Harum repudiandae odit mollitia iusto voluptatem sunt, iure quae et ullam nulla soluta, adipisci eius aperiam.Aliquid, explicabo ratione? Maiores illo quos neque corrupti vero repellendus aliquam deleniti architecto nostrum quasi consequuntur laudantium suscipit praesentium nam accusantium dolores numquam omnis corporis blanditiis ducimus, perferendis voluptate! Consequatur!',
        'desc2':'Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolorem amet soluta deleniti voluptates veritatis Harum repudiandae odit mollitia iusto voluptatem sunt, iure quae et ullam nulla soluta, adipisci eius aperiam.Aliquid, explicabo ratione? Maiores illo quos neque corrupti vero repellendus aliquam deleniti architecto nostrum quasi consequuntur laudantium suscipit praesentium nam accusantium dolores numquam omnis corporis blanditiis ducimus, perferendis voluptate! Consequatur!',
        'desc3':'Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolorem amet soluta deleniti voluptates veritatis Harum repudiandae odit mollitia iusto voluptatem sunt, iure quae et ullam nulla soluta, adipisci eius aperiam.Aliquid, explicabo ratione? Maiores illo quos neque corrupti vero repellendus aliquam deleniti architecto nostrum quasi consequuntur laudantium suscipit praesentium nam accusantium dolores numquam omnis corporis blanditiis ducimus, perferendis voluptate! Consequatur!',
        'extra1' : 'The high court',
        'extra2' : '???',
        'extra3' : 'MercCo'
    }
    return render(request,'informacion.html',data)