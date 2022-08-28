import React, {useState, useEffect, useRef} from 'react';

export default function LoadFile() {
	const [file, setFile] = useState();
	const ref = useRef(null);

	const fileLoader = e => {
		const reader = new FileReader();
		const file = e.target.files[0];
		reader.onload = event => {
			setFile(event.target.result);
			console.log(event.target.result);
		};
		reader.readAsDataURL(file);
	};

	const onButtonClick = () => {
		ref.current.click();
	};

	return (
		<div>
			<button className={"rainbow"} style={{padding:"8px 12px", border: "none", borderRadius: "12px"}}
			onClick={onButtonClick}>Open file</button>
			<input ref={ref} type="file" onChange={e => fileLoader(e)} style={{display: "none"}}/>
			<img src={file} />
		</div>
	);
}
