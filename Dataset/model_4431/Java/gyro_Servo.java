





import java.util.List;
import java.util.ArrayList;

public class gyro_Servo extends Actuate {

    private int step;
    private int maximalPosition;
    private int minimalPosition;



    public gyro_Servo(
        int step,        int maximalPosition,        int minimalPosition    ) {
        super(
        );
        this.step = step;
        this.maximalPosition = maximalPosition;
        this.minimalPosition = minimalPosition;
    }


    public int getStep() {
        return step;
    }

    public void setStep(int step) {
        this.step = step;
    }
    public int getMaximalposition() {
        return maximalPosition;
    }

    public void setMaximalposition(int maximalPosition) {
        this.maximalPosition = maximalPosition;
    }
    public int getMinimalposition() {
        return minimalPosition;
    }

    public void setMinimalposition(int minimalPosition) {
        this.minimalPosition = minimalPosition;
    }


}