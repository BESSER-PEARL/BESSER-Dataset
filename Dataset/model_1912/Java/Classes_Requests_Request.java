





import java.util.List;
import java.util.ArrayList;

public class Classes_Requests_Request  {

    private String description;
    private String id;
    private String isResolved;



    public Classes_Requests_Request(
        String description,        String id,        String isResolved    ) {
        this.description = description;
        this.id = id;
        this.isResolved = isResolved;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getIsresolved() {
        return isResolved;
    }

    public void setIsresolved(String isResolved) {
        this.isResolved = isResolved;
    }


}