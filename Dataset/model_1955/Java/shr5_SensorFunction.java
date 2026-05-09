





import java.util.List;
import java.util.ArrayList;

public class shr5_SensorFunction extends Quelle, Beschreibbar {

    private int maxRange;





    private shr5_Sensor shr5_sensor;


    public shr5_SensorFunction(
        int maxRange    ) {
        super(
        );
        this.maxRange = maxRange;
    }


    public int getMaxrange() {
        return maxRange;
    }

    public void setMaxrange(int maxRange) {
        this.maxRange = maxRange;
    }

    public shr5_Sensor getShr5_sensor() {
        return shr5_sensor;
    }

    public void setShr5_sensor(shr5_Sensor shr5_sensor) {
        this.shr5_sensor = shr5_sensor;
    }

}