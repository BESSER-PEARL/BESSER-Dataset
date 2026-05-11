





import java.util.List;
import java.util.ArrayList;

public class diagram_style_EdgeStyleDescription extends StyleDescription {

    private String targetArrow;
    private String routingStyle;
    private String foldingStyle;
    private String lineStyle;
    private String sizeComputationExpression;
    private String sourceArrow;



    public diagram_style_EdgeStyleDescription(
        String targetArrow,        String routingStyle,        String foldingStyle,        String lineStyle,        String sizeComputationExpression,        String sourceArrow    ) {
        super(
        );
        this.targetArrow = targetArrow;
        this.routingStyle = routingStyle;
        this.foldingStyle = foldingStyle;
        this.lineStyle = lineStyle;
        this.sizeComputationExpression = sizeComputationExpression;
        this.sourceArrow = sourceArrow;
    }


    public String getTargetarrow() {
        return targetArrow;
    }

    public void setTargetarrow(String targetArrow) {
        this.targetArrow = targetArrow;
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
    public String getSourcearrow() {
        return sourceArrow;
    }

    public void setSourcearrow(String sourceArrow) {
        this.sourceArrow = sourceArrow;
    }


}