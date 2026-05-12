





import java.util.List;
import java.util.ArrayList;

public class database_DatabaseElement  {

    private String comments;
    private String ID;



    public database_DatabaseElement(
        String comments,        String ID    ) {
        this.comments = comments;
        this.ID = ID;
    }


    public String getComments() {
        return comments;
    }

    public void setComments(String comments) {
        this.comments = comments;
    }
    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }


}