





import java.util.List;
import java.util.ArrayList;

public class Curtains  {

    private int CurtaiunID;





    private Sensor sensor;


    public Curtains(
        int CurtaiunID    ) {
        this.CurtaiunID = CurtaiunID;
    }


    public int getCurtaiunid() {
        return CurtaiunID;
    }

    public void setCurtaiunid(int CurtaiunID) {
        this.CurtaiunID = CurtaiunID;
    }

    public Sensor getSensor() {
        return sensor;
    }

    public void setSensor(Sensor sensor) {
        this.sensor = sensor;
    }

}