





import java.util.List;
import java.util.ArrayList;

public class farrusco_Motors extends Actuate {

    private int MotorRight;
    private int MotorLeft;



    public farrusco_Motors(
        int MotorRight,        int MotorLeft    ) {
        super(
        );
        this.MotorRight = MotorRight;
        this.MotorLeft = MotorLeft;
    }


    public int getMotorright() {
        return MotorRight;
    }

    public void setMotorright(int MotorRight) {
        this.MotorRight = MotorRight;
    }
    public int getMotorleft() {
        return MotorLeft;
    }

    public void setMotorleft(int MotorLeft) {
        this.MotorLeft = MotorLeft;
    }


}