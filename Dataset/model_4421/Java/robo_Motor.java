





import java.util.List;
import java.util.ArrayList;

public class robo_Motor  {

    private boolean reversed;
    private float speed;
    private String port;
    private String type;





    private robo_Setup robo_setup;




    private robo_Setup robo_setup;


    public robo_Motor(
        boolean reversed,        float speed,        String port,        String type    ) {
        this.reversed = reversed;
        this.speed = speed;
        this.port = port;
        this.type = type;
    }


    public boolean getReversed() {
        return reversed;
    }

    public void setReversed(boolean reversed) {
        this.reversed = reversed;
    }
    public float getSpeed() {
        return speed;
    }

    public void setSpeed(float speed) {
        this.speed = speed;
    }
    public String getPort() {
        return port;
    }

    public void setPort(String port) {
        this.port = port;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public robo_Setup getRobo_setup() {
        return robo_setup;
    }

    public void setRobo_setup(robo_Setup robo_setup) {
        this.robo_setup = robo_setup;
    }
    public robo_Setup getRobo_setup() {
        return robo_setup;
    }

    public void setRobo_setup(robo_Setup robo_setup) {
        this.robo_setup = robo_setup;
    }

}