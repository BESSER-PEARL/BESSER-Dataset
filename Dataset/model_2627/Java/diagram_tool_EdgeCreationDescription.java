





import java.util.List;
import java.util.ArrayList;

public class diagram_tool_EdgeCreationDescription extends MappingBasedToolDescription {

    private String connectionStartPrecondition;
    private String iconPath;





    private List<DiagramElementMapping> diagramelementmappings;




    private List<EdgeMapping> edgemappings;




    private List<DiagramElementMapping> diagramelementmappings;


    public diagram_tool_EdgeCreationDescription(
        String connectionStartPrecondition,        String iconPath    ) {
        super(
        );
        this.connectionStartPrecondition = connectionStartPrecondition;
        this.iconPath = iconPath;
        this.diagramelementmappings = new ArrayList<>();
        this.edgemappings = new ArrayList<>();
        this.diagramelementmappings = new ArrayList<>();
    }

    public diagram_tool_EdgeCreationDescription(
        String connectionStartPrecondition,        String iconPath        ArrayList<DiagramElementMapping> diagramelementmappings,        ArrayList<EdgeMapping> edgemappings,        ArrayList<DiagramElementMapping> diagramelementmappings    ) {
        this.connectionStartPrecondition = connectionStartPrecondition;
        this.iconPath = iconPath;
        this.diagramelementmappings = diagramelementmappings;
        this.edgemappings = edgemappings;
        this.diagramelementmappings = diagramelementmappings;
    }

    public String getConnectionstartprecondition() {
        return connectionStartPrecondition;
    }

    public void setConnectionstartprecondition(String connectionStartPrecondition) {
        this.connectionStartPrecondition = connectionStartPrecondition;
    }
    public String getIconpath() {
        return iconPath;
    }

    public void setIconpath(String iconPath) {
        this.iconPath = iconPath;
    }

    public List<DiagramElementMapping> getDiagramelementmappings() {
        return diagramelementmappings;
    }

    public void addDiagramelementmapping(Diagramelementmapping diagramelementmapping) {
        this.diagramelementmappings.add(diagramelementmapping);
    }
    public List<EdgeMapping> getEdgemappings() {
        return edgemappings;
    }

    public void addEdgemapping(Edgemapping edgemapping) {
        this.edgemappings.add(edgemapping);
    }
    public List<DiagramElementMapping> getDiagramelementmappings() {
        return diagramelementmappings;
    }

    public void addDiagramelementmapping(Diagramelementmapping diagramelementmapping) {
        this.diagramelementmappings.add(diagramelementmapping);
    }

}