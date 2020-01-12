from django.urls import path

from . import views

urlpatterns = [

    # articles/正の整数(西暦年でビュー関数にyear変数で引き継がれる)/の場合viewsモジュールのyear_archiveメソッドがコールされる
    
    path('articles/<int:year>/', views.year_archive),
    path('articles/<int:year>/<int:month>', views.month_archive),
    # path('articles/<int:month>/<int:pk>/', views.article_detail),
]

 #第一引数はURLパターン、第二引数にはviewsモジュールのビュー関数を指定してURLパターンとビュー関数を紐づける、<int:year>は任意の正の整数と合致することを意味する、合致すると指定した変数に格納されるビュー関数は後で作成

 
 
 # ex.二行目はarticles/正の西暦年/正の月/(ビュー関数にyear変数/month変数で引き継がれる)の場合viewsモジュールのmonth_archiveメソッドがコールされる

 # ex.三行目はarticles/正の西暦年/正の月/正の整数
 #(ビュー関数にyear変数/month変数/pk変数で引き継がれる)の場合viewsモジュールのarticle_detailメソッドがコールされる

# 要求したURLパターンで停止し、紐づいたビュー関数をコールする、URLパターンの可変部分はメソッドの引数として引き継がれる
