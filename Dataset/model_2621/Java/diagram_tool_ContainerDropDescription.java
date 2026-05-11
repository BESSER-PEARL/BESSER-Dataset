





import java.util.List;
import java.util.ArrayList;

public class diagram_tool_ContainerDropDescription extends MappingBasedToolDescription {

    private boolean moveEdges;
    private String dragSource;





    private List<DiagramElementMapping> diagramelementmappings;


    public diagram_tool_ContainerDropDescription(
        boolean moveEdges,        String dragSource    ) {
        super(
        );
        this.moveEdges = moveEdges;
        this.dragSource = dragSource;
        this.diagramelementmappings = new ArrayList<>();
    }

    public diagram_tool_ContainerDropDescription(
        boolean moveEdges,        String dragSource        ArrayList<DiagramElementMapping> diagramelementmappings    ) {
        this.moveEdges = moveEdges;
        this.dragSource = dragSource;
        this.diagramelementmappings = diagramelementmappings;
    }

    public boolean getMoveedges() {
        return moveEdges;
    }

    public void setMoveedges(boolean moveEdges) {
        this.moveEdges = moveEdges;
    }
    public String getDragsource() {
        return dragSource;
    }

    public void setDragsource(String dragSource) {
        this.dragSource = dragSource;
    }

    public List<DiagramElementMapping> getDiagramelementmappings() {
        return diagramelementmappings;
    }

    public void addDiagramelementmapping(Diagramelementmapping diagramelementmapping) {
        this.diagramelementmappings.add(diagramelementmapping);
    }

}