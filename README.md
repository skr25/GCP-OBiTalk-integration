# GCP-OBiTalk-integration
This integration provides ability to track the incoming call and lookup the Google contacts based on called id and gets name and annouces on your Netowrk speakers 
Here are the following Prerequisites
1. Should have OBITlak device with access to its web page
2. Should have Vera Control Hub and Should have DLNAMEdia Controller app. Alternatively, you can run your own cloud based tts server
3. Should have defined a project in Google Cloud platform and assign Contacts API to this project and receive client id and client secret to connect to GCP.
4. I have hosted this program in qnap server and running 24X7


Note: I am running amazon polly TTS server on another machine. I configured DLNA Media controller app to point to local AWS polly TTS server. So, if tts request goes to Vera, it finaly routes to amzon polly local server to get converted mp3 file and played by DLNA media controller app on vera for one of DLNA speaker.
