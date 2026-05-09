





import java.util.List;
import java.util.ArrayList;

public class uma_Section extends MethodElement {

    private String variabilityBasedOnElement;
    private String variabilityType;
    private String sectionName;
    private String predecessor;
    private String description;





    private uma_Section uma_section;


    public uma_Section(
        String variabilityBasedOnElement,        String variabilityType,        String sectionName,        String predecessor,        String description    ) {
        super(
        );
        this.variabilityBasedOnElement = variabilityBasedOnElement;
        this.variabilityType = variabilityType;
        this.sectionName = sectionName;
        this.predecessor = predecessor;
        this.description = description;
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
    public String getSectionname() {
        return sectionName;
    }

    public void setSectionname(String sectionName) {
        this.sectionName = sectionName;
    }
    public String getPredecessor() {
        return predecessor;
    }

    public void setPredecessor(String predecessor) {
        this.predecessor = predecessor;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public uma_Section getUma_section() {
        return uma_section;
    }

    public void setUma_section(uma_Section uma_section) {
        this.uma_section = uma_section;
    }

}