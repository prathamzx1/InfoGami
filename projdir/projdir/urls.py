"""projdir URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from app.views import login_view,register_view,logout_view,index,about_view
from app.codehub import codehub_question,remove_codehub_question,edit_codehub_question,codehub,codehub_topic,edit_topic,remove_topic,comment_on_topic,search_topic,remove_topic_comment,edit_topic_comment,codehub_question_details,remove_codehub_question_comment,edit_codehub_question_comment,search_question,codehub_innovation,codehub_innovation_details,edit_codehub_innovation_idea,remove_codehub_innovation_idea,edit_codehub_innovation_idea_comment,remove_codehub_innovation_idea_comment,search_codehub_innovation_post,get_all_codehub_topics,get_all_codehub_questions
from app.users import get_users,user_profile,edit_user_profile,get_user_questions,get_user_topics,user_blog,follow_user_profile,get_user_new_ideas,get_codehub_user_events,unfollow_user_profile,get_user_notifications,get_following_users,get_users_followed,user_new_messages_api,get_user_messages,post_message_api,set_message_status_true_api,fetch_user_messages_message_center_api,get_message_center,get_message_center_data_api,save_user_social_accounts,edit_user_social_accounts
from app.create_event import codehub_events,create_codehub_event,edit_codehub_event,remove_codehub_event,codehub_event_details,remove_codehub_event_question,edit_codehub_event_question,search_codehub_event,propose_event,propose_event_details,upVote_propose_event,downVote_propose_event,propose_event_users_upvoted,propose_event_users_downvoted,edit_propose_event,remove_propose_event,search_propose_event,get_all_proposed_events,edit_suggestion_to_propose_event,remove_suggestion_to_propose_event
from app.music import music_list
from app.match_skill import match_user_skills,search_users_by_skill,get_all_skills_stat,get_all_skills_stat_apiv1,get_user_skills_stat_apiv1
from app.tags import tags
from app.host_project import work_collaborately,host_project,get_all_hosted_projects,hosted_project_details,edit_hosted_project,remove_hosted_project,activate_hosted_project,deactivate_hosted_project,skill_matched_hosted_project,user_hosted_projects,ping_hosted_project,hosted_project_interested_users,search_hosted_project,accept_hosted_project_request,reject_hosted_project_request,edit_hosted_project_query,remove_hosted_project_query


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^markitup/', include('markitup.urls')),
    url('^markdown/', include( 'django_markdown.urls')),
    url(r'^$',index,name = 'index'),
    url(r'^auth/login/$',login_view,name='login_view'),
    url(r'^auth/about/$',about_view,name='about_view'),
    url(r'^auth/register/$',register_view,name='register_view'),
    url(r'^auth/logout/$',logout_view,name='logout_view'),
    url(r'^codehub/$',codehub,name='codehub'),
    url(r'^codehub/topic/$',codehub_topic,name = 'codehub_topic'),
    url(r'^codehub/topic/edit/(?P<id>\d+)/$',edit_topic,name = 'edit_topic'),
    url(r'^codehub/topic/remove/(?P<id>\d+)/$',remove_topic,name = 'remove_topic'),
    url(r'^codehub/topic/(?P<id>\d+)/comment/$',comment_on_topic,name = 'comment_on_topic'),
    url(r'^codehub/topic/search_topic/$',search_topic,name = 'search_topic'),
    url(r'^codehub/topic/comment/(?P<id>\d+)/remove/$',remove_topic_comment,name = 'remove_topic_comment'),
    url(r'^codehub/topic/comment/(?P<id>\d+)/edit/$',edit_topic_comment,name = 'edit_topic_comment'),
    url(r'^codehub/all_topics/$',get_all_codehub_topics,name = 'get_all_codehub_topics'),
    url(r'^users/$',get_users,name='get_users'),
    url(r'^tags/$',tags,name = 'tags'),
    #user profile
    url(r'^user/profile/(?P<user_id>\d+)/$',user_profile,name = 'user_profile'),
    url(r'^user/profile/(?P<user_id>\d+)/edit/$',edit_user_profile,name = 'edit_user_profile'),
    url(r'^user/profile/(?P<user_id>\d+)/follow$',follow_user_profile,name = 'follow_user_profile'),
    url(r'^user/profile/(?P<user_id>\d+)/unfollow$',unfollow_user_profile,name = 'unfollow_user_profile'),
    url(r'^codehub/events/$',codehub_events,name = 'codehub_events'),
    url(r'^codehub/event/(?P<event_id>\d+)/details/$',codehub_event_details,name = 'codehub_event_details'),
    url(r'^codehub/event/create$',create_codehub_event,name = 'create_codehub_event'),
    url(r'^codehub/event/(?P<event_id>\d+)/edit/$',edit_codehub_event,name = 'edit_codehub_event'),
    url(r'^codehub/event/(?P<event_id>\d+)/remove/$',remove_codehub_event,name = 'remove_codehub_event'),
    url(r'^codehub/event/question/(?P<ques_id>\d+)/remove/$',remove_codehub_event_question,name = 'remove_codehub_event_question'),
    url(r'^codehub/event/question/(?P<ques_id>\d+)/edit/$',edit_codehub_event_question,name = 'edit_codehub_event_question'),
    url(r'^codehub/event/search_event/$',search_codehub_event,name = 'search_codehub_event'),
    url(r'^music/$',music_list,name = 'music_list'),
    url(r'^codehub/question/$',codehub_question,name = 'codehub_question'),
    url(r'^codehub/question/search_question/$',search_question,name = 'search_question'),
    url(r'^codehub/question/(?P<ques_id>\d+)/details/$',codehub_question_details,name = 'codehub_question_details'),
    url(r'^codehub/question/(?P<ques_id>\d+)/remove/$',remove_codehub_question,name = 'remove_codehub_question'),
    url(r'^codehub/question/(?P<ques_id>\d+)/edit/$',edit_codehub_question,name = 'edit_codehub_question'),
    url(r'^codehub/question/answer/(?P<ans_id>\d+)/remove/$',remove_codehub_question_comment,name = 'remove_codehub_question_comment'),
    url(r'^codehub/question/answer/(?P<ans_id>\d+)/edit/$',edit_codehub_question_comment,name = 'edit_codehub_question_comment'),
    url(r'^codehub/all_questions/$',get_all_codehub_questions,name = 'get_all_codehub_questions'),
    #storing user profile api
    url(r'^user/social-accounts/save', save_user_social_accounts, name = 'save_user_social_accounts'),
    url(r'^user/social-accounts/edit', edit_user_social_accounts, name = 'edit_user_social_accounts'),
    #user's specific
    url(r'^notifications/',get_user_notifications,name = 'notifications'),
    url(r'^user/(?P<user_id>\d+)/topics/$',get_user_topics,name = 'get_user_topics'),
    url(r'^user/(?P<user_id>\d+)/questions/$',get_user_questions,name = 'get_user_questions'),
    url(r'^user/(?P<user_id>\d+)/blog/$',user_blog,name = 'user_blog'),
    url(r'^user/(?P<user_id>\d+)/new-ideas/$',get_user_new_ideas,name = 'get_user_new_ideas'),
    url(r'^user/(?P<user_id>\d+)/codehub-events/$',get_codehub_user_events,name = 'get_codehub_user_events'),
    url(r'^user/(?P<user_id>\d+)/following-users/$',get_following_users,name = 'get_following_users'),
    url(r'^user/(?P<user_id>\d+)/users-followed/$',get_users_followed,name = 'get_users_followed'),
    url(r'^user/messages/$',get_user_messages,name = 'get_user_messages'),
    url(r'^user-new-messages/$',user_new_messages_api,name = 'user_new_messages_api'),
    url(r'^post-message-api/$',post_message_api,name = 'post_message_api'),
    url(r'^set-message-status-true-api/$',set_message_status_true_api,name = 'set_message_status_true_api'),
    #message center apis
    url(r'^message-center/$',get_message_center,name = 'get_message_center'),
    url(r'^get-message-center-data/api/$',get_message_center_data_api,name = 'get_message_center_data_api'),
    url(r'^message-center/user/(?P<sender_id>\d+)/messages/api/$', fetch_user_messages_message_center_api, name = 'fetch_user_messages_message_center_api'),
    #message center apis end here
    url(r'^blog/',include('app.blog_urls')),
    url(r'^codehub/innovation/$',codehub_innovation,name = 'codehub_innovation'),
    url(r'^codehub/innovation/(?P<idea_id>\d+)/details/$',codehub_innovation_details,name = 'codehub_innovation_details'),
    url(r'^codehub/innovation/(?P<idea_id>\d+)/edit/$',edit_codehub_innovation_idea,name = 'edit_codehub_innovation_idea'),
    url(r'^codehub/innovation/(?P<idea_id>\d+)/remove/$',remove_codehub_innovation_idea,name = 'remove_codehub_innovation_idea'),
    url(r'^codehub/innovation/(?P<idea_id>\d+)/comment/(?P<com_id>\d+)/edit/$',edit_codehub_innovation_idea_comment,name = 'edit_codehub_innovation_idea_comment'),
    url(r'^codehub/innovation/(?P<idea_id>\d+)/comment/(?P<com_id>\d+)/remove/$',remove_codehub_innovation_idea_comment,name = 'remove_codehub_innovation_idea_comment'),
    url(r'^codehub/innovation/search_post/$',search_codehub_innovation_post,name = 'search_codehub_innovation_post'),
    #skill matchinng routes comes here
    url(r'^match-user-skills/$',match_user_skills,name = 'match_user_skills'),
    url(r'^match-user-skills/(?P<skill_slug_str>[\w\-]+)/users/$',search_users_by_skill,name = 'search_users_by_skill'),
    url(r'^match-user-skills/skills-stat/$',get_all_skills_stat,name = 'get_all_skills_stat'),
    #api for skills
    url(r'get-all-skills-stat-api/v1/$',get_all_skills_stat_apiv1,name = 'get_all_skills_stat_apiv1'),
    url(r'get-user-skills-stat-api/v1/(?P<user_id>\d+)/$',get_user_skills_stat_apiv1,name = 'get_user_skills_stat_apiv1'),
    #developers out there
    url(r'^developer-section/',include('app.devhub_urls')),
    #propose event routtes
    url(r'^event/propose-event/$',propose_event,name = 'propose_event'),
    url(r'^event/propose-event/(?P<event_id>\d+)/details/$',propose_event_details,name = 'propose_event_details'),
    url(r'^event/propose-event/(?P<event_id>\d+)/upVote/$',upVote_propose_event,name = 'upVote_propose_event'),
    url(r'^event/propose-event/(?P<event_id>\d+)/downVote/$',downVote_propose_event,name = 'downVote_propose_event'),
    url(r'^event/propose-event/(?P<event_id>\d+)/users-upvoted/$',propose_event_users_upvoted,name = 'propose_event_users_upvoted'),
    url(r'^event/propose-event/(?P<event_id>\d+)/users-downvoted/$',propose_event_users_downvoted,name = 'propose_event_users_downvoted'),
    url(r'^event/propose-event/(?P<event_id>\d+)/edit/$',edit_propose_event,name = 'edit_propose_event'),
    url(r'^event/propose-event/(?P<event_id>\d+)/remove/$',remove_propose_event,name = 'remove_propose_event'),
    url(r'^event/propose-event/search-event/$',search_propose_event,name = 'search_propose_event'),
    url(r'^event/propose-event/all-events/$',get_all_proposed_events,name = 'get_all_proposed_events'),
    url(r'^event/propose-event/(?P<event_id>\d+)/suggestion/(?P<sugg_id>\d+)/edit/$',edit_suggestion_to_propose_event,name = 'edit_suggestion_to_propose_event'),
    url(r'^event/propose-event/(?P<event_id>\d+)/suggestion/(?P<sugg_id>\d+)/remove/$',remove_suggestion_to_propose_event,name = 'remove_suggestion_to_propose_event'),
    # work collaborately and hosting a project
    url(r'^project/',include('app.host_project_urls')),
    #queries for the autocomplete
    # url(r'^devhubQuestion_autocomplete/$',DevhubQuestionAutoComplete.as_view(),name = 'devhubQuestion_autocomplete'),
    url(r'^theInfo/',include('app.the_info_urls')),
    url(r'^general-question/',include('app.general_question_urls')),
    url(r'^group/',include('app.create_group_urls')),
]
if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
