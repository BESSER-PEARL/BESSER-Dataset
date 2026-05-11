





import java.util.List;
import java.util.ArrayList;

public class diagram_description_ContainerMapping extends description_DragAndDropTargetDescription, description_AbstractNodeMapping {

    private String childrenPresentation;





    private List<ContainerMapping> containermappings;




    private List<NodeMapping> nodemappings;




    private List<NodeMapping> nodemappings;




    private List<ContainerMapping> containermappings;




    private List<ContainerMapping> containermappings;




    private List<NodeMapping> nodemappings;


    public diagram_description_ContainerMapping(
        String childrenPresentation    ) {
        super(
        );
        this.childrenPresentation = childrenPresentation;
        this.containermappings = new ArrayList<>();
        this.nodemappings = new ArrayList<>();
        this.nodemappings = new ArrayList<>();
        this.containermappings = new ArrayList<>();
        this.containermappings = new ArrayList<>();
        this.nodemappings = new ArrayList<>();
    }

    public diagram_description_ContainerMapping(
        String childrenPresentation        ArrayList<ContainerMapping> containermappings,        ArrayList<NodeMapping> nodemappings,        ArrayList<NodeMapping> nodemappings,        ArrayList<ContainerMapping> containermappings,        ArrayList<ContainerMapping> containermappings,        ArrayList<NodeMapping> nodemappings    ) {
        this.childrenPresentation = childrenPresentation;
        this.containermappings = containermappings;
        this.nodemappings = nodemappings;
        this.nodemappings = nodemappings;
        this.containermappings = containermappings;
        this.containermappings = containermappings;
        this.nodemappings = nodemappings;
    }

    public String getChildrenpresentation() {
        return childrenPresentation;
    }

    public void setChildrenpresentation(String childrenPresentation) {
        this.childrenPresentation = childrenPresentation;
    }

    public List<ContainerMapping> getContainermappings() {
        return containermappings;
    }

    public void addContainermapping(Containermapping containermapping) {
        this.containermappings.add(containermapping);
    }
    public List<NodeMapping> getNodemappings() {
        return nodemappings;
    }

    public void addNodemapping(Nodemapping nodemapping) {
        this.nodemappings.add(nodemapping);
    }
    public List<NodeMapping> getNodemappings() {
        return nodemappings;
    }

    public void addNodemapping(Nodemapping nodemapping) {
        this.nodemappings.add(nodemapping);
    }
    public List<ContainerMapping> getContainermappings() {
        return containermappings;
    }

    public void addContainermapping(Containermapping containermapping) {
        this.containermappings.add(containermapping);
    }
    public List<ContainerMapping> getContainermappings() {
        return containermappings;
    }

    public void addContainermapping(Containermapping containermapping) {
        this.containermappings.add(containermapping);
    }
    public List<NodeMapping> getNodemappings() {
        return nodemappings;
    }

    public void addNodemapping(Nodemapping nodemapping) {
        this.nodemappings.add(nodemapping);
    }

}