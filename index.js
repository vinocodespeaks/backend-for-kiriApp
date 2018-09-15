var firebase = require('firebase');
var cmd = require('node-cmd');

var config = {
    apiKey: "AIzaSyAsn0ow1cIugfZSKS4cidFokLK9eMZwduw",
    authDomain: "rit-hackathon.firebaseapp.com",
    databaseURL: "https://rit-hackathon.firebaseio.com",
    projectId: "rit-hackathon",
    storageBucket: "rit-hackathon.appspot.com",
    messagingSenderId: "60634605932"
};
firebase.initializeApp(config);

firebase.database().ref("/in/").on("value", (snap) => {
    
    if (snap.val()) {
        console.log(snap.val())
        cmd.get("py ask.py \"" + snap.val().split("\n").join(" ") + "\"",
            function (err, a, stderr) {
                firebase.database().ref("/out/").set(a.substring(a.indexOf("----------POSSIBLE QUESTIONS--------") + 38));
                firebase.database().ref("/in/").set(null);
            }
        );
    }
})