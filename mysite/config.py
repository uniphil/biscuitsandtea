from mysite import app

app.config.update({
    'POSTS_FOLDER': 'markdown',
    'MEDIA_FOLDER': 'media',
    'MEDIA_URL': '/media/',
})
