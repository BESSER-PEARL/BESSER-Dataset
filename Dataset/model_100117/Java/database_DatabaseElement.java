





import java.util.List;
import java.util.ArrayList;

public class database_DatabaseElement  {

    private String ID;
    private String techID;
    private String comments;



    public database_DatabaseElement(
        String ID,        String techID,        String comments    ) {
        this.ID = ID;
        this.techID = techID;
        this.comments = comments;
    }


    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }
    public String getTechid() {
        return techID;
    }

    public void setTechid(String techID) {
        this.techID = techID;
    }
    public String getComments() {
        return comments;
    }

    public void setComments(String comments) {
        this.comments = comments;
    }


}