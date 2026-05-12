





import java.util.List;
import java.util.ArrayList;

public class Comment  {

    private int comment_id;
    private String creation_date;
    private int content;
    private int id;
    private int post_id;
    private int user_id;





    private List<Comment> comments;




    private Post post;




    private Reciever reciever;


    public Comment(
        int comment_id,        String creation_date,        int content,        int id,        int post_id,        int user_id    ) {
        this.comment_id = comment_id;
        this.creation_date = creation_date;
        this.content = content;
        this.id = id;
        this.post_id = post_id;
        this.user_id = user_id;
        this.comments = new ArrayList<>();
    }

    public Comment(
        int comment_id,        String creation_date,        int content,        int id,        int post_id,        int user_id        ArrayList<Comment> comments    ) {
        this.comment_id = comment_id;
        this.creation_date = creation_date;
        this.content = content;
        this.id = id;
        this.post_id = post_id;
        this.user_id = user_id;
        this.comments = comments;
    }

    public int getComment_id() {
        return comment_id;
    }

    public void setComment_id(int comment_id) {
        this.comment_id = comment_id;
    }
    public String getCreation_date() {
        return creation_date;
    }

    public void setCreation_date(String creation_date) {
        this.creation_date = creation_date;
    }
    public int getContent() {
        return content;
    }

    public void setContent(int content) {
        this.content = content;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getPost_id() {
        return post_id;
    }

    public void setPost_id(int post_id) {
        this.post_id = post_id;
    }
    public int getUser_id() {
        return user_id;
    }

    public void setUser_id(int user_id) {
        this.user_id = user_id;
    }

    public List<Comment> getComments() {
        return comments;
    }

    public void addComment(Comment comment) {
        this.comments.add(comment);
    }
    public Post getPost() {
        return post;
    }

    public void setPost(Post post) {
        this.post = post;
    }
    public Reciever getReciever() {
        return reciever;
    }

    public void setReciever(Reciever reciever) {
        this.reciever = reciever;
    }

}