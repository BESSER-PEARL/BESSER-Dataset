





import java.util.List;
import java.util.ArrayList;

public class bean_CommentBean  {

    private None time;
    private String emailFId;
    private int id;
    private String status;
    private String comment;
    private int imageFId;
    private None date;



    public bean_CommentBean(
        None time,        String emailFId,        int id,        String status,        String comment,        int imageFId,        None date    ) {
        this.time = time;
        this.emailFId = emailFId;
        this.id = id;
        this.status = status;
        this.comment = comment;
        this.imageFId = imageFId;
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
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public int getImagefid() {
        return imageFId;
    }

    public void setImagefid(int imageFId) {
        this.imageFId = imageFId;
    }
    public None getDate() {
        return date;
    }

    public void setDate(None date) {
        this.date = date;
    }


}