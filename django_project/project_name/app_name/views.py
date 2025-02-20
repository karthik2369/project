from django.shortcuts import render

def youtube_stats_view(request):
    # Render the uploaded HTML template
    return render(request, 'youtube_stat_extractor.html')
