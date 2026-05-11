





import java.util.List;
import java.util.ArrayList;

public class diagram_style_EdgeStyleDescription extends StyleDescription {

    private String endsCentering;
    private String lineStyle;
    private String routingStyle;
    private String foldingStyle;
    private String targetArrow;
    private String sourceArrow;
    private String sizeComputationExpression;





    private List<DiagramElementMapping> diagramelementmappings;




    private List<DiagramElementMapping> diagramelementmappings;


    public diagram_style_EdgeStyleDescription(
        String endsCentering,        String lineStyle,        String routingStyle,        String foldingStyle,        String targetArrow,        String sourceArrow,        String sizeComputationExpression    ) {
        super(
        );
        this.endsCentering = endsCentering;
        this.lineStyle = lineStyle;
        this.routingStyle = routingStyle;
        this.foldingStyle = foldingStyle;
        this.targetArrow = targetArrow;
        this.sourceArrow = sourceArrow;
        this.sizeComputationExpression = sizeComputationExpression;
        this.diagramelementmappings = new ArrayList<>();
        this.diagramelementmappings = new ArrayList<>();
    }

    public diagram_style_EdgeStyleDescription(
        String endsCentering,        String lineStyle,        String routingStyle,        String foldingStyle,        String targetArrow,        String sourceArrow,        String sizeComputationExpression        ArrayList<DiagramElementMapping> diagramelementmappings,        ArrayList<DiagramElementMapping> diagramelementmappings    ) {
        this.endsCentering = endsCentering;
        this.lineStyle = lineStyle;
        this.routingStyle = routingStyle;
        this.foldingStyle = foldingStyle;
        this.targetArrow = targetArrow;
        this.sourceArrow = sourceArrow;
        this.sizeComputationExpression = sizeComputationExpression;
        this.diagramelementmappings = diagramelementmappings;
        this.diagramelementmappings = diagramelementmappings;
    }

    public String getEndscentering() {
        return endsCentering;
    }

    public void setEndscentering(String endsCentering) {
        this.endsCentering = endsCentering;
    }
    public String getLinestyle() {
        return lineStyle;
    }

    public void setLinestyle(String lineStyle) {
        this.lineStyle = lineStyle;
    }
    public String getRoutingstyle() {
        return routingStyle;
    }

    public void setRoutingstyle(String routingStyle) {
        this.routingStyle = routingStyle;
    }
    public String getFoldingstyle() {
        return foldingStyle;
    }

    public void setFoldingstyle(String foldingStyle) {
        this.foldingStyle = foldingStyle;
    }
    public String getTargetarrow() {
        return targetArrow;
    }

    public void setTargetarrow(String targetArrow) {
        this.targetArrow = targetArrow;
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