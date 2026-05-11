





import java.util.List;
import java.util.ArrayList;

public class roverDSL_Robot  {

    private int maxAngle;
    private int defaultSpeed;
    private int minAngle;
    private int slowSpeed;



    public roverDSL_Robot(
        int maxAngle,        int defaultSpeed,        int minAngle,        int slowSpeed    ) {
        this.maxAngle = maxAngle;
        this.defaultSpeed = defaultSpeed;
        this.minAngle = minAngle;
        this.slowSpeed = slowSpeed;
    }


    public int getMaxangle() {
        return maxAngle;
    }

    public void setMaxangle(int maxAngle) {
        this.maxAngle = maxAngle;
    }
    public int getDefaultspeed() {
        return defaultSpeed;
    }

    public void setDefaultspeed(int defaultSpeed) {
        this.defaultSpeed = defaultSpeed;
    }
    public int getMinangle() {
        return minAngle;
    }

    public void setMinangle(int minAngle) {
        this.minAngle = minAngle;
    }
    public int getSlowspeed() {
        return slowSpeed;
    }

    public void setSlowspeed(int slowSpeed) {
        this.slowSpeed = slowSpeed;
    }


}