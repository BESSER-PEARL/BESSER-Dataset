





import java.util.List;
import java.util.ArrayList;

public class smm_Observation extends SmmElement {

    private String observer;
    private String tool;
    private String whenObserved;





    private smm_Measurement smm_measurement;


    public smm_Observation(
        String observer,        String tool,        String whenObserved    ) {
        super(
        );
        this.observer = observer;
        this.tool = tool;
        this.whenObserved = whenObserved;
    }


    public String getObserver() {
        return observer;
    }

    public void setObserver(String observer) {
        this.observer = observer;
    }
    public String getTool() {
        return tool;
    }

    public void setTool(String tool) {
        this.tool = tool;
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