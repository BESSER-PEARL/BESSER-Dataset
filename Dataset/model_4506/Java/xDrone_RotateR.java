





import java.util.List;
import java.util.ArrayList;

public class xDrone_RotateR extends Command {

    private String angle;



    public xDrone_RotateR(
        String angle    ) {
        super(
        );
        this.angle = angle;
    }


    public String getAngle() {
        return angle;
    }

    public void setAngle(String angle) {
        this.angle = angle;
    }


}