





import java.util.List;
import java.util.ArrayList;

public class fair_Division  {

    private String name;
    private String description;
    private String comments;



    public fair_Division(
        String name,        String description,        String comments    ) {
        this.name = name;
        this.description = description;
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
    public String getComments() {
        return comments;
    }

    public void setComments(String comments) {
        this.comments = comments;
    }


}