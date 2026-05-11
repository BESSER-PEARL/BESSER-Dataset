





import java.util.List;
import java.util.ArrayList;

public class smm_Observation extends SmmElement {

    private String whenObserved;
    private String tool;
    private String observer;



    public smm_Observation(
        String whenObserved,        String tool,        String observer    ) {
        super(
        );
        this.whenObserved = whenObserved;
        this.tool = tool;
        this.observer = observer;
    }


    public String getWhenobserved() {
        return whenObserved;
    }

    public void setWhenobserved(String whenObserved) {
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


}