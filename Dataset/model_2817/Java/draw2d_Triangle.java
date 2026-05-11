





import java.util.List;
import java.util.ArrayList;

public class draw2d_Triangle extends Shape {

    private String direction;
    private String orientation;



    public draw2d_Triangle(
        String direction,        String orientation    ) {
        super(
        );
        this.direction = direction;
        this.orientation = orientation;
    }


    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }
    public String getOrientation() {
        return orientation;
    }

    public void setOrientation(String orientation) {
        this.orientation = orientation;
    }


}