





import java.util.List;
import java.util.ArrayList;

public class emfta_FTAModel  {

    private String comments;
    private String name;
    private String description;



    public emfta_FTAModel(
        String comments,        String name,        String description    ) {
        this.comments = comments;
        this.name = name;
        this.description = description;
    }


    public String getComments() {
        return comments;
    }

    public void setComments(String comments) {
        this.comments = comments;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }


}