//https://scotch.io/tutorials/sort-and-filter-a-table-using-angular
angular.module('sortApp', [])

    .controller('mainController', function($scope, $http) {
        $scope.sortType     = 'name'; // set the default sort type
        $scope.sortReverse  = false;  // set the default sort order
        $scope.searchBook   = '';     // set the default search/filter term
        $scope.editMode  = false;

        $http.get('http://127.0.0.1:5555/books')
            .then(function(res){
                $scope.books = res.data;
                var firstRow = {'id':-1,'writers':'','title':'','series':'','volumes':1,'copies':1,'date_created':new Date()};
                $scope.books.unshift(firstRow);
            });

        $scope.sort = function(sortBy) {
            $scope.sortReverse = !$scope.sortReverse;
            $scope.sortType = sortBy;
        };

        $scope.addRecord = function() {
            $scope.editMode = true;
            $scope.editableRowIndex = 0;
        }

        $scope.editRecord = function(book,index) {
            $scope.editMode = true;
            $scope.editableRowIndex = index;
        }

        $scope.confirmEdit = function(book) {
            if (book.id==-1) {
                //insert
                url = 'http://127.0.0.1:5555/insert_book?w='+book.writers+'&t='+book.title+'&s='+book.series+'&v='+book.volumes+'&c='+book.copies;
                $http.get(url)
                    .then(function(res){
                        $scope.books[0].id = res.data.new_id;
                        var firstRow = {'id':-1,'writers':'','title':'','series':'','volumes':1,'copies':1,'date_created':new Date()};
                        $scope.books.unshift(firstRow);
                    });
            }
            else {
                //update
                url = 'http://127.0.0.1:5555/update_book?i='+book.id+'&w='+book.writers+'&t='+book.title+'&s='+book.series+'&v='+book.volumes+'&c='+book.copies;
                console.log(url);
                $http.get(url)
                    .then(function(res){
                    });
            }
            $scope.editMode = false;
            $scope.editableRowIndex = -1;
        }

        $scope.cancelEdit = function(book) {
            $scope.editMode = false;
            $scope.editableRowIndex = -1;
        }

        $scope.deleteRecord = function(book) {
            if (confirm('אתם בטוחים שברצונכם למחוק את הספר?')) {
            $http.get('http://127.0.0.1:5555/delete_book?id='+book.id)
                .then(function(res){
                    alert('הפעולה בוצעה בהצלחה');
                    var indexToRemove = -1;
                    for (var i=0;i<$scope.books.length;i++)
                    {
                        if ($scope.books[i].id==book.id)
                        {
                            indexToRemove = i;
                            break;
                        }
                    }
                    if (indexToRemove>-1)
                        $scope.books.splice(indexToRemove,1);
                });
            }
        }

    });