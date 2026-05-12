





import java.util.List;
import java.util.ArrayList;

public class Arduino  {






    private List<Sensor> sensors;




    private Firebase firebase;


    public Arduino(
    ) {
        this.sensors = new ArrayList<>();
    }

    public Arduino(
        ArrayList<Sensor> sensors    ) {
        this.sensors = sensors;
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