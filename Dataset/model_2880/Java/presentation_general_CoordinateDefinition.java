





import java.util.List;
import java.util.ArrayList;

public class presentation_general_CoordinateDefinition  {

    private String coordinate;
    private String right_bottom;
    private String type;



    public presentation_general_CoordinateDefinition(
        String coordinate,        String right_bottom,        String type    ) {
        this.coordinate = coordinate;
        this.right_bottom = right_bottom;
        this.type = type;
    }


    public String getCoordinate() {
        return coordinate;
    }

    public void setCoordinate(String coordinate) {
        this.coordinate = coordinate;
    }
    public String getRight_bottom() {
        return right_bottom;
    }

    public void setRight_bottom(String right_bottom) {
        this.right_bottom = right_bottom;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}