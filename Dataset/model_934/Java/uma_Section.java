





import java.util.List;
import java.util.ArrayList;

public class uma_Section extends MethodElement {

    private String variabilityType;
    private String variabilityBasedOnElement;
    private String description;
    private String predecessor;
    private String sectionName;





    private uma_Section uma_section;




    private uma_TaskDescriptor uma_taskdescriptor;


    public uma_Section(
        String variabilityType,        String variabilityBasedOnElement,        String description,        String predecessor,        String sectionName    ) {
        super(
        );
        this.variabilityType = variabilityType;
        this.variabilityBasedOnElement = variabilityBasedOnElement;
        this.description = description;
        this.predecessor = predecessor;
        this.sectionName = sectionName;
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
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getPredecessor() {
        return predecessor;
    }

    public void setPredecessor(String predecessor) {
        this.predecessor = predecessor;
    }
    public String getSectionname() {
        return sectionName;
    }

    public void setSectionname(String sectionName) {
        this.sectionName = sectionName;
    }

    public uma_Section getUma_section() {
        return uma_section;
    }

    public void setUma_section(uma_Section uma_section) {
        this.uma_section = uma_section;
    }
    public uma_TaskDescriptor getUma_taskdescriptor() {
        return uma_taskdescriptor;
    }

    public void setUma_taskdescriptor(uma_TaskDescriptor uma_taskdescriptor) {
        this.uma_taskdescriptor = uma_taskdescriptor;
    }

}