





import java.util.List;
import java.util.ArrayList;

public class model_Turn extends ContinuosAction, RotorAction, RandomAction {

    private String direction;
    private float degrees;



    public model_Turn(
        String direction,        float degrees    ) {
        super(
        );
        this.direction = direction;
        this.degrees = degrees;
    }


    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }
    public float getDegrees() {
        return degrees;
    }

    public void setDegrees(float degrees) {
        this.degrees = degrees;
    }


}