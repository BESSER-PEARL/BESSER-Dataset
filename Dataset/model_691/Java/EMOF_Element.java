





import java.util.List;
import java.util.ArrayList;

public class EMOF_Element extends Object {






    private List<Comment> comments;


    public EMOF_Element(
    ) {
        super(
        );
        this.comments = new ArrayList<>();
    }

    public EMOF_Element(
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