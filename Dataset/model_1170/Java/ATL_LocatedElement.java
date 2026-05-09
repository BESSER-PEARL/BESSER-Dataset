





import java.util.List;
import java.util.ArrayList;

public class ATL_LocatedElement  {

    private String commentsAfter;
    private String commentsBefore;
    private String location;



    public ATL_LocatedElement(
        String commentsAfter,        String commentsBefore,        String location    ) {
        this.commentsAfter = commentsAfter;
        this.commentsBefore = commentsBefore;
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
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }


}