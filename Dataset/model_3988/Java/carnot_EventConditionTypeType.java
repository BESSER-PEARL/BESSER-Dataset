





import java.util.List;
import java.util.ArrayList;

public class carnot_EventConditionTypeType extends IMetaType {

    private String pullEventEmitterClass;
    private String activityCondition;
    private String rule;
    private String binderClass;
    private String implementation;
    private String panelClass;
    private String processCondition;





    private carnot_EventHandlerType carnot_eventhandlertype;




    private carnot_ModelType carnot_modeltype;




    private List<carnot_EventHandlerType> carnot_eventhandlertypes;


    public carnot_EventConditionTypeType(
        String pullEventEmitterClass,        String activityCondition,        String rule,        String binderClass,        String implementation,        String panelClass,        String processCondition    ) {
        super(
        );
        this.pullEventEmitterClass = pullEventEmitterClass;
        this.activityCondition = activityCondition;
        this.rule = rule;
        this.binderClass = binderClass;
        this.implementation = implementation;
        this.panelClass = panelClass;
        this.processCondition = processCondition;
        this.carnot_eventhandlertypes = new ArrayList<>();
    }

    public carnot_EventConditionTypeType(
        String pullEventEmitterClass,        String activityCondition,        String rule,        String binderClass,        String implementation,        String panelClass,        String processCondition        ArrayList<carnot_EventHandlerType> carnot_eventhandlertypes    ) {
        this.pullEventEmitterClass = pullEventEmitterClass;
        this.activityCondition = activityCondition;
        this.rule = rule;
        this.binderClass = binderClass;
        this.implementation = implementation;
        this.panelClass = panelClass;
        this.processCondition = processCondition;
        this.carnot_eventhandlertypes = carnot_eventhandlertypes;
    }

    public String getPulleventemitterclass() {
        return pullEventEmitterClass;
    }

    public void setPulleventemitterclass(String pullEventEmitterClass) {
        this.pullEventEmitterClass = pullEventEmitterClass;
    }
    public String getActivitycondition() {
        return activityCondition;
    }

    public void setActivitycondition(String activityCondition) {
        this.activityCondition = activityCondition;
    }
    public String getRule() {
        return rule;
    }

    public void setRule(String rule) {
        this.rule = rule;
    }
    public String getBinderclass() {
        return binderClass;
    }

    public void setBinderclass(String binderClass) {
        this.binderClass = binderClass;
    }
    public String getImplementation() {
        return implementation;
    }

    public void setImplementation(String implementation) {
        this.implementation = implementation;
    }
    public String getPanelclass() {
        return panelClass;
    }

    public void setPanelclass(String panelClass) {
        this.panelClass = panelClass;
    }
    public String getProcesscondition() {
        return processCondition;
    }

    public void setProcesscondition(String processCondition) {
        this.processCondition = processCondition;
    }

    public carnot_EventHandlerType getCarnot_eventhandlertype() {
        return carnot_eventhandlertype;
    }

    public void setCarnot_eventhandlertype(carnot_EventHandlerType carnot_eventhandlertype) {
        this.carnot_eventhandlertype = carnot_eventhandlertype;
    }
    public carnot_ModelType getCarnot_modeltype() {
        return carnot_modeltype;
    }

    public void setCarnot_modeltype(carnot_ModelType carnot_modeltype) {
        this.carnot_modeltype = carnot_modeltype;
    }
    public List<carnot_EventHandlerType> getCarnot_eventhandlertypes() {
        return carnot_eventhandlertypes;
    }

    public void addCarnot_eventhandlertype(Carnot_eventhandlertype carnot_eventhandlertype) {
        this.carnot_eventhandlertypes.add(carnot_eventhandlertype);
    }

}