let submitLink = document.getElementById('submit-link')
let stream = document.querySelectorAll('.stream')
let downloadButton = document.getElementById('download')
let closeToast = document.querySelector('.close')
let warningToast = document.querySelector('.warning')
console.log(warningToast)
bool = false

Array.from(stream).map(element =>
    {
        element.addEventListener('click',(event) => {
            sessionStorage.setItem('stream_type',event.target.value)
            Array.from(stream).map(element =>{
                if (element.classList.contains('selected-stream')){
                    element.classList.remove('selected-stream')
                }
                    event.target.classList.add('selected-stream')                                   
            })           
        } 
    )
})
Array.from(stream).map(element =>{
    let type = sessionStorage.getItem('stream_type')
    if(type =='mp3' || type=="mp4"){
        if(element.value==type){
            element.classList.add('selected-stream')
        }
    }
})

videoList = document.getElementsByClassName('video-name')
const arrayFromCollection = Array.from(videoList);

downloadButton.addEventListener('click', function getData(){  
    let videoUrls = []
    arrayFromCollection.map((element, index) => {
        videoUrls.push(element.dataset.videourl)
        
    });
    sessionStorage.setItem('video_urls',[videoUrls])

    let type = sessionStorage.getItem('stream_type')
    if (!type){
        document.querySelector('.warning').style.display = "block"
        setTimeout(function(){
            document.querySelector('.warning').style.display = "none"
        },2000)
        
    }else{
        let video_urls = sessionStorage.getItem('video_urls')
        sendData(type,video_urls)
        document.querySelector('.success').style.display = "block"
        setTimeout(function(){
            document.querySelector('.success').style.display = "none"
        },2000)
    }
    
    
    })

closeToast.addEventListener('click',function(){
    warningToast.style.display = "none";
    
});
function sendData(type,video_urls){
        var url = 'download/'
        fetch(url, {
        method: 'POST',
        headers: {
        'Content-Type':'application/json',
        'X-CSRFToken':csrftokenIndex,
        },
        body: JSON.stringify({
        'type': type,
        'video_urls':video_urls})
                }
        )
        .then((response)=>{
        return response.json()
        })

        .then((data) =>{

        console.log(data)
        return data     

        })
}


