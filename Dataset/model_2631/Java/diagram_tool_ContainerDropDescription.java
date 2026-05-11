





import java.util.List;
import java.util.ArrayList;

public class diagram_tool_ContainerDropDescription extends MappingBasedToolDescription {

    private String dragSource;
    private boolean moveEdges;





    private List<DiagramElementMapping> diagramelementmappings;


    public diagram_tool_ContainerDropDescription(
        String dragSource,        boolean moveEdges    ) {
        super(
        );
        this.dragSource = dragSource;
        this.moveEdges = moveEdges;
        this.diagramelementmappings = new ArrayList<>();
    }

    public diagram_tool_ContainerDropDescription(
        String dragSource,        boolean moveEdges        ArrayList<DiagramElementMapping> diagramelementmappings    ) {
        this.dragSource = dragSource;
        this.moveEdges = moveEdges;
        this.diagramelementmappings = diagramelementmappings;
    }

    public String getDragsource() {
        return dragSource;
    }

    public void setDragsource(String dragSource) {
        this.dragSource = dragSource;
    }
    public boolean getMoveedges() {
        return moveEdges;
    }

    public void setMoveedges(boolean moveEdges) {
        this.moveEdges = moveEdges;
    }

    public List<DiagramElementMapping> getDiagramelementmappings() {
        return diagramelementmappings;
    }

    public void addDiagramelementmapping(Diagramelementmapping diagramelementmapping) {
        this.diagramelementmappings.add(diagramelementmapping);
    }

}