from django.shortcuts import redirect,render
from django.http import HttpResponse
from .models import donarModel
from .forms import addForm

def homepage(request):
    model = donarModel.objects.all()
    return render(request,'index.html',{'model':model})
def add(request):
    form = addForm()
    if request.method == 'POST':
        form = addForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/add')
    return render(request,'add.html',{'forms':form})
def delete(request,id):
    modela =donarModel.objects.get(id=id)
    modela.delete()
    return redirect("/")
def update(request,id):
    addmodel = donarModel.objects.get(id=id)
    addforms = addForm(instance=addmodel)
    if request.method == 'POST':
        addforms= addForm(request.POST,instance=addmodel)
        if addforms.is_valid():
            addforms.save()
            return redirect('/add') 
    return render(request,'update.html',{'addform':addforms})  
