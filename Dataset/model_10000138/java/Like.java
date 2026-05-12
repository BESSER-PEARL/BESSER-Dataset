





import java.util.List;
import java.util.ArrayList;

public class Like  {

    private String date_sent;
    private int id;
    private int user_id;
    private int post_id;





    private Reciever reciever;




    private Post post;


    public Like(
        String date_sent,        int id,        int user_id,        int post_id    ) {
        this.date_sent = date_sent;
        this.id = id;
        this.user_id = user_id;
        this.post_id = post_id;
    }


    public String getDate_sent() {
        return date_sent;
    }

    public void setDate_sent(String date_sent) {
        this.date_sent = date_sent;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getUser_id() {
        return user_id;
    }

    public void setUser_id(int user_id) {
        this.user_id = user_id;
    }
    public int getPost_id() {
        return post_id;
    }

    public void setPost_id(int post_id) {
        this.post_id = post_id;
    }

    public Reciever getReciever() {
        return reciever;
    }

    public void setReciever(Reciever reciever) {
        this.reciever = reciever;
    }
    public Post getPost() {
        return post;
    }

    public void setPost(Post post) {
        this.post = post;
    }

}