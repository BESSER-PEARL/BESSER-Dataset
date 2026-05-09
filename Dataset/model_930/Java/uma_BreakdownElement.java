





import java.util.List;
import java.util.ArrayList;

public class uma_BreakdownElement extends ProcessElement {

    private String hasMultipleOccurrences;
    private String isOptional;
    private String isPlanned;
    private String prefix;





    private uma_PlanningData uma_planningdata;




    private uma_BreakdownElement uma_breakdownelement;




    private uma_BreakdownElement uma_breakdownelement;


    public uma_BreakdownElement(
        String hasMultipleOccurrences,        String isOptional,        String isPlanned,        String prefix    ) {
        super(
        );
        this.hasMultipleOccurrences = hasMultipleOccurrences;
        this.isOptional = isOptional;
        this.isPlanned = isPlanned;
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
    public String getPrefix() {
        return prefix;
    }

    public void setPrefix(String prefix) {
        this.prefix = prefix;
    }

    public uma_PlanningData getUma_planningdata() {
        return uma_planningdata;
    }

    public void setUma_planningdata(uma_PlanningData uma_planningdata) {
        this.uma_planningdata = uma_planningdata;
    }
    public uma_BreakdownElement getUma_breakdownelement() {
        return uma_breakdownelement;
    }

    public void setUma_breakdownelement(uma_BreakdownElement uma_breakdownelement) {
        this.uma_breakdownelement = uma_breakdownelement;
    }
    public uma_BreakdownElement getUma_breakdownelement() {
        return uma_breakdownelement;
    }

    public void setUma_breakdownelement(uma_BreakdownElement uma_breakdownelement) {
        this.uma_breakdownelement = uma_breakdownelement;
    }

}