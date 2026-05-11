





import java.util.List;
import java.util.ArrayList;

public class House2_TemperatureSensor extends Sensor {

    private float temp;



    public House2_TemperatureSensor(
        float temp    ) {
        super(
        );
        this.temp = temp;
    }


    public float getTemp() {
        return temp;
    }

    public void setTemp(float temp) {
        this.temp = temp;
    }


}