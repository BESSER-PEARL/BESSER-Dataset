





import java.util.List;
import java.util.ArrayList;

public class bean_MessageLikeBean  {

    private None date;
    private None time;
    private String emailFId;
    private int id;
    private int messageFId;



    public bean_MessageLikeBean(
        None date,        None time,        String emailFId,        int id,        int messageFId    ) {
        this.date = date;
        this.time = time;
        this.emailFId = emailFId;
        this.id = id;
        this.messageFId = messageFId;
    }


    public None getDate() {
        return date;
    }

    public void setDate(None date) {
        this.date = date;
    }
    public None getTime() {
        return time;
    }

    public void setTime(None time) {
        this.time = time;
    }
    public String getEmailfid() {
        return emailFId;
    }

    public void setEmailfid(String emailFId) {
        this.emailFId = emailFId;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getMessagefid() {
        return messageFId;
    }

    public void setMessagefid(int messageFId) {
        this.messageFId = messageFId;
    }


}