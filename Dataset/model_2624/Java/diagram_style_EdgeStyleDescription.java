





import java.util.List;
import java.util.ArrayList;

public class diagram_style_EdgeStyleDescription extends StyleDescription {

    private String foldingStyle;
    private String endsCentering;
    private String targetArrow;
    private String lineStyle;
    private String sourceArrow;
    private String sizeComputationExpression;
    private String routingStyle;





    private List<DiagramElementMapping> diagramelementmappings;




    private List<DiagramElementMapping> diagramelementmappings;


    public diagram_style_EdgeStyleDescription(
        String foldingStyle,        String endsCentering,        String targetArrow,        String lineStyle,        String sourceArrow,        String sizeComputationExpression,        String routingStyle    ) {
        super(
        );
        this.foldingStyle = foldingStyle;
        this.endsCentering = endsCentering;
        this.targetArrow = targetArrow;
        this.lineStyle = lineStyle;
        this.sourceArrow = sourceArrow;
        this.sizeComputationExpression = sizeComputationExpression;
        this.routingStyle = routingStyle;
        this.diagramelementmappings = new ArrayList<>();
        this.diagramelementmappings = new ArrayList<>();
    }

    public diagram_style_EdgeStyleDescription(
        String foldingStyle,        String endsCentering,        String targetArrow,        String lineStyle,        String sourceArrow,        String sizeComputationExpression,        String routingStyle        ArrayList<DiagramElementMapping> diagramelementmappings,        ArrayList<DiagramElementMapping> diagramelementmappings    ) {
        this.foldingStyle = foldingStyle;
        this.endsCentering = endsCentering;
        this.targetArrow = targetArrow;
        this.lineStyle = lineStyle;
        this.sourceArrow = sourceArrow;
        this.sizeComputationExpression = sizeComputationExpression;
        this.routingStyle = routingStyle;
        this.diagramelementmappings = diagramelementmappings;
        this.diagramelementmappings = diagramelementmappings;
    }

    public String getFoldingstyle() {
        return foldingStyle;
    }

    public void setFoldingstyle(String foldingStyle) {
        this.foldingStyle = foldingStyle;
    }
    public String getEndscentering() {
        return endsCentering;
    }

    public void setEndscentering(String endsCentering) {
        this.endsCentering = endsCentering;
    }
    public String getTargetarrow() {
        return targetArrow;
    }

    public void setTargetarrow(String targetArrow) {
        this.targetArrow = targetArrow;
    }
    public String getLinestyle() {
        return lineStyle;
    }

    public void setLinestyle(String lineStyle) {
        this.lineStyle = lineStyle;
    }
    public String getSourcearrow() {
        return sourceArrow;
    }

    public void setSourcearrow(String sourceArrow) {
        this.sourceArrow = sourceArrow;
    }
    public String getSizecomputationexpression() {
        return sizeComputationExpression;
    }

    public void setSizecomputationexpression(String sizeComputationExpression) {
        this.sizeComputationExpression = sizeComputationExpression;
    }
    public String getRoutingstyle() {
        return routingStyle;
    }

    public void setRoutingstyle(String routingStyle) {
        this.routingStyle = routingStyle;
    }

    public List<DiagramElementMapping> getDiagramelementmappings() {
        return diagramelementmappings;
    }

    public void addDiagramelementmapping(Diagramelementmapping diagramelementmapping) {
        this.diagramelementmappings.add(diagramelementmapping);
    }
    public List<DiagramElementMapping> getDiagramelementmappings() {
        return diagramelementmappings;
    }

    public void addDiagramelementmapping(Diagramelementmapping diagramelementmapping) {
        this.diagramelementmappings.add(diagramelementmapping);
    }

}