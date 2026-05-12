





import java.util.List;
import java.util.ArrayList;

public class Item  {






    private User user;




    private List<Hashtag> hashtags;




    private List<Comment> comments;


    public Item(
    ) {
        this.hashtags = new ArrayList<>();
        this.comments = new ArrayList<>();
    }

    public Item(
        ArrayList<Hashtag> hashtags,        ArrayList<Comment> comments    ) {
        this.hashtags = hashtags;
        this.comments = comments;
    }


    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }
    public List<Hashtag> getHashtags() {
        return hashtags;
    }

    public void addHashtag(Hashtag hashtag) {
        this.hashtags.add(hashtag);
    }
    public List<Comment> getComments() {
        return comments;
    }

    public void addComment(Comment comment) {
        this.comments.add(comment);
    }

}