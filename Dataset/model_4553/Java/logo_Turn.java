





import java.util.List;
import java.util.ArrayList;

public class logo_Turn extends Command {

    private float angle;



    public logo_Turn(
        float angle    ) {
        super(
        );
        this.angle = angle;
    }


    public float getAngle() {
        return angle;
    }

    public void setAngle(float angle) {
        this.angle = angle;
    }


}