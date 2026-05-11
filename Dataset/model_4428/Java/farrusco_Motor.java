





import java.util.List;
import java.util.ArrayList;

public class farrusco_Motor extends Actuate {

    private int MotorLeft;
    private int MotorRight;



    public farrusco_Motor(
        int MotorLeft,        int MotorRight    ) {
        super(
        );
        this.MotorLeft = MotorLeft;
        this.MotorRight = MotorRight;
    }


    public int getMotorleft() {
        return MotorLeft;
    }

    public void setMotorleft(int MotorLeft) {
        this.MotorLeft = MotorLeft;
    }
    public int getMotorright() {
        return MotorRight;
    }

    public void setMotorright(int MotorRight) {
        this.MotorRight = MotorRight;
    }


}