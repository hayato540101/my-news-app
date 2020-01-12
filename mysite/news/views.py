from django.shortcuts import render

from .models import Article
# Create your views here.
def year_archive(request, year):
    # Aricleモデルをpub_dateフィールドの年が引数のyear変数と一致するという条件で検索しインスタンスリストを取得する
    a_list = Article.objects.filter(pub_date__year=year)
    
    # 辞書型のcontext変数に西暦年と検索結果を入れ込んでいる
    context = {'year':year, 'article_list':a_list}

    # renderメソッドを実行しリターン
    # renderメソッドは第二引数で指定したhtmlテンプレートと第三引数で指定したcontext変数でhtmlを生成する、生成したhtmlはhtmlレスポンスに乗せてブラウザに送信する
    return render(request, 'news/year_archive.html', context)



