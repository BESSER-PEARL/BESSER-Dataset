





import java.util.List;
import java.util.ArrayList;

public class minilang_Program  {

    private float x;
    private String angle;
    private float distance;
    private float y;



    public minilang_Program(
        float x,        String angle,        float distance,        float y    ) {
        this.x = x;
        this.angle = angle;
        this.distance = distance;
        this.y = y;
    }


    public float getX() {
        return x;
    }

    public void setX(float x) {
        this.x = x;
    }
    public String getAngle() {
        return angle;
    }

    public void setAngle(String angle) {
        this.angle = angle;
    }
    public float getDistance() {
        return distance;
    }

    public void setDistance(float distance) {
        this.distance = distance;
    }
    public float getY() {
        return y;
    }

    public void setY(float y) {
        this.y = y;
    }


}