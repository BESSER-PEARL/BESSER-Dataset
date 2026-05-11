





import java.util.List;
import java.util.ArrayList;

public class gyro_Motor extends Actuate {

    private int leftMotor;
    private int rightMotor;



    public gyro_Motor(
        int leftMotor,        int rightMotor    ) {
        super(
        );
        this.leftMotor = leftMotor;
        this.rightMotor = rightMotor;
    }


    public int getLeftmotor() {
        return leftMotor;
    }

    public void setLeftmotor(int leftMotor) {
        this.leftMotor = leftMotor;
    }
    public int getRightmotor() {
        return rightMotor;
    }

    public void setRightmotor(int rightMotor) {
        this.rightMotor = rightMotor;
    }


}