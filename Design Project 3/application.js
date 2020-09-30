/*
Created by Ethan Tran
application script called by application.html
Pleasure ensure that both files are in the same folder
*/
//Firebase Configuration
var firebaseConfig = {
    apiKey: "AIzaSyA4fFc50MbroRk0YgUGuYcci7YKl2rM_-I",
    authDomain: "baby-temperature.firebaseapp.com",
    databaseURL: "https://baby-temperature.firebaseio.com",
    projectId: "baby-temperature",
    storageBucket: "baby-temperature.appspot.com",
    messagingSenderId: "333367061666",
    appId: "1:333367061666:web:b589e8f7764e8bf28e3bfb",
    measurementId: "G-K8NS0CVXKT"
  };

  //Initialize Firebase
  firebase.initializeApp(firebaseConfig);
  
  //Reference to objects in database
  var temp = firebase.database().ref("Temp");
  var t = firebase.database().ref("T");

  //Update values in table when child_changed event is triggered
  temp.on("child_changed", function(snapshot){
    var temperature = snapshot.val();
    $("#temperature").html(temperature)
  });

  t.on("child_changed", function(snapshot){
    var time = snapshot.val();
    $("#time").html(time)
  });

$(function(){
    var ctx = document.getElementById('myChart').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['time1', 'time2', 'time3', 'time4', 'time5', 'time6'],
            datasets: [{
                label: 'Temperature',
                data: [12, 19, 3, 5, 2, 3],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }]
        },
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        }
                }]
            }
        }
    });
})