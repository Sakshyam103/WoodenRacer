import {useEffect, useState} from 'react'
import {stringify} from "postcss";
// import './App.css'
// import "./index.css"
function App() {
    // const [bool, setBool] = useState(false)
    const[speed, setSpeed] = useState(0);
    const[throttle, setThrottle] = useState(0);
    const [braking, setBraking] = useState(0);
    const [steering, setSteering] = useState(0);
    const [slip, setSlip] = useState(0);
    const [autofunction, setAutofunction] = useState("");

    const [data, setData] = useState({
        velocity: 0,
        throttle: 0,
        braking: 0,
        steering: 0,
        slip: 0,
        auto_function: "n",
        velocity1: 0,
        throttle1: 0,
        braking1: 0,
        steering1: 0,
        slip1:0,
        auto_function1: "n"
    });

    // const [data2, setData2] = useState({
    //     upType: "",
    //     name: "",
    //     velocity: 0,
    //     throttle: 0,
    //     braking: 0,
    //     steering: 0,
    //     slip: 0,
    //     auto_function: ""
    // })



    let headers =new Headers();
    headers.append('Content-Type', 'application/json');
  headers.append('Accept', 'application/json');

  headers.append('Access-Control-Allow-Origin', 'http://127.0.0.1:5175');
  headers.append('Access-Control-Allow-Credentials', 'true');



    useEffect(() => {
        fetch("http://127.0.0.1:5175/data").then((res)=>res.json().then((data1)=> {
            setData({
                velocity: data1['velocity'],
                throttle: data1['throttle'],
                braking: data1['braking'],
                steering: data1['steeringAngle'],
                slip: data1['slipAngle'],
                auto_function: data1['autoFunction'],
                velocity1: data1['velocity1'],
                throttle1: data1['throttle1'],
                braking1: data1['braking1'],
                steering1: data1['steeringAngle1'],
                slip1: data1['slipAngle1'],
                autofunction1: data1['autoFunction1']
            });
            // fetch("http://127.0.0.1:5175/data2").then((res)=>res.json().then((data2)=>{
            //     setData2({
            //     upType: data2.upType,
            //     name: data2.name,
            //     velocity: data2.velocity,
            //     throttle: data2.throttle,
            //     braking: data2.braking,
            //     steering: data2.steering,
            //     slip: data2.slip,
            //     auto_function: data2.auto_function
            // });
            // }))
        }));
    }, [data]);


    // function increaseSpeed(){
    //     fetch("/speed")
    // }

    // async function changeSpeed(a) {
    //     const response = await fetch('http://127.0.0.1:5175/speed',{method:"POST",
    //     headers:{
    //         'Content-Type': 'application/json'
    //     },
    //         body: JSON.stringify({a})
    //     })
    //     if (response.ok){
    //         console.log("speed changed")
    //     }
    // }

    // async function changeSteering(a) {
    //     const response = await fetch('http://127.0.0.1:5175/steering',{method:"POST",
    //     headers:{
    //         'Content-Type': 'application/json'
    //     },
    //         body: JSON.stringify({a})
    //     })
    //     if (response.ok){
    //         console.log("steering angle changed")
    //     }
    // }

    async function stop() {
        const response = await fetch('http://127.0.0.1:5175/stop',{method:"GET",
        headers:{
            'Content-Type': 'application/json'
        },
        })
        if (response.ok){
            console.log("stopped")
        }
    }

    async function start(a,b,c,d,e,f) {
        let val = JSON.stringify({velocity: a, throttle: b, braking: c, steering: d, slip: e, autoF: f});
        const response = await fetch('http://127.0.0.1:5175/start',{method:"POST",
        headers:{
            'Content-Type': 'application/json'
        },
            body: val
        })
        if (response.ok){
            let a = await response.json();
                console.log("done")
            console.log(a)
                // setData(prevState => ({
                //     ...prevState,
                //     velocity: a['velocity'],
                //     throttle: a['throttle'],
                //     braking: a['braking'],
                //     steering: a['steeringAngle'],
                //     slip: a['slipAngle'],
                //     auto_function: a['autoFunction'],
                //     velocity1: a['velocity1'],
                //     throttle1: a['throttle1'],
                //     braking1: a['braking1'],
                //     steering1: a['steeringAngle1'],
                //     slip1: a['slipAngle1'],
                //     auto_function1: a['autoFunction1']
                // }))

        }
        //     .then(res=> {
        //     if(!res.ok){
        //         console.error('Request failed with status:', res.status);
        //         return res.text();
        //     }
        //     return res.text();
        // }).then( response=>{
        //     console.log(response);
        //     if(response === true){
        //         let a = response.json();
        //         console.log("done")
        //         setData(prevState => ({
        //             velocity: a['velocity'],
        //             throttle: a['throttle'],
        //             braking: a['braking'],
        //             steering: a['steeringAngle'],
        //             slip: a['slipAngle'],
        //             auto_function: a['autoFunction'],
        //             velocity1: a['velocity1'],
        //             throttle1: a['throttle1'],
        //             braking1: a['braking1'],
        //             steering1: a['steeringAngle1'],
        //             slip1: a['slipAngle1'],
        //             auto_function1: a['autoFunction1']
        //         }))
        //     }
        // }).catch(error=>{
        //     console.error("Error:" , error);
        // })

    }
  // const [count, setCount] = useState(0)
  //
  // return (
  //   <>d
  //     <div>
  //       <a href="https://vitejs.dev" target="_blank">
  //         <img src={viteLogo} className="logo" alt="Vite logo" />
  //       </a>
  //       <a href="https://react.dev" target="_blank">
  //         <img src={reactLogo} className="logo react" alt="React logo" />
  //       </a>
  //     </div>
  //     <h1>Vite + React</h1>
  //     <div className="card">
  //       <button onClick={() => setCount((count) => count + 1)}>
  //         count is {count}
  //       </button>
  //       <p>
  //         Edit <code>src/App.jsx</code> and save to test HMR
  //       </p>
  //     </div>
  //     <p className="read-the-docs">
  //       Click on the Vite and React logos to learn more
  //     </p>
  //   </>
  // )

    return (
        <div className="w-[100%] h-screen">
            <h1 className="text-center text-4xl font-serif font-bold">Wooden car</h1>
            <div className="flex flex-col">

                <div
                    className="w-1/2 mx-auto h-1/2 bg-gray-500 flex flex-col gap-5 justify-items-center my-5 p-5 shadow-black shadow-2xl">
                    {/*<div>*/}
                    {/*    <button className="w-full h-10 bg-blue-950 text-white rounded-2xl" onClick={() => setBool(true)}>{bool &&*/}
                    {/*    </button>*/}
                    {/*</div>*/}

                    <div className="w-full">velocity: <input className="m-3 border-2 border-black p-4 w-1/2 h-10"
                                                             type="number"
                                                             value={speed}
                                                             onChange={(e) => setSpeed(e.target.valueAsNumber)}/>
                    </div>
                    {/*<div className="w-full">*/}
                    {/*    <button*/}
                    {/*        className="w-full h-10 bg-blue-950 text-white rounded-2xl m-3 hover:bg-blue-900 focus:border-white focus:border-2"*/}
                    {/*        onClick={async () => changeSpeed(speed)}>Click*/}
                    {/*    </button>*/}
                    {/*</div>*/}
                    <div className="w-full">throttle: <input className="m-3 border-2 border-black p-4 w-1/2 h-10"
                                                             type="number"
                                                             value={throttle}
                                                             onChange={(e) => setThrottle(e.target.valueAsNumber)}/></div>
                    {/*<div className="w-full">*/}
                    {/*    <button*/}
                    {/*        className="w-full h-10 bg-blue-950 text-white rounded-2xl m-3 hover:bg-blue-900 focus:border-white focus:border-2"*/}
                    {/*        onClick={async () => changeThrottle(speed)}>Click*/}
                    {/*    </button>*/}
                    {/*</div>*/}
                    <div className="w-full">braking: <input className="m-3 border-2 border-black p-4 w-1/2 h-10"
                                                            type="number"
                                                            value={braking}
                                                            onChange={(e) => setBraking(e.target.valueAsNumber)}/></div>
                    {/*<div className="w-full">*/}
                    {/*    <button*/}
                    {/*        className="w-full h-10 bg-blue-950 text-white rounded-2xl m-3 hover:bg-blue-900 focus:border-white focus:border-2"*/}
                    {/*        onClick={async () => changeBraking(speed)}>Click*/}
                    {/*    </button>*/}
                    {/*</div>*/}
                    {/*<div className="w-full">*/}
                    {/*    <button className="w-full h-10 bg-blue-950 text-white rounded-2xl m-3 hover:bg-blue-900"*/}
                    {/*            onClick={async () => changeSteering(steering)}>*/}
                    {/*        Click*/}
                    {/*    </button>*/}
                    {/*</div>*/}
                    {/*<button className="w-full h-10 bg-blue-950 text-white rounded-2xl m-3 hover:bg-blue-900"*/}
                    {/*        onClick={() => start(speed1, steering)}>*/}
                    {/*    Start*/}
                    {/*</button>*/}
                    <div className="w-full">Steering Angle: <input className="m-3 border-2 border-black p-4 w-1/2 h-10"
                                                                   type="number"
                                                                   value={steering}
                                                                   onChange={(e) => setSteering(e.target.valueAsNumber)}/>
                    </div>
                    {/*<div className="w-full">*/}
                    {/*    <button*/}
                    {/*        className="w-full h-10 bg-blue-950 text-white rounded-2xl m-3 hover:bg-blue-900 focus:border-white focus:border-2"*/}
                    {/*        onClick={async () => changeSteering(speed1)}>Click*/}
                    {/*    </button>*/}
                    {/*</div>*/}
                    {/*<div>*/}
                    {/*    <button className="w-full h-10 bg-blue-950 text-white rounded-2xl" onClick={() => increseSteeringAngle}>Increase steering angle*/}
                    {/*    </button>*/}
                    {/*</div>*/}
                    {/*    <div className="w-full">Slip Angle: <input className="m-3 border-2 border-black w-1/2 h-10 p-4"*/}
                    {/*                                                   type="number" defaultValue={slip}*/}
                    {/*                                                   onChange={(e) => setSlip(e.target.valueAsNumber)}/>*/}
                    {/*    </div>*/}

                    {/*    <button className="w-full h-10 bg-blue-950 text-white rounded-2xl m-3 hover:bg-blue-900"*/}
                    {/*            onClick={async () => slip}>*/}
                    {/*        Stop*/}
                    {/*    </button>*/}
                    {/*</div>*/}
                    <div className="w-full">Slip Angle: <input className="m-3 border-2 border-black p-4 w-1/2 h-10"
                                                               type="number"
                                                               value={slip}
                                                               onChange={(e) => setSlip(e.target.valueAsNumber)}/>
                    </div>
                    {/*<div className="w-full">*/}
                    {/*    <button*/}
                    {/*        className="w-full h-10 bg-blue-950 text-white rounded-2xl m-3 hover:bg-blue-900 focus:border-white focus:border-2"*/}
                    {/*        onClick={async () => changeSlip(speed1)}>Click*/}
                    {/*    </button>*/}
                    {/*</div>*/}
                    <div className="w-full">Auto Function: <input className="m-3 border-2 border-black p-4 w-1/2 h-10"
                                                                  type="text"
                                                                  value={autofunction}
                                                                  onChange={(e) => setAutofunction(e.target.value)}/>
                    </div>
                    <div className="w-full flex flex-row">
                    <div className="w-full">
                        <button
                            className="w-full h-10 bg-blue-950 text-white rounded-2xl m-3 hover:bg-blue-900 focus:border-white focus:border-2"
                            onClick={async () => start(speed, throttle, braking, steering, slip, autofunction)}>Start
                        </button>
                    </div>
                    <div className="w-full">
                        <button
                            className="w-full h-10 bg-blue-950 text-white rounded-2xl m-3 hover:bg-blue-900 focus:border-white focus:border-2"
                            onClick={async () => stop()}>Stop
                        </button>
                    </div>
                    </div>
                </div>

                <div className="flex flex-row gap-5">
                    <div
                        className="w-full h-1/2 m-5 text-purple-950 font-bold font-serif italic text-4xl shadow-black shadow-2xl p-5 flex flex-col justify-evenly gap-5">
                        {/*<h3>upType: {data.upType}</h3>*/}
                        {/*<h3>name: {data.name}</h3>*/}
                        <h3>velocity: {data.velocity}</h3>
                        <h3>throttle: {data.throttle}</h3>
                        <h3>braking force: {data.braking}</h3>
                        <h3>steering angle: {data.steering}</h3>
                        <h3>slip angle: {data.slip}</h3>
                        <h3>auto-function: {data.auto_function}</h3>
                    </div>
                        <div
                            className="w-full h-1/2 m-5 text-purple-950 font-bold font-serif italic text-4xl shadow-black shadow-2xl p-5 flex flex-col justify-evenly gap-5">
                            {/*<h3>upType: {data.upType1}</h3>*/}
                            {/*<h3>name: {data.name1}</h3>*/}
                            <h3>velocity: {data.velocity1}</h3>
                            <h3>throttle: {data.throttle1}</h3>
                            <h3>braking force: {data.braking1}</h3>
                            <h3>steering angle: {data.steering1}</h3>
                            <h3>slip angle: {data.slip1}</h3>
                            <h3>auto-function: {data.auto_function1}</h3>
                        </div>

                    </div>
                </div>
            </div>
            )
            }

            export default App
