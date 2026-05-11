





import java.util.List;
import java.util.ArrayList;

public class FPath_LocatedElement  {

    private String location;
    private String commentsBefore;
    private String commentsAfter;



    public FPath_LocatedElement(
        String location,        String commentsBefore,        String commentsAfter    ) {
        this.location = location;
        this.commentsBefore = commentsBefore;
        this.commentsAfter = commentsAfter;
    }


    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getCommentsbefore() {
        return commentsBefore;
    }

    public void setCommentsbefore(String commentsBefore) {
        this.commentsBefore = commentsBefore;
    }
    public String getCommentsafter() {
        return commentsAfter;
    }

    public void setCommentsafter(String commentsAfter) {
        this.commentsAfter = commentsAfter;
    }


}