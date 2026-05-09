





import java.util.List;
import java.util.ArrayList;

public class uma_Activity extends WorkBreakdownElement {

    private String precondition;
    private String group3;
    private String roadmap;
    private String postcondition;
    private String isEnactable;
    private String variabilityBasedOnElement;
    private String variabilityType;



    public uma_Activity(
        String precondition,        String group3,        String roadmap,        String postcondition,        String isEnactable,        String variabilityBasedOnElement,        String variabilityType    ) {
        super(
        );
        this.precondition = precondition;
        this.group3 = group3;
        this.roadmap = roadmap;
        this.postcondition = postcondition;
        this.isEnactable = isEnactable;
        this.variabilityBasedOnElement = variabilityBasedOnElement;
        this.variabilityType = variabilityType;
    }


    public String getPrecondition() {
        return precondition;
    }

    public void setPrecondition(String precondition) {
        this.precondition = precondition;
    }
    public String getGroup3() {
        return group3;
    }

    public void setGroup3(String group3) {
        this.group3 = group3;
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
    public String getVariabilitytype() {
        return variabilityType;
    }

    public void setVariabilitytype(String variabilityType) {
        this.variabilityType = variabilityType;
    }


}