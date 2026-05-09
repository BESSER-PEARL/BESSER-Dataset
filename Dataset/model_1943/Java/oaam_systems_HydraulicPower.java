





import java.util.List;
import java.util.ArrayList;

public class oaam_systems_HydraulicPower extends InformationPower {

    private float pressure;
    private float massFlowRate;



    public oaam_systems_HydraulicPower(
        float pressure,        float massFlowRate    ) {
        super(
        );
        this.pressure = pressure;
        this.massFlowRate = massFlowRate;
    }


    public float getPressure() {
        return pressure;
    }

    public void setPressure(float pressure) {
        this.pressure = pressure;
    }
    public float getMassflowrate() {
        return massFlowRate;
    }

    public void setMassflowrate(float massFlowRate) {
        this.massFlowRate = massFlowRate;
    }


}