





import java.util.List;
import java.util.ArrayList;

public class carnot_TriggerTypeType extends IMetaType {

    private String pullTriggerEvaluator;
    private String rule;
    private String panelClass;
    private String pullTrigger;





    private List<carnot_TriggerType> carnot_triggertypes;




    private carnot_TriggerType carnot_triggertype;




    private carnot_ModelType carnot_modeltype;


    public carnot_TriggerTypeType(
        String pullTriggerEvaluator,        String rule,        String panelClass,        String pullTrigger    ) {
        super(
        );
        this.pullTriggerEvaluator = pullTriggerEvaluator;
        this.rule = rule;
        this.panelClass = panelClass;
        this.pullTrigger = pullTrigger;
        this.carnot_triggertypes = new ArrayList<>();
    }

    public carnot_TriggerTypeType(
        String pullTriggerEvaluator,        String rule,        String panelClass,        String pullTrigger        ArrayList<carnot_TriggerType> carnot_triggertypes    ) {
        this.pullTriggerEvaluator = pullTriggerEvaluator;
        this.rule = rule;
        this.panelClass = panelClass;
        this.pullTrigger = pullTrigger;
        this.carnot_triggertypes = carnot_triggertypes;
    }

    public String getPulltriggerevaluator() {
        return pullTriggerEvaluator;
    }

    public void setPulltriggerevaluator(String pullTriggerEvaluator) {
        this.pullTriggerEvaluator = pullTriggerEvaluator;
    }
    public String getRule() {
        return rule;
    }

    public void setRule(String rule) {
        this.rule = rule;
    }
    public String getPanelclass() {
        return panelClass;
    }

    public void setPanelclass(String panelClass) {
        this.panelClass = panelClass;
    }
    public String getPulltrigger() {
        return pullTrigger;
    }

    public void setPulltrigger(String pullTrigger) {
        this.pullTrigger = pullTrigger;
    }

    public List<carnot_TriggerType> getCarnot_triggertypes() {
        return carnot_triggertypes;
    }

    public void addCarnot_triggertype(Carnot_triggertype carnot_triggertype) {
        this.carnot_triggertypes.add(carnot_triggertype);
    }
    public carnot_TriggerType getCarnot_triggertype() {
        return carnot_triggertype;
    }

    public void setCarnot_triggertype(carnot_TriggerType carnot_triggertype) {
        this.carnot_triggertype = carnot_triggertype;
    }
    public carnot_ModelType getCarnot_modeltype() {
        return carnot_modeltype;
    }

    public void setCarnot_modeltype(carnot_ModelType carnot_modeltype) {
        this.carnot_modeltype = carnot_modeltype;
    }

}