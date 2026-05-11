





import java.util.List;
import java.util.ArrayList;

public class diagram_style_NodeStyleDescription extends style_LabelStyleDescription, style_BorderedStyleDescription, style_HideLabelCapabilityStyleDescription, style_TooltipStyleDescription, style_StyleDescription {

    private String labelPosition;
    private String labelDirection;
    private String resizeKind;
    private String forbiddenSides;
    private String sizeComputationExpression;



    public diagram_style_NodeStyleDescription(
        String labelPosition,        String labelDirection,        String resizeKind,        String forbiddenSides,        String sizeComputationExpression    ) {
        super(
        );
        this.labelPosition = labelPosition;
        this.labelDirection = labelDirection;
        this.resizeKind = resizeKind;
        this.forbiddenSides = forbiddenSides;
        this.sizeComputationExpression = sizeComputationExpression;
    }


    public String getLabelposition() {
        return labelPosition;
    }

    public void setLabelposition(String labelPosition) {
        this.labelPosition = labelPosition;
    }
    public String getLabeldirection() {
        return labelDirection;
    }

    public void setLabeldirection(String labelDirection) {
        this.labelDirection = labelDirection;
    }
    public String getResizekind() {
        return resizeKind;
    }

    public void setResizekind(String resizeKind) {
        this.resizeKind = resizeKind;
    }
    public String getForbiddensides() {
        return forbiddenSides;
    }

    public void setForbiddensides(String forbiddenSides) {
        this.forbiddenSides = forbiddenSides;
    }
    public String getSizecomputationexpression() {
        return sizeComputationExpression;
    }

    public void setSizecomputationexpression(String sizeComputationExpression) {
        this.sizeComputationExpression = sizeComputationExpression;
    }


}