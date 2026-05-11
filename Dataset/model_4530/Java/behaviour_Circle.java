





import java.util.List;
import java.util.ArrayList;

public class behaviour_Circle extends Move {

    private float duration;
    private float radius;
    private boolean clockwise;
    private float altitude;





    private behaviour_Coordinate behaviour_coordinate;


    public behaviour_Circle(
        float duration,        float radius,        boolean clockwise,        float altitude    ) {
        super(
        );
        this.duration = duration;
        this.radius = radius;
        this.clockwise = clockwise;
        this.altitude = altitude;
    }


    public float getDuration() {
        return duration;
    }

    public void setDuration(float duration) {
        this.duration = duration;
    }
    public float getRadius() {
        return radius;
    }

    public void setRadius(float radius) {
        this.radius = radius;
    }
    public boolean getClockwise() {
        return clockwise;
    }

    public void setClockwise(boolean clockwise) {
        this.clockwise = clockwise;
    }
    public float getAltitude() {
        return altitude;
    }

    public void setAltitude(float altitude) {
        this.altitude = altitude;
    }

    public behaviour_Coordinate getBehaviour_coordinate() {
        return behaviour_coordinate;
    }

    public void setBehaviour_coordinate(behaviour_Coordinate behaviour_coordinate) {
        this.behaviour_coordinate = behaviour_coordinate;
    }

}