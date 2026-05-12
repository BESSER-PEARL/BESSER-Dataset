





import java.util.List;
import java.util.ArrayList;

public class bean_MessageBean  {

    private None date;
    private String emailFId;
    private String status;
    private int imageFId;
    private int id;
    private None time;
    private String message;
    private String recFId;
    private String category;



    public bean_MessageBean(
        None date,        String emailFId,        String status,        int imageFId,        int id,        None time,        String message,        String recFId,        String category    ) {
        this.date = date;
        this.emailFId = emailFId;
        this.status = status;
        this.imageFId = imageFId;
        this.id = id;
        this.time = time;
        this.message = message;
        this.recFId = recFId;
        this.category = category;
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
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
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
    public None getTime() {
        return time;
    }

    public void setTime(None time) {
        this.time = time;
    }
    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
    public String getRecfid() {
        return recFId;
    }

    public void setRecfid(String recFId) {
        this.recFId = recFId;
    }
    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }


}