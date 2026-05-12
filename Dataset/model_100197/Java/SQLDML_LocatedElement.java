





import java.util.List;
import java.util.ArrayList;

public class SQLDML_LocatedElement  {

    private String commentsBefore;
    private String location;
    private String commentsAfter;



    public SQLDML_LocatedElement(
        String commentsBefore,        String location,        String commentsAfter    ) {
        this.commentsBefore = commentsBefore;
        this.location = location;
        this.commentsAfter = commentsAfter;
    }


    public String getCommentsbefore() {
        return commentsBefore;
    }

    public void setCommentsbefore(String commentsBefore) {
        this.commentsBefore = commentsBefore;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getCommentsafter() {
        return commentsAfter;
    }

    public void setCommentsafter(String commentsAfter) {
        this.commentsAfter = commentsAfter;
    }


}