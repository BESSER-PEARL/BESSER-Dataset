





import java.util.List;
import java.util.ArrayList;

public class bean_LikeBean  {

    private int imageFId;
    private int id;
    private None date;
    private String emailFId;
    private None time;



    public bean_LikeBean(
        int imageFId,        int id,        None date,        String emailFId,        None time    ) {
        this.imageFId = imageFId;
        this.id = id;
        this.date = date;
        this.emailFId = emailFId;
        this.time = time;
    }


    public int getImagefid() {
        return imageFId;
    }

    public void setImagefid(int imageFId) {
        this.imageFId = imageFId;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public None getDate() {
        return date;
    }

    public void setDate(None date) {
        this.date = date;
    }
    public String getEmailfid() {
        return emailFId;
    }

    public void setEmailfid(String emailFId) {
        this.emailFId = emailFId;
    }
    public None getTime() {
        return time;
    }

    public void setTime(None time) {
        this.time = time;
    }


}