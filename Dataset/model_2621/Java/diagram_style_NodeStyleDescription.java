





import java.util.List;
import java.util.ArrayList;

public class diagram_style_NodeStyleDescription extends style_BorderedStyleDescription, style_LabelStyleDescription, style_StyleDescription, style_TooltipStyleDescription, style_HideLabelCapabilityStyleDescription {

    private String labelPosition;
    private String forbiddenSides;
    private String resizeKind;
    private String sizeComputationExpression;



    public diagram_style_NodeStyleDescription(
        String labelPosition,        String forbiddenSides,        String resizeKind,        String sizeComputationExpression    ) {
        super(
        );
        this.labelPosition = labelPosition;
        this.forbiddenSides = forbiddenSides;
        this.resizeKind = resizeKind;
        this.sizeComputationExpression = sizeComputationExpression;
    }


    public String getLabelposition() {
        return labelPosition;
    }

    public void setLabelposition(String labelPosition) {
        this.labelPosition = labelPosition;
    }
    public String getForbiddensides() {
        return forbiddenSides;
    }

    public void setForbiddensides(String forbiddenSides) {
        this.forbiddenSides = forbiddenSides;
    }
    public String getResizekind() {
        return resizeKind;
    }

    public void setResizekind(String resizeKind) {
        this.resizeKind = resizeKind;
    }
    public String getSizecomputationexpression() {
        return sizeComputationExpression;
    }

    public void setSizecomputationexpression(String sizeComputationExpression) {
        this.sizeComputationExpression = sizeComputationExpression;
    }


}