//https://scotch.io/tutorials/sort-and-filter-a-table-using-angular
var books_url = 'http://127.0.0.1:5555';
var settings_url = 'http://127.0.0.1:5556';

var libraryApp = angular.module('libraryApp', ['ngRoute']);

libraryApp.filter('urlencode', function() {
  return function(input) {
    return window.encodeURIComponent(input);
  }
});


