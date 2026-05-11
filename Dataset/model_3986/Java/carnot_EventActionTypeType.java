





import java.util.List;
import java.util.ArrayList;

public class carnot_EventActionTypeType extends IMetaType {

    private String unsupportedContexts;
    private String supportedConditionTypes;
    private String panelClass;
    private String actionClass;
    private String activityAction;
    private String processAction;





    private carnot_AbstractEventAction carnot_abstracteventaction;




    private carnot_ModelType carnot_modeltype;




    private List<carnot_AbstractEventAction> carnot_abstracteventactions;


    public carnot_EventActionTypeType(
        String unsupportedContexts,        String supportedConditionTypes,        String panelClass,        String actionClass,        String activityAction,        String processAction    ) {
        super(
        );
        this.unsupportedContexts = unsupportedContexts;
        this.supportedConditionTypes = supportedConditionTypes;
        this.panelClass = panelClass;
        this.actionClass = actionClass;
        this.activityAction = activityAction;
        this.processAction = processAction;
        this.carnot_abstracteventactions = new ArrayList<>();
    }

    public carnot_EventActionTypeType(
        String unsupportedContexts,        String supportedConditionTypes,        String panelClass,        String actionClass,        String activityAction,        String processAction        ArrayList<carnot_AbstractEventAction> carnot_abstracteventactions    ) {
        this.unsupportedContexts = unsupportedContexts;
        this.supportedConditionTypes = supportedConditionTypes;
        this.panelClass = panelClass;
        this.actionClass = actionClass;
        this.activityAction = activityAction;
        this.processAction = processAction;
        this.carnot_abstracteventactions = carnot_abstracteventactions;
    }

    public String getUnsupportedcontexts() {
        return unsupportedContexts;
    }

    public void setUnsupportedcontexts(String unsupportedContexts) {
        this.unsupportedContexts = unsupportedContexts;
    }
    public String getSupportedconditiontypes() {
        return supportedConditionTypes;
    }

    public void setSupportedconditiontypes(String supportedConditionTypes) {
        this.supportedConditionTypes = supportedConditionTypes;
    }
    public String getPanelclass() {
        return panelClass;
    }

    public void setPanelclass(String panelClass) {
        this.panelClass = panelClass;
    }
    public String getActionclass() {
        return actionClass;
    }

    public void setActionclass(String actionClass) {
        this.actionClass = actionClass;
    }
    public String getActivityaction() {
        return activityAction;
    }

    public void setActivityaction(String activityAction) {
        this.activityAction = activityAction;
    }
    public String getProcessaction() {
        return processAction;
    }

    public void setProcessaction(String processAction) {
        this.processAction = processAction;
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
    public List<carnot_AbstractEventAction> getCarnot_abstracteventactions() {
        return carnot_abstracteventactions;
    }

    public void addCarnot_abstracteventaction(Carnot_abstracteventaction carnot_abstracteventaction) {
        this.carnot_abstracteventactions.add(carnot_abstracteventaction);
    }

}