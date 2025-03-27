if ('serviceWorker' in navigator){
    navigator.serviceWorker.register('/static/js/sw.js')
    .then((reg) => console.log('service worker registered ', reg)) //Loging the registered service worker if succesfull
    .catch((err) => console.log('service worker not registered' , err)); //loging the error if not succesfull
}


