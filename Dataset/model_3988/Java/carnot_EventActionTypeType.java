





import java.util.List;
import java.util.ArrayList;

public class carnot_EventActionTypeType extends IMetaType {

    private String processAction;
    private String activityAction;
    private String panelClass;
    private String supportedConditionTypes;
    private String unsupportedContexts;
    private String actionClass;





    private List<carnot_AbstractEventAction> carnot_abstracteventactions;




    private carnot_AbstractEventAction carnot_abstracteventaction;




    private carnot_ModelType carnot_modeltype;


    public carnot_EventActionTypeType(
        String processAction,        String activityAction,        String panelClass,        String supportedConditionTypes,        String unsupportedContexts,        String actionClass    ) {
        super(
        );
        this.processAction = processAction;
        this.activityAction = activityAction;
        this.panelClass = panelClass;
        this.supportedConditionTypes = supportedConditionTypes;
        this.unsupportedContexts = unsupportedContexts;
        this.actionClass = actionClass;
        this.carnot_abstracteventactions = new ArrayList<>();
    }

    public carnot_EventActionTypeType(
        String processAction,        String activityAction,        String panelClass,        String supportedConditionTypes,        String unsupportedContexts,        String actionClass        ArrayList<carnot_AbstractEventAction> carnot_abstracteventactions    ) {
        this.processAction = processAction;
        this.activityAction = activityAction;
        this.panelClass = panelClass;
        this.supportedConditionTypes = supportedConditionTypes;
        this.unsupportedContexts = unsupportedContexts;
        this.actionClass = actionClass;
        this.carnot_abstracteventactions = carnot_abstracteventactions;
    }

    public String getProcessaction() {
        return processAction;
    }

    public void setProcessaction(String processAction) {
        this.processAction = processAction;
    }
    public String getActivityaction() {
        return activityAction;
    }

    public void setActivityaction(String activityAction) {
        this.activityAction = activityAction;
    }
    public String getPanelclass() {
        return panelClass;
    }

    public void setPanelclass(String panelClass) {
        this.panelClass = panelClass;
    }
    public String getSupportedconditiontypes() {
        return supportedConditionTypes;
    }

    public void setSupportedconditiontypes(String supportedConditionTypes) {
        this.supportedConditionTypes = supportedConditionTypes;
    }
    public String getUnsupportedcontexts() {
        return unsupportedContexts;
    }

    public void setUnsupportedcontexts(String unsupportedContexts) {
        this.unsupportedContexts = unsupportedContexts;
    }
    public String getActionclass() {
        return actionClass;
    }

    public void setActionclass(String actionClass) {
        this.actionClass = actionClass;
    }

    public List<carnot_AbstractEventAction> getCarnot_abstracteventactions() {
        return carnot_abstracteventactions;
    }

    public void addCarnot_abstracteventaction(Carnot_abstracteventaction carnot_abstracteventaction) {
        this.carnot_abstracteventactions.add(carnot_abstracteventaction);
    }
    public carnot_AbstractEventAction getCarnot_abstracteventaction() {
        return carnot_abstracteventaction;
    }

    public void setCarnot_abstracteventaction(carnot_AbstractEventAction carnot_abstracteventaction) {
        this.carnot_abstracteventaction = carnot_abstracteventaction;
    }
    public carnot_ModelType getCarnot_modeltype() {
        return carnot_modeltype;
    }

    public void setCarnot_modeltype(carnot_ModelType carnot_modeltype) {
        this.carnot_modeltype = carnot_modeltype;
    }

}