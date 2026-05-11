





import java.util.List;
import java.util.ArrayList;

public class carnot_EventConditionTypeType extends IMetaType {

    private String panelClass;
    private String pullEventEmitterClass;
    private String rule;
    private String implementation;
    private String binderClass;
    private String processCondition;
    private String activityCondition;





    private carnot_EventHandlerType carnot_eventhandlertype;




    private carnot_ModelType carnot_modeltype;




    private List<carnot_EventHandlerType> carnot_eventhandlertypes;


    public carnot_EventConditionTypeType(
        String panelClass,        String pullEventEmitterClass,        String rule,        String implementation,        String binderClass,        String processCondition,        String activityCondition    ) {
        super(
        );
        this.panelClass = panelClass;
        this.pullEventEmitterClass = pullEventEmitterClass;
        this.rule = rule;
        this.implementation = implementation;
        this.binderClass = binderClass;
        this.processCondition = processCondition;
        this.activityCondition = activityCondition;
        this.carnot_eventhandlertypes = new ArrayList<>();
    }

    public carnot_EventConditionTypeType(
        String panelClass,        String pullEventEmitterClass,        String rule,        String implementation,        String binderClass,        String processCondition,        String activityCondition        ArrayList<carnot_EventHandlerType> carnot_eventhandlertypes    ) {
        this.panelClass = panelClass;
        this.pullEventEmitterClass = pullEventEmitterClass;
        this.rule = rule;
        this.implementation = implementation;
        this.binderClass = binderClass;
        this.processCondition = processCondition;
        this.activityCondition = activityCondition;
        this.carnot_eventhandlertypes = carnot_eventhandlertypes;
    }

    public String getPanelclass() {
        return panelClass;
    }

    public void setPanelclass(String panelClass) {
        this.panelClass = panelClass;
    }
    public String getPulleventemitterclass() {
        return pullEventEmitterClass;
    }

    public void setPulleventemitterclass(String pullEventEmitterClass) {
        this.pullEventEmitterClass = pullEventEmitterClass;
    }
    public String getRule() {
        return rule;
    }

    public void setRule(String rule) {
        this.rule = rule;
    }
    public String getImplementation() {
        return implementation;
    }

    public void setImplementation(String implementation) {
        this.implementation = implementation;
    }
    public String getBinderclass() {
        return binderClass;
    }

    public void setBinderclass(String binderClass) {
        this.binderClass = binderClass;
    }
    public String getProcesscondition() {
        return processCondition;
    }

    public void setProcesscondition(String processCondition) {
        this.processCondition = processCondition;
    }
    public String getActivitycondition() {
        return activityCondition;
    }

    public void setActivitycondition(String activityCondition) {
        this.activityCondition = activityCondition;
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