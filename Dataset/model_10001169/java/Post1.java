





import java.util.List;
import java.util.ArrayList;

public class Post1  {

    private String files;
    private String body;
    private String title;
    private String author;
    private String date;





    private User1 user1;


    public Post1(
        String files,        String body,        String title,        String author,        String date    ) {
        this.files = files;
        this.body = body;
        this.title = title;
        this.author = author;
        this.date = date;
    }


    public String getFiles() {
        return files;
    }

    public void setFiles(String files) {
        this.files = files;
    }
    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }
    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }

    public User1 getUser1() {
        return user1;
    }

    public void setUser1(User1 user1) {
        this.user1 = user1;
    }

}