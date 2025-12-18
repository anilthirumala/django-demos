from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
# sample data
posts = [{'id':1,'title':'First Post','content':'This is the content of the first post.'},
            {'id':2,'title':'Second Post','content':'This is the content of the second post.'}]

def home(request):
    html = ""
    for post in posts:
        html += f"<div><h2>{post['title']}</h2><p>{post['content']}</p></div>"
    return HttpResponse(html)

# return one post at a time
def post_detail(request, post_id):
    post = next((post for post in posts if post['id'] == post_id), None)
    if post:
        html = f"<div><h2>{post['title']}</h2><p>{post['content']}</p></div>"
        return HttpResponse(html)
    else:
        return HttpResponse("<h2>Post not found</h2>", status=404)
    
def about(request):
    return render(request, 'about.html',{'company':'MyCompany', 'year':2024})

def contact(request):
    return render(request, 'contact.html')