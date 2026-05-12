





import java.util.List;
import java.util.ArrayList;

public class ContainerCar  {

    private float temp;
    private float cubicFeet;
    private boolean climateControlled;





    private FreightTrain freighttrain;


    public ContainerCar(
        float temp,        float cubicFeet,        boolean climateControlled    ) {
        this.temp = temp;
        this.cubicFeet = cubicFeet;
        this.climateControlled = climateControlled;
    }


    public float getTemp() {
        return temp;
    }

    public void setTemp(float temp) {
        this.temp = temp;
    }
    public float getCubicfeet() {
        return cubicFeet;
    }

    public void setCubicfeet(float cubicFeet) {
        this.cubicFeet = cubicFeet;
    }
    public boolean getClimatecontrolled() {
        return climateControlled;
    }

    public void setClimatecontrolled(boolean climateControlled) {
        this.climateControlled = climateControlled;
    }

    public FreightTrain getFreighttrain() {
        return freighttrain;
    }

    public void setFreighttrain(FreightTrain freighttrain) {
        this.freighttrain = freighttrain;
    }

}