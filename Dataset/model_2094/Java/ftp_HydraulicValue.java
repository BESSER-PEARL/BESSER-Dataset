





import java.util.List;
import java.util.ArrayList;

public class ftp_HydraulicValue extends TypedPortValue {

    private boolean anyFlow;
    private float pressure;
    private boolean anyPressure;
    private float flow;



    public ftp_HydraulicValue(
        boolean anyFlow,        float pressure,        boolean anyPressure,        float flow    ) {
        super(
        );
        this.anyFlow = anyFlow;
        this.pressure = pressure;
        this.anyPressure = anyPressure;
        this.flow = flow;
    }


    public boolean getAnyflow() {
        return anyFlow;
    }

    public void setAnyflow(boolean anyFlow) {
        this.anyFlow = anyFlow;
    }
    public float getPressure() {
        return pressure;
    }

    public void setPressure(float pressure) {
        this.pressure = pressure;
    }
    public boolean getAnypressure() {
        return anyPressure;
    }

    public void setAnypressure(boolean anyPressure) {
        this.anyPressure = anyPressure;
    }
    public float getFlow() {
        return flow;
    }

    public void setFlow(float flow) {
        this.flow = flow;
    }


}