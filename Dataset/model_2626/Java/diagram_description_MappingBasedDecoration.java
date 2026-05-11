





import java.util.List;
import java.util.ArrayList;

public class diagram_description_MappingBasedDecoration extends DecorationDescription {






    private List<DiagramElementMapping> diagramelementmappings;


    public diagram_description_MappingBasedDecoration(
    ) {
        super(
        );
        this.diagramelementmappings = new ArrayList<>();
    }

    public diagram_description_MappingBasedDecoration(
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