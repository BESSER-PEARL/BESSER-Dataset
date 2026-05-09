





import java.util.List;
import java.util.ArrayList;

public class uma_BreakdownElement extends ProcessElement {

    private String prefix;
    private String hasMultipleOccurrences;
    private String isOptional;
    private String isPlanned;





    private uma_BreakdownElement uma_breakdownelement;




    private uma_Activity uma_activity;




    private uma_BreakdownElement uma_breakdownelement;




    private uma_PlanningData uma_planningdata;




    private List<uma_Activity> uma_activitys;


    public uma_BreakdownElement(
        String prefix,        String hasMultipleOccurrences,        String isOptional,        String isPlanned    ) {
        super(
        );
        this.prefix = prefix;
        this.hasMultipleOccurrences = hasMultipleOccurrences;
        this.isOptional = isOptional;
        this.isPlanned = isPlanned;
        this.uma_activitys = new ArrayList<>();
    }

    public uma_BreakdownElement(
        String prefix,        String hasMultipleOccurrences,        String isOptional,        String isPlanned        ArrayList<uma_Activity> uma_activitys    ) {
        this.prefix = prefix;
        this.hasMultipleOccurrences = hasMultipleOccurrences;
        this.isOptional = isOptional;
        this.isPlanned = isPlanned;
        this.uma_activitys = uma_activitys;
    }

    public String getPrefix() {
        return prefix;
    }

    public void setPrefix(String prefix) {
        this.prefix = prefix;
    }
    public String getHasmultipleoccurrences() {
        return hasMultipleOccurrences;
    }

    public void setHasmultipleoccurrences(String hasMultipleOccurrences) {
        this.hasMultipleOccurrences = hasMultipleOccurrences;
    }
    public String getIsoptional() {
        return isOptional;
    }

    public void setIsoptional(String isOptional) {
        this.isOptional = isOptional;
    }
    public String getIsplanned() {
        return isPlanned;
    }

    public void setIsplanned(String isPlanned) {
        this.isPlanned = isPlanned;
    }

    public uma_BreakdownElement getUma_breakdownelement() {
        return uma_breakdownelement;
    }

    public void setUma_breakdownelement(uma_BreakdownElement uma_breakdownelement) {
        this.uma_breakdownelement = uma_breakdownelement;
    }
    public uma_Activity getUma_activity() {
        return uma_activity;
    }

    public void setUma_activity(uma_Activity uma_activity) {
        this.uma_activity = uma_activity;
    }
    public uma_BreakdownElement getUma_breakdownelement() {
        return uma_breakdownelement;
    }

    public void setUma_breakdownelement(uma_BreakdownElement uma_breakdownelement) {
        this.uma_breakdownelement = uma_breakdownelement;
    }
    public uma_PlanningData getUma_planningdata() {
        return uma_planningdata;
    }

    public void setUma_planningdata(uma_PlanningData uma_planningdata) {
        this.uma_planningdata = uma_planningdata;
    }
    public List<uma_Activity> getUma_activitys() {
        return uma_activitys;
    }

    public void addUma_activity(Uma_activity uma_activity) {
        this.uma_activitys.add(uma_activity);
    }

}