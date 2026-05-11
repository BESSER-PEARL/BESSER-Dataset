





import java.util.List;
import java.util.ArrayList;

public class minidrone_Turn extends Instruction {

    private int angle;



    public minidrone_Turn(
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