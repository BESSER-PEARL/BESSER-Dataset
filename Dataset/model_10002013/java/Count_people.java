





import java.util.List;
import java.util.ArrayList;

public class Count_people  {

    private int _attr;





    private Sensor sensor;


    public Count_people(
        int _attr    ) {
        this._attr = _attr;
    }


    public int get_attr() {
        return _attr;
    }

    public void set_attr(int _attr) {
        this._attr = _attr;
    }

    public Sensor getSensor() {
        return sensor;
    }

    public void setSensor(Sensor sensor) {
        this.sensor = sensor;
    }

}