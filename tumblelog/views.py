# -*- coding: utf-8 -*-
from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView

# model_form 直接从modles构造表单，复用validate信息。
from flask_mongoengine.wtf import model_form

from .models import Post, Comment

posts = Blueprint('posts', __name__, template_folder='templates')


class ListView(MethodView):
    def get(self):
        posts = Post.objects.all()
        return render_template('posts/list.html', posts=posts)


'''
class DetailView(MethodView):

    def get(self, slug):
        post = Post.objects.get_or_404(slug=slug)
        return render_template('posts/detail.html', post=post)
'''


class DetailView(MethodView):
    MyForm = model_form(Comment, exclude=['created_at'])

    def get_context(self, slug):
        post = Post.objects.get_or_404(slug=slug)
        # 创建新的form实例
        form = self.MyForm(request.form)

        context = {
            "post": post,
            "form": form
        }
        return context

    def get(self, slug):
        context = self.get_context(slug)
        return render_template('posts/detail.html', **context)

    def post(self, slug):
        context = self.get_context(slug)
        form = context.get('form')

        if form.validate():
            comment = Comment()

            # 使用form中的数据来更新comment对象
            form.populate_obj(comment)

            post = context.get('post')
            post.comments.append(comment)
            post.save()

            return redirect(url_for('posts.detail', slug=slug))

        return render_template('posts/detail.html', **context)


# Register the urls
posts.add_url_rule('/', view_func=ListView.as_view('list'))
posts.add_url_rule('/<slug>/', view_func=DetailView.as_view('detail'))

# the follow format is ok too
# the endpoint for url_for is posts.detail <= Blueprint(posts).name + View(detail).name
# posts.add_url_rule('/post/<slug>/', view_func=DetailView.as_view('detail'))
