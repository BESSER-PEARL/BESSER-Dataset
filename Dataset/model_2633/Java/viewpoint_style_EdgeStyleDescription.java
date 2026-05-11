





import java.util.List;
import java.util.ArrayList;

public class viewpoint_style_EdgeStyleDescription extends StyleDescription {

    private String sizeComputationExpression;
    private String routingStyle;
    private String foldingStyle;
    private String targetArrow;
    private String sourceArrow;
    private String lineStyle;





    private ColorDescription colordescription;


    public viewpoint_style_EdgeStyleDescription(
        String sizeComputationExpression,        String routingStyle,        String foldingStyle,        String targetArrow,        String sourceArrow,        String lineStyle    ) {
        super(
        );
        this.sizeComputationExpression = sizeComputationExpression;
        this.routingStyle = routingStyle;
        this.foldingStyle = foldingStyle;
        this.targetArrow = targetArrow;
        this.sourceArrow = sourceArrow;
        this.lineStyle = lineStyle;
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

    public ColorDescription getColordescription() {
        return colordescription;
    }

    public void setColordescription(ColorDescription colordescription) {
        this.colordescription = colordescription;
    }

}