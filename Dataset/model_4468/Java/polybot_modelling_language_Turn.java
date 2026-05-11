





import java.util.List;
import java.util.ArrayList;

public class polybot_modelling_language_Turn extends Instruction {

    private int angle;



    public polybot_modelling_language_Turn(
        int angle    ) {
        super(
        );
        this.angle = angle;
    }


    public int getAngle() {
        return angle;
    }

    public void setAngle(int angle) {
        this.angle = angle;
    }


}