# Youtube Client_ID and Client_Secret

to get the client ID and Client secret for Youtube JSON we first need to go on the Google Cloud Console
- https://console.cloud.google.com/welcome/new?authuser=3&supportedpurview=project
- log in with your google account that you have associated with Youtube

- When you log in on the Google Cloud Console you'll see a button on your left that says "Select a project" click there.

![Playlist_Transfer Step 1 image](https://github.com/Dark57234/Playlist_Transfer/blob/main/Setup/Images/YoutubeStep1.png)

- Afterwards a new pop up will appear with all your projects, if you don't have any projects, click on the upper right option called "New Project".

![Playlist_Transfer Step 2 image](https://github.com/Dark57234/Playlist_Transfer/blob/main/Setup/Images/YoutubeStep2.png)

- Then you'll be prompted to add a name and add an organization. Add your name of choice but any name is fine.

![Playlist_Transfer Step 3 image](https://github.com/Dark57234/Playlist_Transfer/blob/main/Setup/Images/YoutubeStep3.png)

- After waiting for a bit you'll see a notification pop up saying your project has been created, when it does click on Select Project

![Playlist_Transfer Step 4 image](https://github.com/Dark57234/Playlist_Transfer/blob/main/Setup/Images/YoutubeStep4.png)

- When you enter your project dashboard, on your left you'll see an option called "APIs & Services" when you hover on it you'll see another option called library. Click there

![Playlist_Transfer Step 5 image](https://github.com/Dark57234/Playlist_Transfer/blob/main/Setup/Images/YoutubeStep5.png)

- After you enter the API Library look up "youtube data api v3" and click the option that appears

![Playlist_Transfer Step 6 image](https://github.com/Dark57234/Playlist_Transfer/blob/main/Setup/Images/YoutubeStep6.png)


![Playlist_Transfer Step 7 image](https://github.com/Dark57234/Playlist_Transfer/blob/main/Setup/Images/YoutubeStep7.png)

- When you click on the result you'll see an option that says "Enable" click it

![Playlist_Transfer Step 8 image](https://github.com/Dark57234/Playlist_Transfer/blob/main/Setup/Images/YoutubeStep8.png)

- Afterwards you'll see new options on your left, specifically one called "OAuth consent screen", click there

![Playlist_Transfer Step 9 image](https://github.com/Dark57234/Playlist_Transfer/blob/main/Setup/Images/YoutubeStep9.png)

- When entering this consent screen you'll see that you haven't configured the Google Auth Platform, to start press "Get Started"

![Playlist_Transfer Step 10 image](https://github.com/Dark57234/Playlist_Transfer/blob/main/Setup/Images/YoutubeStep10.png)

- Afterwards fill the requirements with any name you want and add any email, the important step is on the Audience section select "External" so we can add test users

![Playlist_Transfer Step 11 image](https://github.com/Dark57234/Playlist_Transfer/blob/main/Setup/Images/YoutubeStep11.png)

- After filling the rest of the requirements you'll see a new option called metrics and that you haven't configured OAuth Clients for the project yet, and to create one go to the right and click where it says "Create OAuth client"

![Playlist_Transfer Step 12 image](https://github.com/Dark57234/Playlist_Transfer/blob/main/Setup/Images/YoutubeStep12.png)

- Then we choose the Application type, choose Desktop app

![Playlist_Transfer Step 13 image](https://github.com/Dark57234/Playlist_Transfer/blob/main/Setup/Images/YoutubeStep13.png)

- Afterwards add any name you like and then click "Create" and then a pop up with your Client ID and with an option to download JSON, in this case we need the JSON so we download it

![Playlist_Transfer Step 14 image](https://github.com/Dark57234/Playlist_Transfer/blob/main/Setup/Images/YoutubeStep14.png)

- If the download didnt start in the last step, press ok and on the next screen on right there will be an option to download the JSON which should look like this

![Playlist_Transfer Step 15 image](https://github.com/Dark57234/Playlist_Transfer/blob/main/Setup/Images/YoutubeStep15.png)

- After we get the JSON we need to add a test user so they can use the app, so we go back on the Audience section on the left and we scroll down to the "OAuth user cap" and on the "Test users" section we click on the Add users 

![Playlist_Transfer Step 16 image](https://github.com/Dark57234/Playlist_Transfer/blob/main/Setup/Images/YoutubeStep16.png)

- And here we add the Email that is associated with the Youtube account that you want to add your playlist to

![Playlist_Transfer Step 17 image](https://github.com/Dark57234/Playlist_Transfer/blob/main/Setup/Images/YoutubeStep17.png)
