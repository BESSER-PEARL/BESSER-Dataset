





import java.util.List;
import java.util.ArrayList;

public class location_Area  {

    private String boundary;
    private String comments;
    private String name;





    private location_Location location_location;


    public location_Area(
        String boundary,        String comments,        String name    ) {
        this.boundary = boundary;
        this.comments = comments;
        this.name = name;
    }


    public String getBoundary() {
        return boundary;
    }

    public void setBoundary(String boundary) {
        this.boundary = boundary;
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

    public location_Location getLocation_location() {
        return location_location;
    }

    public void setLocation_location(location_Location location_location) {
        this.location_location = location_location;
    }

}