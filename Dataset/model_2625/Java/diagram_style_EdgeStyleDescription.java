





import java.util.List;
import java.util.ArrayList;

public class diagram_style_EdgeStyleDescription extends StyleDescription {

    private String routingStyle;
    private String foldingStyle;
    private String targetArrow;
    private String sourceArrow;
    private String lineStyle;
    private String sizeComputationExpression;
    private String endsCentering;





    private List<DiagramElementMapping> diagramelementmappings;




    private List<DiagramElementMapping> diagramelementmappings;


    public diagram_style_EdgeStyleDescription(
        String routingStyle,        String foldingStyle,        String targetArrow,        String sourceArrow,        String lineStyle,        String sizeComputationExpression,        String endsCentering    ) {
        super(
        );
        this.routingStyle = routingStyle;
        this.foldingStyle = foldingStyle;
        this.targetArrow = targetArrow;
        this.sourceArrow = sourceArrow;
        this.lineStyle = lineStyle;
        this.sizeComputationExpression = sizeComputationExpression;
        this.endsCentering = endsCentering;
        this.diagramelementmappings = new ArrayList<>();
        this.diagramelementmappings = new ArrayList<>();
    }

    public diagram_style_EdgeStyleDescription(
        String routingStyle,        String foldingStyle,        String targetArrow,        String sourceArrow,        String lineStyle,        String sizeComputationExpression,        String endsCentering        ArrayList<DiagramElementMapping> diagramelementmappings,        ArrayList<DiagramElementMapping> diagramelementmappings    ) {
        this.routingStyle = routingStyle;
        this.foldingStyle = foldingStyle;
        this.targetArrow = targetArrow;
        this.sourceArrow = sourceArrow;
        this.lineStyle = lineStyle;
        this.sizeComputationExpression = sizeComputationExpression;
        this.endsCentering = endsCentering;
        this.diagramelementmappings = diagramelementmappings;
        this.diagramelementmappings = diagramelementmappings;
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
    public String getLinestyle() {
        return lineStyle;
    }

    public void setLinestyle(String lineStyle) {
        this.lineStyle = lineStyle;
    }
    public String getSizecomputationexpression() {
        return sizeComputationExpression;
    }

    public void setSizecomputationexpression(String sizeComputationExpression) {
        this.sizeComputationExpression = sizeComputationExpression;
    }
    public String getEndscentering() {
        return endsCentering;
    }

    public void setEndscentering(String endsCentering) {
        this.endsCentering = endsCentering;
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