





import java.util.List;
import java.util.ArrayList;

public class dbca_CommentedElement extends Element {

    private String comment;



    public dbca_CommentedElement(
        String comment    ) {
        super(
        );
        this.comment = comment;
    }


    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }


}