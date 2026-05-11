





import java.util.List;
import java.util.ArrayList;

public class viewpoint_filter_MappingFilter extends Filter {

    private String viewConditionExpression;
    private String semanticConditionExpression;





    private List<description_DiagramElementMapping> description_diagramelementmappings;


    public viewpoint_filter_MappingFilter(
        String viewConditionExpression,        String semanticConditionExpression    ) {
        super(
        );
        this.viewConditionExpression = viewConditionExpression;
        this.semanticConditionExpression = semanticConditionExpression;
        this.description_diagramelementmappings = new ArrayList<>();
    }

    public viewpoint_filter_MappingFilter(
        String viewConditionExpression,        String semanticConditionExpression        ArrayList<description_DiagramElementMapping> description_diagramelementmappings    ) {
        this.viewConditionExpression = viewConditionExpression;
        this.semanticConditionExpression = semanticConditionExpression;
        this.description_diagramelementmappings = description_diagramelementmappings;
    }

    public String getViewconditionexpression() {
        return viewConditionExpression;
    }

    public void setViewconditionexpression(String viewConditionExpression) {
        this.viewConditionExpression = viewConditionExpression;
    }
    public String getSemanticconditionexpression() {
        return semanticConditionExpression;
    }

    public void setSemanticconditionexpression(String semanticConditionExpression) {
        this.semanticConditionExpression = semanticConditionExpression;
    }

    public List<description_DiagramElementMapping> getDescription_diagramelementmappings() {
        return description_diagramelementmappings;
    }

    public void addDescription_diagramelementmapping(Description_diagramelementmapping description_diagramelementmapping) {
        this.description_diagramelementmappings.add(description_diagramelementmapping);
    }

}