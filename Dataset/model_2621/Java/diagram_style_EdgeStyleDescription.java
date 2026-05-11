





import java.util.List;
import java.util.ArrayList;

public class diagram_style_EdgeStyleDescription extends StyleDescription {

    private String sourceArrow;
    private String routingStyle;
    private String lineStyle;
    private String sizeComputationExpression;
    private String foldingStyle;
    private String endsCentering;
    private String targetArrow;





    private List<DiagramElementMapping> diagramelementmappings;




    private ColorDescription colordescription;




    private List<DiagramElementMapping> diagramelementmappings;


    public diagram_style_EdgeStyleDescription(
        String sourceArrow,        String routingStyle,        String lineStyle,        String sizeComputationExpression,        String foldingStyle,        String endsCentering,        String targetArrow    ) {
        super(
        );
        this.sourceArrow = sourceArrow;
        this.routingStyle = routingStyle;
        this.lineStyle = lineStyle;
        this.sizeComputationExpression = sizeComputationExpression;
        this.foldingStyle = foldingStyle;
        this.endsCentering = endsCentering;
        this.targetArrow = targetArrow;
        this.diagramelementmappings = new ArrayList<>();
        this.diagramelementmappings = new ArrayList<>();
    }

    public diagram_style_EdgeStyleDescription(
        String sourceArrow,        String routingStyle,        String lineStyle,        String sizeComputationExpression,        String foldingStyle,        String endsCentering,        String targetArrow        ArrayList<DiagramElementMapping> diagramelementmappings,        ArrayList<DiagramElementMapping> diagramelementmappings    ) {
        this.sourceArrow = sourceArrow;
        this.routingStyle = routingStyle;
        this.lineStyle = lineStyle;
        this.sizeComputationExpression = sizeComputationExpression;
        this.foldingStyle = foldingStyle;
        this.endsCentering = endsCentering;
        this.targetArrow = targetArrow;
        this.diagramelementmappings = diagramelementmappings;
        this.diagramelementmappings = diagramelementmappings;
    }

    public String getSourcearrow() {
        return sourceArrow;
    }

    public void setSourcearrow(String sourceArrow) {
        this.sourceArrow = sourceArrow;
    }
    public String getRoutingstyle() {
        return routingStyle;
    }

    public void setRoutingstyle(String routingStyle) {
        this.routingStyle = routingStyle;
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

    public List<DiagramElementMapping> getDiagramelementmappings() {
        return diagramelementmappings;
    }

    public void addDiagramelementmapping(Diagramelementmapping diagramelementmapping) {
        this.diagramelementmappings.add(diagramelementmapping);
    }
    public ColorDescription getColordescription() {
        return colordescription;
    }

    public void setColordescription(ColorDescription colordescription) {
        this.colordescription = colordescription;
    }
    public List<DiagramElementMapping> getDiagramelementmappings() {
        return diagramelementmappings;
    }

    public void addDiagramelementmapping(Diagramelementmapping diagramelementmapping) {
        this.diagramelementmappings.add(diagramelementmapping);
    }

}