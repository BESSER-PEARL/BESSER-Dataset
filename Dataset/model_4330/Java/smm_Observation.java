





import java.util.List;
import java.util.ArrayList;

public class smm_Observation extends SmmElement {

    private String whenObserved;
    private String tool;
    private String observer;





    private List<smm_Argument> smm_arguments;




    private List<smm_SmmRelationship> smm_smmrelationships;




    private List<smm_ObservationScope> smm_observationscopes;


    public smm_Observation(
        String whenObserved,        String tool,        String observer    ) {
        super(
        );
        this.whenObserved = whenObserved;
        this.tool = tool;
        this.observer = observer;
        this.smm_arguments = new ArrayList<>();
        this.smm_smmrelationships = new ArrayList<>();
        this.smm_observationscopes = new ArrayList<>();
    }

    public smm_Observation(
        String whenObserved,        String tool,        String observer        ArrayList<smm_Argument> smm_arguments,        ArrayList<smm_SmmRelationship> smm_smmrelationships,        ArrayList<smm_ObservationScope> smm_observationscopes    ) {
        this.whenObserved = whenObserved;
        this.tool = tool;
        this.observer = observer;
        this.smm_arguments = smm_arguments;
        this.smm_smmrelationships = smm_smmrelationships;
        this.smm_observationscopes = smm_observationscopes;
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

    public List<smm_Argument> getSmm_arguments() {
        return smm_arguments;
    }

    public void addSmm_argument(Smm_argument smm_argument) {
        this.smm_arguments.add(smm_argument);
    }
    public List<smm_SmmRelationship> getSmm_smmrelationships() {
        return smm_smmrelationships;
    }

    public void addSmm_smmrelationship(Smm_smmrelationship smm_smmrelationship) {
        this.smm_smmrelationships.add(smm_smmrelationship);
    }
    public List<smm_ObservationScope> getSmm_observationscopes() {
        return smm_observationscopes;
    }

    public void addSmm_observationscope(Smm_observationscope smm_observationscope) {
        this.smm_observationscopes.add(smm_observationscope);
    }

}