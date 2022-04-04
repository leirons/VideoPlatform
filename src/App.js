import './App.css';
import React from 'react'
import ReactPlayer from 'react-player'
import Comments from "./comments/Comments"
import UrlForm from "./UrlForm";
import VideoComponent from "./VideoComponent";

function App() {

    return(
        <div>

            <UrlForm/>
            <ReactPlayer url='https://www.twitch.tv/videos/106400740' controls={true}/>
            <Comments
                commentsUrl="http://localhost:3000/comments"
                currentUserId="1"
            />
        </div>
    )

}


export default App
