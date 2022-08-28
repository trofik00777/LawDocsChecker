import logo from './logo.svg';
import './App.css';
import LoadFile from "./components/LoadFile/load_file";
import FirstPage from "./components/firstPage";
import {useEffect, useState} from "react";
import SecondPage from "./components/secondPage";

function App() {
	const [file, setFile] = useState("");
	const [result, setResult] = useState({});

	useEffect(() => {
		if (!file)return
		console.log('file', file)

		const formData = new FormData()
		formData.append('item', file)

		fetch("http://84.252.143.40/post_inline_file", {
			method: 'POST',
			body: formData,
			headers: {
				Authorization: "Bearer lol",
			}
		}).then((response) => response.json()).then((response)=>{
			console.log(response)
			setResult(response)})
	}, [file]);

console.log('result',result)
	return <> {
		!file?
			<FirstPage setFile={setFile}/> :
			// <FirstPage setFile={setFile}/>
			<SecondPage result={result}/>
	}
	</>

}

export default App;
