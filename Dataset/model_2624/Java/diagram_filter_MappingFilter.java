





import java.util.List;
import java.util.ArrayList;

public class diagram_filter_MappingFilter extends Filter {

    private String viewConditionExpression;
    private String semanticConditionExpression;





    private List<DiagramElementMapping> diagramelementmappings;


    public diagram_filter_MappingFilter(
        String viewConditionExpression,        String semanticConditionExpression    ) {
        super(
        );
        this.viewConditionExpression = viewConditionExpression;
        this.semanticConditionExpression = semanticConditionExpression;
        this.diagramelementmappings = new ArrayList<>();
    }

    public diagram_filter_MappingFilter(
        String viewConditionExpression,        String semanticConditionExpression        ArrayList<DiagramElementMapping> diagramelementmappings    ) {
        this.viewConditionExpression = viewConditionExpression;
        this.semanticConditionExpression = semanticConditionExpression;
        this.diagramelementmappings = diagramelementmappings;
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

    public List<DiagramElementMapping> getDiagramelementmappings() {
        return diagramelementmappings;
    }

    public void addDiagramelementmapping(Diagramelementmapping diagramelementmapping) {
        this.diagramelementmappings.add(diagramelementmapping);
    }

}