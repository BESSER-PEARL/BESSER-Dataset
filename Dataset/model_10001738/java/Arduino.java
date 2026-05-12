





import java.util.List;
import java.util.ArrayList;

public class Arduino  {

    private String MicID;





    private List<Sensor> sensors;




    private Firebase firebase;


    public Arduino(
        String MicID    ) {
        this.MicID = MicID;
        this.sensors = new ArrayList<>();
    }

    public Arduino(
        String MicID        ArrayList<Sensor> sensors    ) {
        this.MicID = MicID;
        this.sensors = sensors;
    }

    public String getMicid() {
        return MicID;
    }

    public void setMicid(String MicID) {
        this.MicID = MicID;
    }

    public List<Sensor> getSensors() {
        return sensors;
    }

    public void addSensor(Sensor sensor) {
        this.sensors.add(sensor);
    }
    public Firebase getFirebase() {
        return firebase;
    }

    public void setFirebase(Firebase firebase) {
        this.firebase = firebase;
    }

}