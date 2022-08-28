import React from 'react';
import {Bar} from 'react-chartjs-2';
import {BarElement, CategoryScale, Chart as ChartJS, Legend, LinearScale, Title, Tooltip} from "chart.js";

ChartJS.register(
	CategoryScale,
	LinearScale,
	BarElement,
	Title,
	Tooltip,
	Legend
);

const data = {
	labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39],
	datasets: [
		{
			label: 'My First dataset',
			backgroundColor: 'rgba(255,99,132,0.2)',
			borderColor: 'rgba(255,99,132,1)',
			borderWidth: 1,
			hoverBackgroundColor: 'rgba(255,99,132,0.4)',
			hoverBorderColor: 'rgba(255,99,132,1)',
			data: [1,2,3,4,5].map(()=> [65, 59,59,59, 80, 81, 56, 55, 40]).flat()
		}
	]
};
function BarChart({result}) {
	if (!result.classes)return "wait..."
	console.log(data.datasets[0].data)
	data.datasets[0].data=result.classes.reduce((acc,v)=>{
		acc[v.label+1]+=1;
		return acc
	},data.datasets[0].data.fill(0)).slice(1)

	return (
		<div>
			<h2>Распределение типов абзацев</h2>
			<Bar
				data={data}
				width={700}
				height={350}
				updateMode={"none"}
				options={{
					maintainAspectRatio: true
				}}
			/>
		</div>
	);
}
export default BarChart;
