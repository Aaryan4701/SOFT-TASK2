self.addEventListener('install', evt => {
    console.log('service worker has been installed'); // logs if service worker is installed
 });
 

 self.addEventListener('activate' , evt => {
    console.log('service worker has been activated'); //logs if service worker is not activated
 });

 //instalation of the service worker 