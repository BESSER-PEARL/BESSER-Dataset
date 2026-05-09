





import java.util.List;
import java.util.ArrayList;

public class uma_Activity extends WorkBreakdownElement {

    private String group3;
    private String variabilityType;
    private String isEnactable;
    private String variabilityBasedOnElement;
    private String roadmap;
    private String postcondition;
    private String precondition;





    private List<uma_BreakdownElement> uma_breakdownelements;


    public uma_Activity(
        String group3,        String variabilityType,        String isEnactable,        String variabilityBasedOnElement,        String roadmap,        String postcondition,        String precondition    ) {
        super(
        );
        this.group3 = group3;
        this.variabilityType = variabilityType;
        this.isEnactable = isEnactable;
        this.variabilityBasedOnElement = variabilityBasedOnElement;
        this.roadmap = roadmap;
        this.postcondition = postcondition;
        this.precondition = precondition;
        this.uma_breakdownelements = new ArrayList<>();
    }

    public uma_Activity(
        String group3,        String variabilityType,        String isEnactable,        String variabilityBasedOnElement,        String roadmap,        String postcondition,        String precondition        ArrayList<uma_BreakdownElement> uma_breakdownelements    ) {
        this.group3 = group3;
        this.variabilityType = variabilityType;
        this.isEnactable = isEnactable;
        this.variabilityBasedOnElement = variabilityBasedOnElement;
        this.roadmap = roadmap;
        this.postcondition = postcondition;
        this.precondition = precondition;
        this.uma_breakdownelements = uma_breakdownelements;
    }

    public String getGroup3() {
        return group3;
    }

    public void setGroup3(String group3) {
        this.group3 = group3;
    }
    public String getVariabilitytype() {
        return variabilityType;
    }

    public void setVariabilitytype(String variabilityType) {
        this.variabilityType = variabilityType;
    }
    public String getIsenactable() {
        return isEnactable;
    }

    public void setIsenactable(String isEnactable) {
        this.isEnactable = isEnactable;
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
    public String getPrecondition() {
        return precondition;
    }

    public void setPrecondition(String precondition) {
        this.precondition = precondition;
    }

    public List<uma_BreakdownElement> getUma_breakdownelements() {
        return uma_breakdownelements;
    }

    public void addUma_breakdownelement(Uma_breakdownelement uma_breakdownelement) {
        this.uma_breakdownelements.add(uma_breakdownelement);
    }

}