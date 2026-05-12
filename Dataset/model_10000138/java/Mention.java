





import java.util.List;
import java.util.ArrayList;

public class Mention  {

    private int id;
    private int user_id;
    private int post_id;





    private Reciever reciever;




    private Post post;


    public Mention(
        int id,        int user_id,        int post_id    ) {
        this.id = id;
        this.user_id = user_id;
        this.post_id = post_id;
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