





import java.util.List;
import java.util.ArrayList;

public class XPath_LocatedElement  {

    private String commentsAfter;
    private String location;
    private String commentsBefore;



    public XPath_LocatedElement(
        String commentsAfter,        String location,        String commentsBefore    ) {
        this.commentsAfter = commentsAfter;
        this.location = location;
        this.commentsBefore = commentsBefore;
    }


    public String getCommentsafter() {
        return commentsAfter;
    }

    public void setCommentsafter(String commentsAfter) {
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


}