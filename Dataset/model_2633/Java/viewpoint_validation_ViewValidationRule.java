





import java.util.List;
import java.util.ArrayList;

public class viewpoint_validation_ViewValidationRule extends ValidationRule {






    private List<description_DiagramElementMapping> description_diagramelementmappings;


    public viewpoint_validation_ViewValidationRule(
    ) {
        super(
        );
        this.description_diagramelementmappings = new ArrayList<>();
    }

    public viewpoint_validation_ViewValidationRule(
        ArrayList<description_DiagramElementMapping> description_diagramelementmappings    ) {
        this.description_diagramelementmappings = description_diagramelementmappings;
    }


    public List<description_DiagramElementMapping> getDescription_diagramelementmappings() {
        return description_diagramelementmappings;
    }

    public void addDescription_diagramelementmapping(Description_diagramelementmapping description_diagramelementmapping) {
        this.description_diagramelementmappings.add(description_diagramelementmapping);
    }

}