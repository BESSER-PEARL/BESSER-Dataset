





import java.util.List;
import java.util.ArrayList;

public class ContainerCar  {

    private boolean climateControlled;
    private float cubicFeet;
    private float temp;





    private FreightTrain freighttrain;


    public ContainerCar(
        boolean climateControlled,        float cubicFeet,        float temp    ) {
        this.climateControlled = climateControlled;
        this.cubicFeet = cubicFeet;
        this.temp = temp;
    }


    public boolean getClimatecontrolled() {
        return climateControlled;
    }

    public void setClimatecontrolled(boolean climateControlled) {
        this.climateControlled = climateControlled;
    }
    public float getCubicfeet() {
        return cubicFeet;
    }

    public void setCubicfeet(float cubicFeet) {
        this.cubicFeet = cubicFeet;
    }
    public float getTemp() {
        return temp;
    }

    public void setTemp(float temp) {
        this.temp = temp;
    }

    public FreightTrain getFreighttrain() {
        return freighttrain;
    }

    public void setFreighttrain(FreightTrain freighttrain) {
        this.freighttrain = freighttrain;
    }

}