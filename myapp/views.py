from django.http import HttpResponse

def chat_links(request):
    return HttpResponse("""
<!DOCTYPE html>
<html>
<head>
    <title>Useful Links</title>
    <!-- Include Bootstrap CSS from a CDN -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <style>
        body {
            display: flex;
            height: 100vh;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            background-color: #f8f9fa;
            margin: 0;
        }
        .btn-main {
            margin: 5px; /* Spacing between buttons */
        }
    </style>
</head>
<body>
    <div class="container text-center">
    
        <h1 class="h3 mb-3 fw-normal">Useful Links</h1>
         <div class="btn-group-vertical" role="group">
            <a href="https://platform.openai.com/assistants" class="btn btn-primary btn-lg my-2" role="button">Assistants</a>
            <a href="https://openai.com/" class="btn btn-secondary btn-lg my-2" role="button">OpenAI</a>
            <a href="https://platform.openai.com/usage" class="btn btn-success btn-lg my-2" role="button">Usage</a>
            <a href="https://chat.openai.com/" class="btn btn-info btn-lg my-2" role="button">Chat</a>
        </div>
    </div>
</body>
</html>
""")

def index(request):
    return HttpResponse("""
<!DOCTYPE html>
<html>
<head>
    <title>Local Links</title>
    <!-- Include Bootstrap CSS from a CDN -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <style>
        body {
            display: flex;
            height: 100vh;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            background-color: #f8f9fa;
            margin: 0;
        }
        .btn-main {
            margin: 5px; /* Spacing between buttons */
        }
    </style>
</head>
<body>
    <div class="container text-center">
        <h1 class="mb-4">Server Running</h1>
        <p class="mb-4">Here are some links</p>
        <div class="btn-group-vertical" role="group">
            <a href="http://localhost:8000/admin/" class="btn btn-primary btn-lg btn-main" role="button">Admin</a>
            <a href="http://localhost:8000/chat/" class="btn btn-secondary btn-lg btn-main" role="button">Open AI Resources</a>
        </div>
    </div>
</body>
</html>
""")