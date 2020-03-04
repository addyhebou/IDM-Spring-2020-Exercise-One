import React from "react";
import axios from "axios";

const defaultKey = "88b2bb448dff5786abe11bb1a3cfa4fe";

function Home(){
    return (
        <div className = "Home">
            <h1>Weather in "City"</h1>
            <div className = "WeatherInfo">
                <div className = "WeatherInfo_Image">
                    <img src = "" alt = ""></img>
                </div>
                <div className = "WeatherInfo_Data">

                    <div className = "CurrentTemperature">
                        <p className = "CurrentTemperatureTemp">48&#176;</p>
                        <p className = "CurrentTemperatureLabel">Current Temperature</p>
                    </div>

                    <div className = "OtherTemperatures">
                        <p>High Temp: <strong>53&#176;</strong></p>
                        <p>Low Temp: <strong>32&#176;</strong></p>
                    </div>
                    
                    <div className = "Stats">
                        <p>Humidity: 100%</p>
                        <p>Wind: 10mph</p>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Home;