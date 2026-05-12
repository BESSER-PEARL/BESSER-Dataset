





import java.util.List;
import java.util.ArrayList;

public class presentation_PlayType  {

    private String speed;
    private String shapeId;



    public presentation_PlayType(
        String speed,        String shapeId    ) {
        this.speed = speed;
        this.shapeId = shapeId;
    }


    public String getSpeed() {
        return speed;
    }

    public void setSpeed(String speed) {
        this.speed = speed;
    }
    public String getShapeid() {
        return shapeId;
    }

    public void setShapeid(String shapeId) {
        this.shapeId = shapeId;
    }


}