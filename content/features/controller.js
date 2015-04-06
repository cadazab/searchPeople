function Test($scope,$http){
	console.log("Hello from Test Controller");
	$scope.message = "Dulsberg is the New Chanze";

	$scope.search = function(){
		console.log($scope.data);

		$http.post("/dbsearch", $scope.data)
		.success(function (response){
			$scope.serviceClients = response;
		})

	}

}