





import java.util.List;
import java.util.ArrayList;

public class surveillance_GunShot extends ProbableElement {

    private boolean hitsTarget;
    private float angle;





    private surveillance_Coordinate surveillance_coordinate;




    private surveillance_Coordinate surveillance_coordinate;


    public surveillance_GunShot(
        boolean hitsTarget,        float angle    ) {
        super(
        );
        this.hitsTarget = hitsTarget;
        this.angle = angle;
    }


    public boolean getHitstarget() {
        return hitsTarget;
    }

    public void setHitstarget(boolean hitsTarget) {
        this.hitsTarget = hitsTarget;
    }
    public float getAngle() {
        return angle;
    }

    public void setAngle(float angle) {
        this.angle = angle;
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