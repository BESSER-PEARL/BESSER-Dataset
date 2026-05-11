





import java.util.List;
import java.util.ArrayList;

public class draw2d_XYAnchor extends ConnectionAnchor {

    private String location;



    public draw2d_XYAnchor(
        String location    ) {
        super(
        );
        this.location = location;
    }


    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }


}