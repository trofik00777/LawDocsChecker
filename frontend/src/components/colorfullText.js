import React, {useState} from 'react';
import ReactQuill, {Quill} from 'react-quill';
import 'react-quill/dist/quill.snow.css';
import './colorfullText.css'
import lol from './scratch.json'

export default function MyComponent() {
	var ColorClass = Quill.import('attributors/class/color');
	Quill.register(ColorClass, true);
	let value = lol;

	value = value.classes.map((e) => {
		return {insert: e.text, attributes: {color: e.label}}
	})

	console.log(value)

	return (<ReactQuill theme="snow" modules={{toolbar: false}} value={value} readOnly={true}/>);
}
