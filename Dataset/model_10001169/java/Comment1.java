





import java.util.List;
import java.util.ArrayList;

public class Comment1  {

    private String date;
    private String body;
    private String author;





    private Post1 post1;




    private User1 user1;


    public Comment1(
        String date,        String body,        String author    ) {
        this.date = date;
        this.body = body;
        this.author = author;
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

    public Post1 getPost1() {
        return post1;
    }

    public void setPost1(Post1 post1) {
        this.post1 = post1;
    }
    public User1 getUser1() {
        return user1;
    }

    public void setUser1(User1 user1) {
        this.user1 = user1;
    }

}