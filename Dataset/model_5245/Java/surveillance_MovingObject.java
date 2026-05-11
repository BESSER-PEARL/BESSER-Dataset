





import java.util.List;
import java.util.ArrayList;

public class surveillance_MovingObject  {

    private float angle;
    private float width;
    private float speed;





    private surveillance_Coordinate surveillance_coordinate;




    private surveillance_Coordinate surveillance_coordinate;


    public surveillance_MovingObject(
        float angle,        float width,        float speed    ) {
        this.angle = angle;
        this.width = width;
        this.speed = speed;
    }


    public float getAngle() {
        return angle;
    }

    public void setAngle(float angle) {
        this.angle = angle;
    }
    public float getWidth() {
        return width;
    }

    public void setWidth(float width) {
        this.width = width;
    }
    public float getSpeed() {
        return speed;
    }

    public void setSpeed(float speed) {
        this.speed = speed;
    }

    public surveillance_Coordinate getSurveillance_coordinate() {
        return surveillance_coordinate;
    }

    public void setSurveillance_coordinate(surveillance_Coordinate surveillance_coordinate) {
        this.surveillance_coordinate = surveillance_coordinate;
    }
    public surveillance_Coordinate getSurveillance_coordinate() {
        return surveillance_coordinate;
    }

    public void setSurveillance_coordinate(surveillance_Coordinate surveillance_coordinate) {
        this.surveillance_coordinate = surveillance_coordinate;
    }

}