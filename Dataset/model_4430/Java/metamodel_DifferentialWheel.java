





import java.util.List;
import java.util.ArrayList;

public class metamodel_DifferentialWheel extends Actuator {

    private int speed;
    private boolean isLeft;



    public metamodel_DifferentialWheel(
        int speed,        boolean isLeft    ) {
        super(
        );
        this.speed = speed;
        this.isLeft = isLeft;
    }


    public int getSpeed() {
        return speed;
    }

    public void setSpeed(int speed) {
        this.speed = speed;
    }
    public boolean getIsleft() {
        return isLeft;
    }

    public void setIsleft(boolean isLeft) {
        this.isLeft = isLeft;
    }


}