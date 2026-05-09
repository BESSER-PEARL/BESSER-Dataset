





import java.util.List;
import java.util.ArrayList;

public class uma_Activity extends WorkBreakdownElement {

    private String group3;
    private String precondition;
    private String isEnactable;
    private String variabilityType;
    private String variabilityBasedOnElement;
    private String postcondition;
    private String roadmap;





    private List<uma_BreakdownElement> uma_breakdownelements;


    public uma_Activity(
        String group3,        String precondition,        String isEnactable,        String variabilityType,        String variabilityBasedOnElement,        String postcondition,        String roadmap    ) {
        super(
        );
        this.group3 = group3;
        this.precondition = precondition;
        this.isEnactable = isEnactable;
        this.variabilityType = variabilityType;
        this.variabilityBasedOnElement = variabilityBasedOnElement;
        this.postcondition = postcondition;
        this.roadmap = roadmap;
        this.uma_breakdownelements = new ArrayList<>();
    }

    public uma_Activity(
        String group3,        String precondition,        String isEnactable,        String variabilityType,        String variabilityBasedOnElement,        String postcondition,        String roadmap        ArrayList<uma_BreakdownElement> uma_breakdownelements    ) {
        this.group3 = group3;
        this.precondition = precondition;
        this.isEnactable = isEnactable;
        this.variabilityType = variabilityType;
        this.variabilityBasedOnElement = variabilityBasedOnElement;
        this.postcondition = postcondition;
        this.roadmap = roadmap;
        this.uma_breakdownelements = uma_breakdownelements;
    }

    public String getGroup3() {
        return group3;
    }

    public void setGroup3(String group3) {
        this.group3 = group3;
    }
    public String getPrecondition() {
        return precondition;
    }

    public void setPrecondition(String precondition) {
        this.precondition = precondition;
    }
    public String getIsenactable() {
        return isEnactable;
    }

    public void setIsenactable(String isEnactable) {
        this.isEnactable = isEnactable;
    }
    public String getVariabilitytype() {
        return variabilityType;
    }

    public void setVariabilitytype(String variabilityType) {
        this.variabilityType = variabilityType;
    }
    public String getVariabilitybasedonelement() {
        return variabilityBasedOnElement;
    }

    public void setVariabilitybasedonelement(String variabilityBasedOnElement) {
        this.variabilityBasedOnElement = variabilityBasedOnElement;
    }
    public String getPostcondition() {
        return postcondition;
    }

    public void setPostcondition(String postcondition) {
        this.postcondition = postcondition;
    }
    public String getRoadmap() {
        return roadmap;
    }

    public void setRoadmap(String roadmap) {
        this.roadmap = roadmap;
    }

    public List<uma_BreakdownElement> getUma_breakdownelements() {
        return uma_breakdownelements;
    }

    public void addUma_breakdownelement(Uma_breakdownelement uma_breakdownelement) {
        this.uma_breakdownelements.add(uma_breakdownelement);
    }

}