





import java.util.List;
import java.util.ArrayList;

public class diagram_tool_DoubleClickDescription extends MappingBasedToolDescription {






    private tool_InitialOperation tool_initialoperation;




    private List<DiagramElementMapping> diagramelementmappings;


    public diagram_tool_DoubleClickDescription(
    ) {
        super(
        );
        this.diagramelementmappings = new ArrayList<>();
    }

    public diagram_tool_DoubleClickDescription(
        ArrayList<DiagramElementMapping> diagramelementmappings    ) {
        this.diagramelementmappings = diagramelementmappings;
    }


    public tool_InitialOperation getTool_initialoperation() {
        return tool_initialoperation;
    }

    public void setTool_initialoperation(tool_InitialOperation tool_initialoperation) {
        this.tool_initialoperation = tool_initialoperation;
    }
    public List<DiagramElementMapping> getDiagramelementmappings() {
        return diagramelementmappings;
    }

    public void addDiagramelementmapping(Diagramelementmapping diagramelementmapping) {
        this.diagramelementmappings.add(diagramelementmapping);
    }

}