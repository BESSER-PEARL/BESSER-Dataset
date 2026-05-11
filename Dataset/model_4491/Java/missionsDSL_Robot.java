





import java.util.List;
import java.util.ArrayList;

public class missionsDSL_Robot  {

    private int slowSpeed;
    private int minAngle;
    private int refreshRate;
    private int maxAngle;
    private int defaultSpeed;
    private String slaveAddress;



    public missionsDSL_Robot(
        int slowSpeed,        int minAngle,        int refreshRate,        int maxAngle,        int defaultSpeed,        String slaveAddress    ) {
        this.slowSpeed = slowSpeed;
        this.minAngle = minAngle;
        this.refreshRate = refreshRate;
        this.maxAngle = maxAngle;
        this.defaultSpeed = defaultSpeed;
        this.slaveAddress = slaveAddress;
    }


    public int getSlowspeed() {
        return slowSpeed;
    }

    public void setSlowspeed(int slowSpeed) {
        this.slowSpeed = slowSpeed;
    }
    public int getMinangle() {
        return minAngle;
    }

    public void setMinangle(int minAngle) {
        this.minAngle = minAngle;
    }
    public int getRefreshrate() {
        return refreshRate;
    }

    public void setRefreshrate(int refreshRate) {
        this.refreshRate = refreshRate;
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
    public String getSlaveaddress() {
        return slaveAddress;
    }

    public void setSlaveaddress(String slaveAddress) {
        this.slaveAddress = slaveAddress;
    }


}