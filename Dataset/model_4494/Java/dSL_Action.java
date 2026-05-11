





import java.util.List;
import java.util.ArrayList;

public class dSL_Action  {

    private boolean driveDirection;
    private boolean steer;
    private boolean showLakes;
    private boolean blinkLights;
    private boolean probeLake;
    private boolean driveDistance;
    private String direction;



    public dSL_Action(
        boolean driveDirection,        boolean steer,        boolean showLakes,        boolean blinkLights,        boolean probeLake,        boolean driveDistance,        String direction    ) {
        this.driveDirection = driveDirection;
        this.steer = steer;
        this.showLakes = showLakes;
        this.blinkLights = blinkLights;
        this.probeLake = probeLake;
        this.driveDistance = driveDistance;
        this.direction = direction;
    }


    public boolean getDrivedirection() {
        return driveDirection;
    }

    public void setDrivedirection(boolean driveDirection) {
        this.driveDirection = driveDirection;
    }
    public boolean getSteer() {
        return steer;
    }

    public void setSteer(boolean steer) {
        this.steer = steer;
    }
    public boolean getShowlakes() {
        return showLakes;
    }

    public void setShowlakes(boolean showLakes) {
        this.showLakes = showLakes;
    }
    public boolean getBlinklights() {
        return blinkLights;
    }

    public void setBlinklights(boolean blinkLights) {
        this.blinkLights = blinkLights;
    }
    public boolean getProbelake() {
        return probeLake;
    }

    public void setProbelake(boolean probeLake) {
        this.probeLake = probeLake;
    }
    public boolean getDrivedistance() {
        return driveDistance;
    }

    public void setDrivedistance(boolean driveDistance) {
        this.driveDistance = driveDistance;
    }
    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }


}