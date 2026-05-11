





import java.util.List;
import java.util.ArrayList;

public class roverml_DistanceSensorTrigger extends Triggered {

    private float dist;





    private roverml_Length roverml_length;




    private roverml_DistanceSensor roverml_distancesensor;


    public roverml_DistanceSensorTrigger(
        float dist    ) {
        super(
        );
        this.dist = dist;
    }


    public float getDist() {
        return dist;
    }

    public void setDist(float dist) {
        this.dist = dist;
    }

    public roverml_Length getRoverml_length() {
        return roverml_length;
    }

    public void setRoverml_length(roverml_Length roverml_length) {
        this.roverml_length = roverml_length;
    }
    public roverml_DistanceSensor getRoverml_distancesensor() {
        return roverml_distancesensor;
    }

    public void setRoverml_distancesensor(roverml_DistanceSensor roverml_distancesensor) {
        this.roverml_distancesensor = roverml_distancesensor;
    }

}