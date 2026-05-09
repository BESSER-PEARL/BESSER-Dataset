





import java.util.List;
import java.util.ArrayList;

public class atlext_ATL_LocatedElement  {

    private String fileObject;
    private String commentsAfter;
    private String location;
    private String fileLocation;
    private String commentsBefore;



    public atlext_ATL_LocatedElement(
        String fileObject,        String commentsAfter,        String location,        String fileLocation,        String commentsBefore    ) {
        this.fileObject = fileObject;
        this.commentsAfter = commentsAfter;
        this.location = location;
        this.fileLocation = fileLocation;
        this.commentsBefore = commentsBefore;
    }


    public String getFileobject() {
        return fileObject;
    }

    public void setFileobject(String fileObject) {
        this.fileObject = fileObject;
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
    public String getFilelocation() {
        return fileLocation;
    }

    public void setFilelocation(String fileLocation) {
        this.fileLocation = fileLocation;
    }
    public String getCommentsbefore() {
        return commentsBefore;
    }

    public void setCommentsbefore(String commentsBefore) {
        this.commentsBefore = commentsBefore;
    }


}