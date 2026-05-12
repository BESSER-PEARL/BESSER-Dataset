





import java.util.List;
import java.util.ArrayList;

public class Arduino  {






    private Firebase firebase;




    private List<Sensor> sensors;


    public Arduino(
    ) {
        this.sensors = new ArrayList<>();
    }

    public Arduino(
        ArrayList<Sensor> sensors    ) {
        this.sensors = sensors;
    }


    public Firebase getFirebase() {
        return firebase;
    }

    public void setFirebase(Firebase firebase) {
        this.firebase = firebase;
    }
    public List<Sensor> getSensors() {
        return sensors;
    }

    public void addSensor(Sensor sensor) {
        this.sensors.add(sensor);
    }

}