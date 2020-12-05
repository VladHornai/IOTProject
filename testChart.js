
Promise.all([
    fetch('Outputs/Modbus_Gw_File_Parsed.json').then(resp => resp.json()),
    fetch('Outputs/pyModbus.json').then(resp => resp.json())
          ]).then(function (data) {
                appendData(data);
                console.log(data);
            })
            .catch(function (err) {
                console.log('error: ' + err);
            });

    function appendData(tempdata){
      var mainContainer = document.getElementById("myData");
          var ip;
          for(var i=0; i<tempdata[1].length; i++){
              ip = tempdata[1][i].Eui64;
              var div = document.createElement("div");
              div.innerHTML = ip+ ': <br/><b>Concentrator: </b>'+ 
                              '<br/>co_tsap_id: '+tempdata[0][ip].concentrator.co_tsap_id+
                              '<br/>co_id: '+tempdata[0][ip].concentrator.co_id+
                              '<br/>data_period: '+tempdata[0][ip].concentrator.data_period+
                              '<br/>data_phase: '+tempdata[0][ip].concentrator.data_phase+
                              '<br/>data_stalelimit: '+tempdata[0][ip].concentrator.data_stalelimit+
                              '<br/>data_version: '+tempdata[0][ip].concentrator.data_version+
                              '<br/>interface_type: '+tempdata[0][ip].concentrator.interface_type+'<br/>_';   
              mainContainer.appendChild(div);
        }  

          //we will work with data 2!
}


window.chartColors = { 	red: 'rgb(255, 99, 132)', 	orange: 'rgb(255, 159, 64)', 	yellow: 'rgb(255, 205, 86)', 	green: 'rgb(75, 192, 192)', 	blue: 'rgb(54, 162, 235)', 	purple: 'rgb(153, 102, 255)', 	grey: 'rgb(201, 203, 207)' }; 

var randomScalingFactor = function() {
			return Math.round(Math.random() * 100);
		};



var config = {
		type: 'line',
		data: {
			labels: ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'],
			datasets: [{
				label: 'Fresh Data',
				data: [0, 10, 20, 60, 60, NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
				borderColor: window.chartColors.green,
				backgroundColor: 'rgba(0, 0, 0, 0)',
				fill: false,
				cubicInterpolationMode: 'monotone'
			}, {
				label: 'Stale Data',
				data: [NaN, NaN, NaN, NaN, 60, 120, 140, 180, 120, NaN, NaN, NaN, NaN],
				borderColor: window.chartColors.yellow,
				backgroundColor: 'rgba(0, 0, 0, 0)',
				fill: false,
			}, {
				label: 'Missing data or connection',
				data: [NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN, 120, 125, 105, 110, 170],
				borderColor: window.chartColors.red,
				backgroundColor: 'rgba(0, 0, 0, 0)',
				fill: false,
				lineTension: 0
			}]
		},
		options: {
			responsive: true,
			title: {
				display: true,
				text: 'Chart.js Line Chart - Cubic interpolation mode'
			},
			tooltips: {
				mode: 'index'
			},
			scales: {
				xAxes: [{
					display: true,
					scaleLabel: {
						display: true
					}
				}],
				yAxes: [{
					display: true,
					scaleLabel: {
						display: true,
						labelString: 'Value'
					},
					ticks: {
						suggestedMin: -10,
						suggestedMax: 200,
					}
				}]
			}
		},

		
	};

	
var ctx = document.getElementById('canvas').getContext('2d');
window.myLine = new Chart(ctx, config);