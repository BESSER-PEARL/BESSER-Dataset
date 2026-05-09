





import java.util.List;
import java.util.ArrayList;

public class message_Translation  {

    private String uid;
    private String translation;





    private message_Message message_message;




    private message_Language message_language;


    public message_Translation(
        String uid,        String translation    ) {
        this.uid = uid;
        this.translation = translation;
    }


    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }
    public String getTranslation() {
        return translation;
    }

    public void setTranslation(String translation) {
        this.translation = translation;
    }

    public message_Message getMessage_message() {
        return message_message;
    }

    public void setMessage_message(message_Message message_message) {
        this.message_message = message_message;
    }
    public message_Language getMessage_language() {
        return message_language;
    }

    public void setMessage_language(message_Language message_language) {
        this.message_language = message_language;
    }

}