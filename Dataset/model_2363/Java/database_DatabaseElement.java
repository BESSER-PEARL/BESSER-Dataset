





import java.util.List;
import java.util.ArrayList;

public class database_DatabaseElement  {

    private String ID;
    private String comments;
    private String techID;



    public database_DatabaseElement(
        String ID,        String comments,        String techID    ) {
        this.ID = ID;
        this.comments = comments;
        this.techID = techID;
    }


    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }
    public String getComments() {
        return comments;
    }

    public void setComments(String comments) {
        this.comments = comments;
    }
    public String getTechid() {
        return techID;
    }

    public void setTechid(String techID) {
        this.techID = techID;
    }


}