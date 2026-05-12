





import java.util.List;
import java.util.ArrayList;

public class Interior_Container  {

    private int WorkMode;





    private Sensor sensor;


    public Interior_Container(
        int WorkMode    ) {
        this.WorkMode = WorkMode;
    }


    public int getWorkmode() {
        return WorkMode;
    }

    public void setWorkmode(int WorkMode) {
        this.WorkMode = WorkMode;
    }

    public Sensor getSensor() {
        return sensor;
    }

    public void setSensor(Sensor sensor) {
        this.sensor = sensor;
    }

}