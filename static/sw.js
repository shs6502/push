self.addEventListener('push', function(event) {
    const options = {
        body: event.data.text(),
        icon: '/static/icon.png',
        badge: '/static/badge.png'
    };

    event.waitUntil(
        self.registration.showNotification('Push Notification', options)
    );
});

self.addEventListener('notificationclick', function(event) {
    event.notification.close();
    // 알림 클릭시 동작 정의
}); 