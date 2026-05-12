





import java.util.List;
import java.util.ArrayList;

public class Comment  {

    private String date;
    private String comment;
    private String userName;





    private Post post;


    public Comment(
        String date,        String comment,        String userName    ) {
        this.date = date;
        this.comment = comment;
        this.userName = userName;
    }


    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getUsername() {
        return userName;
    }

    public void setUsername(String userName) {
        this.userName = userName;
    }

    public Post getPost() {
        return post;
    }

    public void setPost(Post post) {
        this.post = post;
    }

}