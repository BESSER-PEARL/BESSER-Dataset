





import java.util.List;
import java.util.ArrayList;

public class roverml_GPSTrigger extends Triggered {

    private float x;
    private float y;





    private roverml_GPS roverml_gps;


    public roverml_GPSTrigger(
        float x,        float y    ) {
        super(
        );
        this.x = x;
        this.y = y;
    }


    public float getX() {
        return x;
    }

    public void setX(float x) {
        this.x = x;
    }
    public float getY() {
        return y;
    }

    public void setY(float y) {
        this.y = y;
    }

    public roverml_GPS getRoverml_gps() {
        return roverml_gps;
    }

    public void setRoverml_gps(roverml_GPS roverml_gps) {
        this.roverml_gps = roverml_gps;
    }

}