from sample_config import Config

class Translation(object):
    START_TEXT = """Hello <i><b>{}</b></i>,

I'm Renamer Bot, ⚡Powered By <a href='https://t.me/KumarSwamiKS'>Kumar Swami KS</a> by {}

I Can rename ✍ with custom thumbnail and upload as video/file

Type /help for more details."""
    RENAME_403_ERR = "Sorry. You are not permitted to rename this file."
    ABS_TEXT = " Please don't be selfish."
    UPGRADE_TEXT = "There is no upgrade plan till now it will be added in future"
    DOWNLOAD_START_VIDEO = "Downloading To My Server.....📥"
    DOWNLOAD_START = "<b>Downloding To My Server</b> 📥 \n<code>Please Wait... Uploding Start Soon</code>"
    UPLOAD_START_VIDEO = "Uploading As Video.....📤"
    UPLOAD_START = "<b>Uploding To Telegram</b> 📤 \n<code>😁😍👍Hurray!!!</code>"
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.95GB due to Telegram API limitations.I can't do anything for that 🤷‍♂️."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "**Thank you for Using [Kumar Swami KS](https://t.me/KumarSwamiKS)'s bot.**"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds.\nUploaded in {} seconds."
    NOT_AUTH_USER_TEXT = "Please /upgrade your subscription."
    NOT_AUTH_USER_TEXT_FILE_SIZE = "Detected File Size: {}. Free Users can only upload: {}\nPlease /upgrade your subscription.\nIf you think this is a bug, please contact <a href='https://t.me/Ns_Bot_supporters'>Ns Bot Supporters</a>"
    SAVED_CUSTOM_THUMB_NAIL = "Custom File thumbnail saved ✅️ . This image will be deleted with in 24hr"
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Custom thumbnail cleared succesfully."
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Media cleared succesfully."
    SAVED_RECVD_DOC_FILE = "Document Downloaded Successfully."
    CUSTOM_CAPTION_UL_FILE = "@KS_RenamerProBot"
    NO_CUSTOM_THUMB_NAIL_FOUND = "No Custom ThumbNail found."
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    HELP_USER = """Hai <b><i>{}</i></b>, 

I am Renamer bot ✍ by <a href='https://t.me/{}'>My Father 👨‍🏫</a>
    
1. Send Me A Thumbnail.

2. Send me the file to be Renamed.

3. Reply to that message with <code>/rename new name.extension</code>. with custom thumbnail support.\n(upload as file)

4. Reply to that message with <code>/c2v new name.extension</code>. with custom thumbnail support.\n(uploading as Video)

   
<b>Thanks to <i><a href="https://t.me/KumarSwamiKS">Kumar Swami KS 👨‍🏫</a></i> for his source code. check /about for source code</b>

--------"""
    REPLY_TO_DOC_FOR_RENAME_FILE = "🤦‍♂️ Reply to a Telegram media to `/rename New Name.extension` with custom thumbnail support.\n\n(For uploading as file).\n\nSee /help for mor information. "
    REPLY_TO_DOC_FOR_RENAME_VIDEO = "🤦‍♂️ Reply to a Telegram media to `/c2v New Name.extension` with custom thumbnail support.\n\n(For uploading as video).\n\nSee /help for mor information."
    ABUSIVE_USERS = "You are not allowed to use this bot. If you think this is a mistake, please check /me to remove this restriction."
    FREE_USER_LIMIT_Q_SZE = """Cannot Process.
Free users only 1 request per 30 minutes.
/upgrade or Try 1800 seconds later."""
    IFLONG_FILE_NAME = """File Name limit allowed by Telegram is {alimit} characters.
The given file name has {num} characters.

<b>Essays Not allowed in Telegram file name!</b>
©️ <code>@renamer_Ns_bot</code>
Please short your file name and try again!"""

    About = """Hi __{}__,


**This Bot Can Convert As File/Video**)"""
