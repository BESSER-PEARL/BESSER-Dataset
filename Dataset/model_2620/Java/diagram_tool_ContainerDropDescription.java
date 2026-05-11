





import java.util.List;
import java.util.ArrayList;

public class diagram_tool_ContainerDropDescription extends MappingBasedToolDescription {

    private String dragSource;
    private boolean moveEdges;





    private tool_ContainerViewVariable tool_containerviewvariable;




    private List<DiagramElementMapping> diagramelementmappings;




    private tool_InitialContainerDropOperation tool_initialcontainerdropoperation;




    private tool_DropContainerVariable tool_dropcontainervariable;




    private tool_ElementDropVariable tool_elementdropvariable;




    private tool_DropContainerVariable tool_dropcontainervariable;


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

    public tool_ContainerViewVariable getTool_containerviewvariable() {
        return tool_containerviewvariable;
    }

    public void setTool_containerviewvariable(tool_ContainerViewVariable tool_containerviewvariable) {
        this.tool_containerviewvariable = tool_containerviewvariable;
    }
    public List<DiagramElementMapping> getDiagramelementmappings() {
        return diagramelementmappings;
    }

    public void addDiagramelementmapping(Diagramelementmapping diagramelementmapping) {
        this.diagramelementmappings.add(diagramelementmapping);
    }
    public tool_InitialContainerDropOperation getTool_initialcontainerdropoperation() {
        return tool_initialcontainerdropoperation;
    }

    public void setTool_initialcontainerdropoperation(tool_InitialContainerDropOperation tool_initialcontainerdropoperation) {
        this.tool_initialcontainerdropoperation = tool_initialcontainerdropoperation;
    }
    public tool_DropContainerVariable getTool_dropcontainervariable() {
        return tool_dropcontainervariable;
    }

    public void setTool_dropcontainervariable(tool_DropContainerVariable tool_dropcontainervariable) {
        this.tool_dropcontainervariable = tool_dropcontainervariable;
    }
    public tool_ElementDropVariable getTool_elementdropvariable() {
        return tool_elementdropvariable;
    }

    public void setTool_elementdropvariable(tool_ElementDropVariable tool_elementdropvariable) {
        this.tool_elementdropvariable = tool_elementdropvariable;
    }
    public tool_DropContainerVariable getTool_dropcontainervariable() {
        return tool_dropcontainervariable;
    }

    public void setTool_dropcontainervariable(tool_DropContainerVariable tool_dropcontainervariable) {
        this.tool_dropcontainervariable = tool_dropcontainervariable;
    }

}