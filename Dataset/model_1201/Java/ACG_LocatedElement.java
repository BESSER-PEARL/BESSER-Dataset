





import java.util.List;
import java.util.ArrayList;

public class ACG_LocatedElement  {

    private String commentsBefore;
    private String commentsAfter;
    private String location;



    public ACG_LocatedElement(
        String commentsBefore,        String commentsAfter,        String location    ) {
        this.commentsBefore = commentsBefore;
        this.commentsAfter = commentsAfter;
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
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }


}