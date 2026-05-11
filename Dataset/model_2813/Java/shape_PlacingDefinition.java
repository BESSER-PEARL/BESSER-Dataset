





import java.util.List;
import java.util.ArrayList;

public class shape_PlacingDefinition  {

    private String offset;
    private int distance;
    private int angle;





    private shape_ConnectionDefinition shape_connectiondefinition;


    public shape_PlacingDefinition(
        String offset,        int distance,        int angle    ) {
        this.offset = offset;
        this.distance = distance;
        this.angle = angle;
    }


    public String getOffset() {
        return offset;
    }

    public void setOffset(String offset) {
        this.offset = offset;
    }
    public int getDistance() {
        return distance;
    }

    public void setDistance(int distance) {
        this.distance = distance;
    }
    public int getAngle() {
        return angle;
    }

    public void setAngle(int angle) {
        this.angle = angle;
    }

    public shape_ConnectionDefinition getShape_connectiondefinition() {
        return shape_connectiondefinition;
    }

    public void setShape_connectiondefinition(shape_ConnectionDefinition shape_connectiondefinition) {
        this.shape_connectiondefinition = shape_connectiondefinition;
    }

}