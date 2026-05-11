





import java.util.List;
import java.util.ArrayList;

public class smm_Observation extends SmmElement {

    private String tool;
    private String observer;
    private String whenObserved;





    private smm_SmmModel smm_smmmodel;




    private List<smm_AbstractMeasureElement> smm_abstractmeasureelements;




    private List<smm_ObservationScope> smm_observationscopes;


    public smm_Observation(
        String tool,        String observer,        String whenObserved    ) {
        super(
        );
        this.tool = tool;
        this.observer = observer;
        this.whenObserved = whenObserved;
        this.smm_abstractmeasureelements = new ArrayList<>();
        this.smm_observationscopes = new ArrayList<>();
    }

    public smm_Observation(
        String tool,        String observer,        String whenObserved        ArrayList<smm_AbstractMeasureElement> smm_abstractmeasureelements,        ArrayList<smm_ObservationScope> smm_observationscopes    ) {
        this.tool = tool;
        this.observer = observer;
        this.whenObserved = whenObserved;
        this.smm_abstractmeasureelements = smm_abstractmeasureelements;
        this.smm_observationscopes = smm_observationscopes;
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

    public smm_SmmModel getSmm_smmmodel() {
        return smm_smmmodel;
    }

    public void setSmm_smmmodel(smm_SmmModel smm_smmmodel) {
        this.smm_smmmodel = smm_smmmodel;
    }
    public List<smm_AbstractMeasureElement> getSmm_abstractmeasureelements() {
        return smm_abstractmeasureelements;
    }

    public void addSmm_abstractmeasureelement(Smm_abstractmeasureelement smm_abstractmeasureelement) {
        this.smm_abstractmeasureelements.add(smm_abstractmeasureelement);
    }
    public List<smm_ObservationScope> getSmm_observationscopes() {
        return smm_observationscopes;
    }

    public void addSmm_observationscope(Smm_observationscope smm_observationscope) {
        this.smm_observationscopes.add(smm_observationscope);
    }

}