





import java.util.List;
import java.util.ArrayList;

public class iotdsl_Delay  {

    private int time;
    private String unit;



    public iotdsl_Delay(
        int time,        String unit    ) {
        this.time = time;
        this.unit = unit;
    }


    public int getTime() {
        return time;
    }

    public void setTime(int time) {
        this.time = time;
    }
    public String getUnit() {
        return unit;
    }

    public void setUnit(String unit) {
        this.unit = unit;
    }


}