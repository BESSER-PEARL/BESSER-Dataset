





import java.util.List;
import java.util.ArrayList;

public class carnot_ProcessDefinitionType extends IdRefOwner, IIdentifiableModelElement, IEventHandlerOwner {

    private String defaultPriority;





    private carnot_ActivityType carnot_activitytype;




    private List<carnot_DiagramType> carnot_diagramtypes;




    private List<carnot_ActivityType> carnot_activitytypes;




    private List<carnot_DataPathType> carnot_datapathtypes;




    private carnot_ModelType carnot_modeltype;




    private List<carnot_ActivityType> carnot_activitytypes;




    private List<carnot_TransitionType> carnot_transitiontypes;


    public carnot_ProcessDefinitionType(
        String defaultPriority    ) {
        super(
        );
        this.defaultPriority = defaultPriority;
        this.carnot_diagramtypes = new ArrayList<>();
        this.carnot_activitytypes = new ArrayList<>();
        this.carnot_datapathtypes = new ArrayList<>();
        this.carnot_activitytypes = new ArrayList<>();
        this.carnot_transitiontypes = new ArrayList<>();
    }

    public carnot_ProcessDefinitionType(
        String defaultPriority        ArrayList<carnot_DiagramType> carnot_diagramtypes,        ArrayList<carnot_ActivityType> carnot_activitytypes,        ArrayList<carnot_DataPathType> carnot_datapathtypes,        ArrayList<carnot_ActivityType> carnot_activitytypes,        ArrayList<carnot_TransitionType> carnot_transitiontypes    ) {
        this.defaultPriority = defaultPriority;
        this.carnot_diagramtypes = carnot_diagramtypes;
        this.carnot_activitytypes = carnot_activitytypes;
        this.carnot_datapathtypes = carnot_datapathtypes;
        this.carnot_activitytypes = carnot_activitytypes;
        this.carnot_transitiontypes = carnot_transitiontypes;
    }

    public String getDefaultpriority() {
        return defaultPriority;
    }

    public void setDefaultpriority(String defaultPriority) {
        this.defaultPriority = defaultPriority;
    }

    public carnot_ActivityType getCarnot_activitytype() {
        return carnot_activitytype;
    }

    public void setCarnot_activitytype(carnot_ActivityType carnot_activitytype) {
        this.carnot_activitytype = carnot_activitytype;
    }
    public List<carnot_DiagramType> getCarnot_diagramtypes() {
        return carnot_diagramtypes;
    }

    public void addCarnot_diagramtype(Carnot_diagramtype carnot_diagramtype) {
        this.carnot_diagramtypes.add(carnot_diagramtype);
    }
    public List<carnot_ActivityType> getCarnot_activitytypes() {
        return carnot_activitytypes;
    }

    public void addCarnot_activitytype(Carnot_activitytype carnot_activitytype) {
        this.carnot_activitytypes.add(carnot_activitytype);
    }
    public List<carnot_DataPathType> getCarnot_datapathtypes() {
        return carnot_datapathtypes;
    }

    public void addCarnot_datapathtype(Carnot_datapathtype carnot_datapathtype) {
        this.carnot_datapathtypes.add(carnot_datapathtype);
    }
    public carnot_ModelType getCarnot_modeltype() {
        return carnot_modeltype;
    }

    public void setCarnot_modeltype(carnot_ModelType carnot_modeltype) {
        this.carnot_modeltype = carnot_modeltype;
    }
    public List<carnot_ActivityType> getCarnot_activitytypes() {
        return carnot_activitytypes;
    }

    public void addCarnot_activitytype(Carnot_activitytype carnot_activitytype) {
        this.carnot_activitytypes.add(carnot_activitytype);
    }
    public List<carnot_TransitionType> getCarnot_transitiontypes() {
        return carnot_transitiontypes;
    }

    public void addCarnot_transitiontype(Carnot_transitiontype carnot_transitiontype) {
        this.carnot_transitiontypes.add(carnot_transitiontype);
    }

}