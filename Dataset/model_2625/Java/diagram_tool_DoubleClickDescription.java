





import java.util.List;
import java.util.ArrayList;

public class diagram_tool_DoubleClickDescription extends MappingBasedToolDescription {






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


    public List<DiagramElementMapping> getDiagramelementmappings() {
        return diagramelementmappings;
    }

    public void addDiagramelementmapping(Diagramelementmapping diagramelementmapping) {
        this.diagramelementmappings.add(diagramelementmapping);
    }

}