





import java.util.List;
import java.util.ArrayList;

public class bean_MessageCommentBean  {

    private int id;
    private None date;
    private None time;
    private String status;
    private String emailFId;
    private String comment;
    private int messageFId;



    public bean_MessageCommentBean(
        int id,        None date,        None time,        String status,        String emailFId,        String comment,        int messageFId    ) {
        this.id = id;
        this.date = date;
        this.time = time;
        this.status = status;
        this.emailFId = emailFId;
        this.comment = comment;
        this.messageFId = messageFId;
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
    public None getTime() {
        return time;
    }

    public void setTime(None time) {
        this.time = time;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getEmailfid() {
        return emailFId;
    }

    public void setEmailfid(String emailFId) {
        this.emailFId = emailFId;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public int getMessagefid() {
        return messageFId;
    }

    public void setMessagefid(int messageFId) {
        this.messageFId = messageFId;
    }


}