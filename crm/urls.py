
from django.contrib import admin
from django.urls import path
from launchers import views as launchers_views
from django.conf import settings 
from django.conf.urls.static import static 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('homeexted/',launchers_views.home_demo, name='home extend page'),
    path('mainpage/',launchers_views.homepage,name='home page'),
    path('',launchers_views.login_user,name='home'),
    path('logout/',launchers_views.logout_view,name='home'),
    path('profile/',launchers_views.signup,name='signup'),
    path('info/',launchers_views.local_usersss, name="database user"),
    path('follow/',launchers_views.followsametime,name='follow'),
    path('note/',launchers_views.file_notes,name='notefiles'),
    path('user/',launchers_views.userinfo,name='userinfo'),
    path('today/',launchers_views.todayfollow_up, name='today follow up'),
    path('update/',launchers_views.updateprofile,name='update'),
    path('followup/',launchers_views.followupuser_id,name='followup'),
    path('todayfollowup/',launchers_views.today_followupuser, name='today follow'),
    path('filenote/',launchers_views.filenote,name='filenote'),
    path('break/',launchers_views.break_time, name='Break Start'),
    path('ajax/get_response/', launchers_views.answer_me, name='get_response'),
    path('ajax/stop/', launchers_views.answer, name='stop'),
    path('user_profile/', launchers_views.User_Profiles, name = 'User_Profiles'),
    path('EditFileNote/',launchers_views.edit_file_notes,name='Edit File Notes'),
    path('logs/', launchers_views.admin_page, name='admin page'),
    path('all_logs/', launchers_views.all_user_logs, name=' page'),
    path('password/', launchers_views.changepassword, name='Changepassword'),
    path('file/',launchers_views.home_file, name='weekly file notes'),
    path('editfinfo/',launchers_views.registerpage, name='register page'),
    path('search/',launchers_views.search_user, name='search'),
    path('up/',launchers_views.follow, name='Follow up'),
    path('update_profile/',launchers_views.User_Profiless, name='User Profiless'),
    path('signup/',launchers_views.registers, name='sign up'),
    path('FollowUp/',launchers_views.followsubmit, name='sign up'),
    path('api',launchers_views.ChartData.as_view()),
    path('enquiry/',launchers_views.enquiry, name='enquiry'),
    path('status/',launchers_views.change_status, name='status'),
    path('forgot/',launchers_views.forgotpassword, name='forgot'),
    path('setpassword/',launchers_views.setpassword, name='setpassword'),
    path('application/',launchers_views.change_statuss, name='application'),
    path('apply/',launchers_views.applyed, name='apply'),
    path('applications/',launchers_views.change_statusss, name='applications'),
    path('data.csv/',launchers_views.csv_download_inq, name='data csv'),
    path('lead.csv/',launchers_views.csv_download_Leads, name='data csv'),


    

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
