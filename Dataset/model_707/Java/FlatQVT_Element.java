





import java.util.List;
import java.util.ArrayList;

public class FlatQVT_Element extends Object {






    private List<Comment> comments;


    public FlatQVT_Element(
    ) {
        super(
        );
        this.comments = new ArrayList<>();
    }

    public FlatQVT_Element(
        ArrayList<Comment> comments    ) {
        this.comments = comments;
    }


    public List<Comment> getComments() {
        return comments;
    }

    public void addComment(Comment comment) {
        this.comments.add(comment);
    }

}