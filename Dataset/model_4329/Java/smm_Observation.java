





import java.util.List;
import java.util.ArrayList;

public class smm_Observation extends SmmElement {

    private String observer;
    private String tool;
    private String whenObserved;





    private List<smm_AbstractMeasureElement> smm_abstractmeasureelements;


    public smm_Observation(
        String observer,        String tool,        String whenObserved    ) {
        super(
        );
        this.observer = observer;
        this.tool = tool;
        this.whenObserved = whenObserved;
        this.smm_abstractmeasureelements = new ArrayList<>();
    }

    public smm_Observation(
        String observer,        String tool,        String whenObserved        ArrayList<smm_AbstractMeasureElement> smm_abstractmeasureelements    ) {
        this.observer = observer;
        this.tool = tool;
        this.whenObserved = whenObserved;
        this.smm_abstractmeasureelements = smm_abstractmeasureelements;
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

    public List<smm_AbstractMeasureElement> getSmm_abstractmeasureelements() {
        return smm_abstractmeasureelements;
    }

    public void addSmm_abstractmeasureelement(Smm_abstractmeasureelement smm_abstractmeasureelement) {
        this.smm_abstractmeasureelements.add(smm_abstractmeasureelement);
    }

}