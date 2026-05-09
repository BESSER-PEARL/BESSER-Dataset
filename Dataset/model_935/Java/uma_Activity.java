





import java.util.List;
import java.util.ArrayList;

public class uma_Activity extends WorkBreakdownElement {

    private String precondition;
    private String isEnactable;
    private String variabilityType;
    private String variabilityBasedOnElement;
    private String roadmap;
    private String postcondition;
    private String group3;





    private List<uma_BreakdownElement> uma_breakdownelements;


    public uma_Activity(
        String precondition,        String isEnactable,        String variabilityType,        String variabilityBasedOnElement,        String roadmap,        String postcondition,        String group3    ) {
        super(
        );
        this.precondition = precondition;
        this.isEnactable = isEnactable;
        this.variabilityType = variabilityType;
        this.variabilityBasedOnElement = variabilityBasedOnElement;
        this.roadmap = roadmap;
        this.postcondition = postcondition;
        this.group3 = group3;
        this.uma_breakdownelements = new ArrayList<>();
    }

    public uma_Activity(
        String precondition,        String isEnactable,        String variabilityType,        String variabilityBasedOnElement,        String roadmap,        String postcondition,        String group3        ArrayList<uma_BreakdownElement> uma_breakdownelements    ) {
        this.precondition = precondition;
        this.isEnactable = isEnactable;
        this.variabilityType = variabilityType;
        this.variabilityBasedOnElement = variabilityBasedOnElement;
        this.roadmap = roadmap;
        this.postcondition = postcondition;
        this.group3 = group3;
        this.uma_breakdownelements = uma_breakdownelements;
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
    public String getRoadmap() {
        return roadmap;
    }

    public void setRoadmap(String roadmap) {
        this.roadmap = roadmap;
    }
    public String getPostcondition() {
        return postcondition;
    }

    public void setPostcondition(String postcondition) {
        this.postcondition = postcondition;
    }
    public String getGroup3() {
        return group3;
    }

    public void setGroup3(String group3) {
        this.group3 = group3;
    }

    public List<uma_BreakdownElement> getUma_breakdownelements() {
        return uma_breakdownelements;
    }

    public void addUma_breakdownelement(Uma_breakdownelement uma_breakdownelement) {
        this.uma_breakdownelements.add(uma_breakdownelement);
    }

}