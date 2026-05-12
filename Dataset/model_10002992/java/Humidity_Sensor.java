





import java.util.List;
import java.util.ArrayList;

public class Humidity_Sensor  {

    private float CurrentValue;



    public Humidity_Sensor(
        float CurrentValue    ) {
        this.CurrentValue = CurrentValue;
    }


    public float getCurrentvalue() {
        return CurrentValue;
    }

    public void setCurrentvalue(float CurrentValue) {
        this.CurrentValue = CurrentValue;
    }


}