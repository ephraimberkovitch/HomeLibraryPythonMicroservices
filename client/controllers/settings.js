libraryApp.controller('settingsController', function($scope, $http) {
    $scope.id = "מספר";
    $scope.authors = "מחבר/מחברים";
    $scope.title = "כותרת";
    $scope.series = "סדרה";
    $scope.volumes = "כרכים";
    $scope.copies = "עותקים";
    $scope.owned = "אצל אלי";
    $scope.young = "לקטנים";
    $http.get(settings_url+'/settings')
        .then(function(res){
            $scope.books = res.data;
        });
    $scope.update = function(field) {
         url = settings_url+'/update_setting?i='+book.id;
         $http.get(url)
            .then(function(res) {
            });
   };
});
