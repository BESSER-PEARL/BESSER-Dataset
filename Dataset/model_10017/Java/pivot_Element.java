





import java.util.List;
import java.util.ArrayList;

public class pivot_Element extends Visitable {






    private List<pivot_Comment> pivot_comments;




    private pivot_Comment pivot_comment;




    private pivot_Element pivot_element;




    private pivot_Comment pivot_comment;




    private List<pivot_Comment> pivot_comments;


    public pivot_Element(
    ) {
        super(
        );
        this.pivot_comments = new ArrayList<>();
        this.pivot_comments = new ArrayList<>();
    }

    public pivot_Element(
        ArrayList<pivot_Comment> pivot_comments,        ArrayList<pivot_Comment> pivot_comments    ) {
        this.pivot_comments = pivot_comments;
        this.pivot_comments = pivot_comments;
    }


    public List<pivot_Comment> getPivot_comments() {
        return pivot_comments;
    }

    public void addPivot_comment(Pivot_comment pivot_comment) {
        this.pivot_comments.add(pivot_comment);
    }
    public pivot_Comment getPivot_comment() {
        return pivot_comment;
    }

    public void setPivot_comment(pivot_Comment pivot_comment) {
        this.pivot_comment = pivot_comment;
    }
    public pivot_Element getPivot_element() {
        return pivot_element;
    }

    public void setPivot_element(pivot_Element pivot_element) {
        this.pivot_element = pivot_element;
    }
    public pivot_Comment getPivot_comment() {
        return pivot_comment;
    }

    public void setPivot_comment(pivot_Comment pivot_comment) {
        this.pivot_comment = pivot_comment;
    }
    public List<pivot_Comment> getPivot_comments() {
        return pivot_comments;
    }

    public void addPivot_comment(Pivot_comment pivot_comment) {
        this.pivot_comments.add(pivot_comment);
    }

}