





import java.util.List;
import java.util.ArrayList;

public class Classes_Feedback_Feedback  {

    private String id;
    private String isResolved;
    private String isNoted;
    private String description;



    public Classes_Feedback_Feedback(
        String id,        String isResolved,        String isNoted,        String description    ) {
        this.id = id;
        this.isResolved = isResolved;
        this.isNoted = isNoted;
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
    public String getIsnoted() {
        return isNoted;
    }

    public void setIsnoted(String isNoted) {
        this.isNoted = isNoted;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }


}