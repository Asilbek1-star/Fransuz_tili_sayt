// static/js/scripts.js
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.video-preview').forEach(video => {
        video.addEventListener('mouseover', () => {
            video.play();
        });
        video.addEventListener('mouseout', () => {
            video.pause();
            video.currentTime = 0;
        });
    });
});