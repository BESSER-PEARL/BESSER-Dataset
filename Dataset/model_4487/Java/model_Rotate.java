





import java.util.List;
import java.util.ArrayList;

public class model_Rotate extends Command {

    private String velocity;
    private String direction;
    private float angle;



    public model_Rotate(
        String velocity,        String direction,        float angle    ) {
        super(
        );
        this.velocity = velocity;
        this.direction = direction;
        this.angle = angle;
    }


    public String getVelocity() {
        return velocity;
    }

    public void setVelocity(String velocity) {
        this.velocity = velocity;
    }
    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }
    public float getAngle() {
        return angle;
    }

    public void setAngle(float angle) {
        this.angle = angle;
    }


}