//https://scotch.io/tutorials/sort-and-filter-a-table-using-angular
angular.module('sortApp', [])

    .controller('mainController', function($scope, $http) {
        $scope.sortType     = 'name'; // set the default sort type
        $scope.sortReverse  = false;  // set the default sort order
        $scope.searchFish   = '';     // set the default search/filter term

        // create the list of sushi rolls
        /*$scope.sushi = [
            { name: 'Cali Roll', fish: 'Crab', tastiness: 2 },
            { name: 'Philly', fish: 'Tuna', tastiness: 4 },
            { name: 'Tiger', fish: 'Eel', tastiness: 7 },
            { name: 'Rainbow', fish: 'Variety', tastiness: 6 }
        ];*/

        $http.get('sushi.json')
            .then(function(res){
                $scope.sushi = res.data.sushi;
            });

        $scope.sort = function(sortBy) {
            $scope.sortReverse = !$scope.sortReverse;
            $scope.sortType = sortBy;
        };

    });