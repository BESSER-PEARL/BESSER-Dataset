





import java.util.List;
import java.util.ArrayList;

public class smm_Observation extends SmmElement {

    private String tool;
    private String observer;
    private String whenObserved;





    private smm_Measurement smm_measurement;


    public smm_Observation(
        String tool,        String observer,        String whenObserved    ) {
        super(
        );
        this.tool = tool;
        this.observer = observer;
        this.whenObserved = whenObserved;
    }


    public String getTool() {
        return tool;
    }

    public void setTool(String tool) {
        this.tool = tool;
    }
    public String getObserver() {
        return observer;
    }

    public void setObserver(String observer) {
        this.observer = observer;
    }
    public String getWhenobserved() {
        return whenObserved;
    }

    public void setWhenobserved(String whenObserved) {
        this.whenObserved = whenObserved;
    }

    public smm_Measurement getSmm_measurement() {
        return smm_measurement;
    }

    public void setSmm_measurement(smm_Measurement smm_measurement) {
        this.smm_measurement = smm_measurement;
    }

}