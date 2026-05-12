





import java.util.List;
import java.util.ArrayList;

public class bean_ImageBean  {

    private int id;
    private String emailFId;
    private String imageName;
    private int messageFId;
    private None time;
    private None date;



    public bean_ImageBean(
        int id,        String emailFId,        String imageName,        int messageFId,        None time,        None date    ) {
        this.id = id;
        this.emailFId = emailFId;
        this.imageName = imageName;
        this.messageFId = messageFId;
        this.time = time;
        this.date = date;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getEmailfid() {
        return emailFId;
    }

    public void setEmailfid(String emailFId) {
        this.emailFId = emailFId;
    }
    public String getImagename() {
        return imageName;
    }

    public void setImagename(String imageName) {
        this.imageName = imageName;
    }
    public int getMessagefid() {
        return messageFId;
    }

    public void setMessagefid(int messageFId) {
        this.messageFId = messageFId;
    }
    public None getTime() {
        return time;
    }

    public void setTime(None time) {
        this.time = time;
    }
    public None getDate() {
        return date;
    }

    public void setDate(None date) {
        this.date = date;
    }


}