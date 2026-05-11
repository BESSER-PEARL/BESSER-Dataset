





import java.util.List;
import java.util.ArrayList;

public class diagram_style_NodeStyleDescription extends style_StyleDescription, style_HideLabelCapabilityStyleDescription, style_LabelStyleDescription, style_BorderedStyleDescription, style_TooltipStyleDescription {

    private String sizeComputationExpression;
    private String labelPosition;
    private String resizeKind;
    private String forbiddenSides;



    public diagram_style_NodeStyleDescription(
        String sizeComputationExpression,        String labelPosition,        String resizeKind,        String forbiddenSides    ) {
        super(
        );
        this.sizeComputationExpression = sizeComputationExpression;
        this.labelPosition = labelPosition;
        this.resizeKind = resizeKind;
        this.forbiddenSides = forbiddenSides;
    }


    public String getSizecomputationexpression() {
        return sizeComputationExpression;
    }

    public void setSizecomputationexpression(String sizeComputationExpression) {
        this.sizeComputationExpression = sizeComputationExpression;
    }
    public String getLabelposition() {
        return labelPosition;
    }

    public void setLabelposition(String labelPosition) {
        this.labelPosition = labelPosition;
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


}