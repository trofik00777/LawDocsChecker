import {useEffect, useState} from "react";
import './secondPage.css'
import MyComponent from "./colorfullText";
import BarChart from "./barChart";

function SecondPage({result}) {
	const probability = Math.random()*25+result.is_valid
	console.log('result',result)


	const href = "http://84.252.143.40/static/"+result.filename
	return (
		<div className={"p-file-display"}>

			<div className={"left"}>
				{/*<MyComponent/>*/}
				<iframe style={{height: '100%', width: '100%'}}
								src={"https://docs.google.com/gview?url="+href+"&embedded=true"}
								frameBorder="0">
				</iframe>
				{/*<iframe src='https://view.officeapps.live.com/op/embed.aspx?src=https://127.0.0.1:8000/static/0.docx'*/}
				{/*				width='100%' height='100%' frameBorder='0'>This is an embedded <a target='_blank'*/}
				{/*																																						 href='http://office.com'>Microsoft*/}
				{/*	Office</a> document, powered by <a target='_blank' href='http://office.com/webapps'>Office Online</a>.*/}
				{/*</iframe>*/}
			</div>

			<div className={"right"}>
				<h3>Метрики документа</h3>
				<p>Ниже изложенны показатели описывающие данный документ и в случае если документ считается ошибочным причины и
					варианты решения</p>
				{result.classes&&<div className={"widgets"}>
					<div className="container">
						<div className="card">
							<div className="box">
								<div className="percent">
									<svg>
										<circle cx="70" cy="70" r="70"></circle>
										<circle cx="70" cy="70" r="70" style={{"stroke-dashoffset": 440 - 4.40 * probability}}></circle>
									</svg>
									<div className="num">
										<h2>{probability.toFixed(0)}<span>%</span></h2>
									</div>
								</div>
								<h2 className="text">Вероятность того что документ правильный</h2>
							</div>
						</div>
					</div>
					<div className="container">
						<div className="card">
							<div className="box box-special">
								<div className={"desc"} style={{color: 'white'}}>
									Ооо здесь похоже нет ошибок 🎉🎉🎉
								</div>
								<h2 className="text">Причина по которой документ может не подходить</h2>
							</div>
						</div>
					</div>
				</div>}
				<BarChart result={result}/>
				<div className={""} style={{paddingTop: '20px'}}>
					Подсказка:
				</div>
				<div style={{display:"flex",gap:"12px",flexWrap: "wrap", margin:"12px 0 0 0"}}>
				{[
					"(94, 217, 219)",
					"(213, 99, 210)",
					"(113, 123, 130)",
					"(154, 164, 98)",
					"(236, 255, 215)",
					"(61, 165, 59)",
					"(167, 208, 18)",
					"(200, 56, 216)",
					"(239, 4, 10)",
					"(41, 146, 1)",
					"(237, 224, 224)",
					"(239, 33, 244)",
					"(69, 172, 35)",
					"(37, 158, 250)",
					"(117, 254, 156)",
					"(35, 196, 109)",
					"(117, 71, 249)",
					"(142, 184, 7)",
					"(230, 142, 176)",
					"(209, 107, 221)",
					"(150, 184, 138)",
					"(36, 200, 149)",
					"(21, 248, 44)",
					"(134, 8, 45)",
					"(23, 192, 53)",
					"(137, 115, 23)",
					"(144, 70, 194)",
					"(48, 251, 51)",
					"(241, 169, 219)",
					"(181, 255, 191)",
					"(72, 98, 177)",
					"(86, 233, 13)",
					"(174, 31, 176)",
					"(17, 95, 53)",
					"(118, 103, 35)",
					"(117, 99, 65)",
					"(133, 249, 66)",
					"(67, 216, 202)",
					"(205, 241, 67)"
				].map((c, index)=>
					<div className={"circleContainer"}>
						<div className={"circle"} style={{background: "rgb"+c}}/>
						{index+1}
					</div>
				)}
				</div>
				<a href={href} style={{paddingTop: "32px"}}>Ссылка на документы с выделеными обзацами</a>
			</div>
		</div>);
}

export default SecondPage;
