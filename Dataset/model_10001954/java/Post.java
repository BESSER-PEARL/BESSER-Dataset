





import java.util.List;
import java.util.ArrayList;

public class Post  {

    private String Privacy;
    private int ID_Post;
    private String Info;
    private int ID_Page;
    private String Mail;



    public Post(
        String Privacy,        int ID_Post,        String Info,        int ID_Page,        String Mail    ) {
        this.Privacy = Privacy;
        this.ID_Post = ID_Post;
        this.Info = Info;
        this.ID_Page = ID_Page;
        this.Mail = Mail;
    }


    public String getPrivacy() {
        return Privacy;
    }

    public void setPrivacy(String Privacy) {
        this.Privacy = Privacy;
    }
    public int getId_post() {
        return ID_Post;
    }

    public void setId_post(int ID_Post) {
        this.ID_Post = ID_Post;
    }
    public String getInfo() {
        return Info;
    }

    public void setInfo(String Info) {
        this.Info = Info;
    }
    public int getId_page() {
        return ID_Page;
    }

    public void setId_page(int ID_Page) {
        this.ID_Page = ID_Page;
    }
    public String getMail() {
        return Mail;
    }

    public void setMail(String Mail) {
        this.Mail = Mail;
    }


}