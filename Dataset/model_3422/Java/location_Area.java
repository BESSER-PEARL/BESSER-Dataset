





import java.util.List;
import java.util.ArrayList;

public class location_Area  {

    private String comments;
    private String boundary;
    private String name;



    public location_Area(
        String comments,        String boundary,        String name    ) {
        this.comments = comments;
        this.boundary = boundary;
        this.name = name;
    }


    public String getComments() {
        return comments;
    }

    public void setComments(String comments) {
        this.comments = comments;
    }
    public String getBoundary() {
        return boundary;
    }

    public void setBoundary(String boundary) {
        this.boundary = boundary;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}