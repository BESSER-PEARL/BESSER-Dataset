





import java.util.List;
import java.util.ArrayList;

public class bean_Warning  {

    private String message;
    private String emailFId;
    private None date;
    private None time;
    private int id;
    private String category;



    public bean_Warning(
        String message,        String emailFId,        None date,        None time,        int id,        String category    ) {
        this.message = message;
        this.emailFId = emailFId;
        this.date = date;
        this.time = time;
        this.id = id;
        this.category = category;
    }


    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
    public String getEmailfid() {
        return emailFId;
    }

    public void setEmailfid(String emailFId) {
        this.emailFId = emailFId;
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
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }


}