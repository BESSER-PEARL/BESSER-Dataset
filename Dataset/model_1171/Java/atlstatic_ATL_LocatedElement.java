





import java.util.List;
import java.util.ArrayList;

public class atlstatic_ATL_LocatedElement  {

    private String location;
    private String commentsAfter;
    private String commentsBefore;



    public atlstatic_ATL_LocatedElement(
        String location,        String commentsAfter,        String commentsBefore    ) {
        this.location = location;
        this.commentsAfter = commentsAfter;
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
    public String getCommentsbefore() {
        return commentsBefore;
    }

    public void setCommentsbefore(String commentsBefore) {
        this.commentsBefore = commentsBefore;
    }


}