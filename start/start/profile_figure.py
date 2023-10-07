from models import IssueLog
from django.shortcuts import render


def get_figure(request):
    issue_object = IssueLog.objects.all()
    mysolve_rows = issue_object.filter(Username=request.profile.user, usertype='SOLVER')
    citysolve_rows = issue_object.filter(City=request.profile.city, usertype='SOLVER')
    issue_percentage = mysolve_rows.count() / citysolve_rows.count()

    yourissue_solved = (issue_object.filter(Username=request.profile.user, usertype='POSTER')
                        .filter(usertype='SOLVER').values('issue_id').distinct())
    issue_post = issue_object.filter(Username=request.profile.user, usertype='POSTER')
    issue_posted = yourissue_solved / issue_post

    return render(request, 'profile.html', {'issue_percentage': issue_percentage,'issue_posted': issue_posted })
