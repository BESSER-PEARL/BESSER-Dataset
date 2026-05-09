





import java.util.List;
import java.util.ArrayList;

public class message_Message  {

    private String uid;
    private String name;





    private message_MessageLibrary message_messagelibrary;


    public message_Message(
        String uid,        String name    ) {
        this.uid = uid;
        this.name = name;
    }


    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public message_MessageLibrary getMessage_messagelibrary() {
        return message_messagelibrary;
    }

    public void setMessage_messagelibrary(message_MessageLibrary message_messagelibrary) {
        this.message_messagelibrary = message_messagelibrary;
    }

}