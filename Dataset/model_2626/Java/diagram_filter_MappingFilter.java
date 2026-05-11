





import java.util.List;
import java.util.ArrayList;

public class diagram_filter_MappingFilter extends Filter {

    private String semanticConditionExpression;
    private String viewConditionExpression;





    private List<DiagramElementMapping> diagramelementmappings;


    public diagram_filter_MappingFilter(
        String semanticConditionExpression,        String viewConditionExpression    ) {
        super(
        );
        this.semanticConditionExpression = semanticConditionExpression;
        this.viewConditionExpression = viewConditionExpression;
        this.diagramelementmappings = new ArrayList<>();
    }

    public diagram_filter_MappingFilter(
        String semanticConditionExpression,        String viewConditionExpression        ArrayList<DiagramElementMapping> diagramelementmappings    ) {
        this.semanticConditionExpression = semanticConditionExpression;
        this.viewConditionExpression = viewConditionExpression;
        this.diagramelementmappings = diagramelementmappings;
    }

    public String getSemanticconditionexpression() {
        return semanticConditionExpression;
    }

    public void setSemanticconditionexpression(String semanticConditionExpression) {
        this.semanticConditionExpression = semanticConditionExpression;
    }
    public String getViewconditionexpression() {
        return viewConditionExpression;
    }

    public void setViewconditionexpression(String viewConditionExpression) {
        this.viewConditionExpression = viewConditionExpression;
    }

    public List<DiagramElementMapping> getDiagramelementmappings() {
        return diagramelementmappings;
    }

    public void addDiagramelementmapping(Diagramelementmapping diagramelementmapping) {
        this.diagramelementmappings.add(diagramelementmapping);
    }

}