// configure our routes
libraryApp.config(function($routeProvider) {
    $routeProvider

        // route for the home page
        .when('/', {
            templateUrl : 'views/books.html',
            controller  : 'booksController'
        })

        .when('/books', {
            templateUrl : 'views/books.html',
            controller  : 'booksController'
        })

        // route for the contact page
        .when('/settings', {
            templateUrl : 'views/settings.html',
            controller  : 'settingsController'
        });
});
