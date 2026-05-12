





import java.util.List;
import java.util.ArrayList;

public class Post1  {

    private String date;
    private String body;
    private String author;
    private String title;
    private String files;





    private User1 user1;


    public Post1(
        String date,        String body,        String author,        String title,        String files    ) {
        this.date = date;
        this.body = body;
        this.author = author;
        this.title = title;
        this.files = files;
    }


    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getFiles() {
        return files;
    }

    public void setFiles(String files) {
        this.files = files;
    }

    public User1 getUser1() {
        return user1;
    }

    public void setUser1(User1 user1) {
        this.user1 = user1;
    }

}