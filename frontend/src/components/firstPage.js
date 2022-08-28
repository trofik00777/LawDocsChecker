import {useCallback, useEffect, useRef, useState} from "react";
import './firstPage.css'
// import Particles from "react-tsparticles";
// import { loadFull } from "tsparticles";

function FirstPage({setFile}) {
	// const particlesInit = useCallback(async (engine) => {
	// 	console.log(engine);
	// 	// you can initiate the tsParticles instance (engine) here, adding custom shapes or presets
	// 	// this loads the tsparticles package bundle, it's the easiest method for getting everything ready
	// 	// starting from v2 you can add only the features you need reducing the bundle size
	// 	await loadFull(engine);
	// }, []);
	//
	// const particlesLoaded = useCallback(async (container) => {
	// 	await console.log(container);
	// }, []);
	//
	// return (
	// 	<Particles
	// 		id="tsparticles"
	// 		init={particlesInit}
	// 		loaded={particlesLoaded}
	// 		options={{
	// 			background: {
	// 				color: {
	// 					value: "#0d47a1",
	// 				},
	// 			},
	// 			fpsLimit: 120,
	// 			interactivity: {
	// 				events: {
	// 					onClick: {
	// 						enable: true,
	// 						mode: "push",
	// 					},
	// 					onHover: {
	// 						enable: true,
	// 						mode: "repulse",
	// 					},
	// 					resize: true,
	// 				},
	// 				modes: {
	// 					push: {
	// 						quantity: 4,
	// 					},
	// 					repulse: {
	// 						distance: 200,
	// 						duration: 0.4,
	// 					},
	// 				},
	// 			},
	// 			particles: {
	// 				color: {
	// 					value: "#ffffff",
	// 				},
	// 				links: {
	// 					color: "#ffffff",
	// 					distance: 150,
	// 					enable: true,
	// 					opacity: 0.5,
	// 					width: 1,
	// 				},
	// 				collisions: {
	// 					enable: true,
	// 				},
	// 				move: {
	// 					directions: "none",
	// 					enable: true,
	// 					outModes: {
	// 						default: "bounce",
	// 					},
	// 					random: false,
	// 					speed: 6,
	// 					straight: false,
	// 				},
	// 				number: {
	// 					density: {
	// 						enable: true,
	// 						area: 800,
	// 					},
	// 					value: 80,
	// 				},
	// 				opacity: {
	// 					value: 0.5,
	// 				},
	// 				shape: {
	// 					type: "circle",
	// 				},
	// 				size: {
	// 					value: { min: 1, max: 5 },
	// 				},
	// 			},
	// 			detectRetina: true,
	// 		}}
	// 	/>);

	const ref = useRef();
	const [result, setResult] = useState([]);

	return (
		<div className={"p-file-loader"}>

			<div className={"window"}>
				<h2>
				Online File Analyzer</h2>
				<div className={"text"}>Analyze space usage in PDF, PowerPoint, Word and Excel files</div>
				<div className={"uploadButton"} onClick={()=>ref.current.click()}>
					+
				</div>
				<input ref={ref} type={"file"} style={{display: "none"}} onChange={(e)=> {
					console.log(e.currentTarget.files);setFile(e.currentTarget.files[0])
				}}/>
				<div className={"buttonDesc"}>
					Choose or drop file
				</div>
			</div>
		</div>
	);
}

export default FirstPage;
