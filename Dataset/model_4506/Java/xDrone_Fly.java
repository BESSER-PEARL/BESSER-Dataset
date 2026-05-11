





import java.util.List;
import java.util.ArrayList;

public class xDrone_Fly  {

    private String takeoff;
    private String land;





    private xDrone_Main xdrone_main;


    public xDrone_Fly(
        String takeoff,        String land    ) {
        this.takeoff = takeoff;
        this.land = land;
    }


    public String getTakeoff() {
        return takeoff;
    }

    public void setTakeoff(String takeoff) {
        this.takeoff = takeoff;
    }
    public String getLand() {
        return land;
    }

    public void setLand(String land) {
        this.land = land;
    }

    public xDrone_Main getXdrone_main() {
        return xdrone_main;
    }

    public void setXdrone_main(xDrone_Main xdrone_main) {
        this.xdrone_main = xdrone_main;
    }

}