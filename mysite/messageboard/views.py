from django.shortcuts import render
from .models import MsgPost

# Create your views here.
def index(request):
	msg_list = MsgPost.objects.all()
	for i in range(len(msg_list)):
		msg = msg_list[i]
		msg.datetime = msg.datetime.strftime('%Y-%m-%d %H:%M:%S')
		msg.index = len(msg_list)-i
	context = {'msg_list':msg_list}
	return render(request,'messageboard/index.html',context)
	
def msgCreate(request):
	content = request.POST['content']
	msg = MsgPost(content=content)
	msg.save()
	return index(request)