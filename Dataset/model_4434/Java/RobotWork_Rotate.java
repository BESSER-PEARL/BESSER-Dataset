





import java.util.List;
import java.util.ArrayList;

public class RobotWork_Rotate extends Action {

    private boolean random;
    private int degrees;



    public RobotWork_Rotate(
        boolean random,        int degrees    ) {
        super(
        );
        this.random = random;
        this.degrees = degrees;
    }


    public boolean getRandom() {
        return random;
    }

    public void setRandom(boolean random) {
        this.random = random;
    }
    public int getDegrees() {
        return degrees;
    }

    public void setDegrees(int degrees) {
        this.degrees = degrees;
    }


}