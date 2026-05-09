





import java.util.List;
import java.util.ArrayList;

public class atlext_ATL_LocatedElement  {

    private String commentsBefore;
    private String fileLocation;
    private String commentsAfter;
    private String fileObject;
    private String location;



    public atlext_ATL_LocatedElement(
        String commentsBefore,        String fileLocation,        String commentsAfter,        String fileObject,        String location    ) {
        this.commentsBefore = commentsBefore;
        this.fileLocation = fileLocation;
        this.commentsAfter = commentsAfter;
        this.fileObject = fileObject;
        this.location = location;
    }


    public String getCommentsbefore() {
        return commentsBefore;
    }

    public void setCommentsbefore(String commentsBefore) {
        this.commentsBefore = commentsBefore;
    }
    public String getFilelocation() {
        return fileLocation;
    }

    public void setFilelocation(String fileLocation) {
        this.fileLocation = fileLocation;
    }
    public String getCommentsafter() {
        return commentsAfter;
    }

    public void setCommentsafter(String commentsAfter) {
        this.commentsAfter = commentsAfter;
    }
    public String getFileobject() {
        return fileObject;
    }

    public void setFileobject(String fileObject) {
        this.fileObject = fileObject;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }


}