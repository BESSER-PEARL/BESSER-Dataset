





import java.util.List;
import java.util.ArrayList;

public class carnot_ProcessDefinitionType extends IEventHandlerOwner, IIdentifiableModelElement {

    private String defaultPriority;





    private carnot_ModelType carnot_modeltype;




    private List<carnot_TransitionType> carnot_transitiontypes;




    private List<carnot_DiagramType> carnot_diagramtypes;




    private List<carnot_TriggerType> carnot_triggertypes;


    public carnot_ProcessDefinitionType(
        String defaultPriority    ) {
        super(
        );
        this.defaultPriority = defaultPriority;
        this.carnot_transitiontypes = new ArrayList<>();
        this.carnot_diagramtypes = new ArrayList<>();
        this.carnot_triggertypes = new ArrayList<>();
    }

    public carnot_ProcessDefinitionType(
        String defaultPriority        ArrayList<carnot_TransitionType> carnot_transitiontypes,        ArrayList<carnot_DiagramType> carnot_diagramtypes,        ArrayList<carnot_TriggerType> carnot_triggertypes    ) {
        this.defaultPriority = defaultPriority;
        this.carnot_transitiontypes = carnot_transitiontypes;
        this.carnot_diagramtypes = carnot_diagramtypes;
        this.carnot_triggertypes = carnot_triggertypes;
    }

    public String getDefaultpriority() {
        return defaultPriority;
    }

    public void setDefaultpriority(String defaultPriority) {
        this.defaultPriority = defaultPriority;
    }

    public carnot_ModelType getCarnot_modeltype() {
        return carnot_modeltype;
    }

    public void setCarnot_modeltype(carnot_ModelType carnot_modeltype) {
        this.carnot_modeltype = carnot_modeltype;
    }
    public List<carnot_TransitionType> getCarnot_transitiontypes() {
        return carnot_transitiontypes;
    }

    public void addCarnot_transitiontype(Carnot_transitiontype carnot_transitiontype) {
        this.carnot_transitiontypes.add(carnot_transitiontype);
    }
    public List<carnot_DiagramType> getCarnot_diagramtypes() {
        return carnot_diagramtypes;
    }

    public void addCarnot_diagramtype(Carnot_diagramtype carnot_diagramtype) {
        this.carnot_diagramtypes.add(carnot_diagramtype);
    }
    public List<carnot_TriggerType> getCarnot_triggertypes() {
        return carnot_triggertypes;
    }

    public void addCarnot_triggertype(Carnot_triggertype carnot_triggertype) {
        this.carnot_triggertypes.add(carnot_triggertype);
    }

}