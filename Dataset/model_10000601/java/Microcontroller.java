





import java.util.List;
import java.util.ArrayList;

public class Microcontroller  {

    private String sendData__;





    private HouseHolds households;




    private Sensor sensor;


    public Microcontroller(
        String sendData__    ) {
        this.sendData__ = sendData__;
    }


    public String getSenddata__() {
        return sendData__;
    }

    public void setSenddata__(String sendData__) {
        this.sendData__ = sendData__;
    }

    public HouseHolds getHouseholds() {
        return households;
    }

    public void setHouseholds(HouseHolds households) {
        this.households = households;
    }
    public Sensor getSensor() {
        return sensor;
    }

    public void setSensor(Sensor sensor) {
        this.sensor = sensor;
    }

}