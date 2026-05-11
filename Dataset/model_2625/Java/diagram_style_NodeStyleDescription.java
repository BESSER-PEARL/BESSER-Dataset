





import java.util.List;
import java.util.ArrayList;

public class diagram_style_NodeStyleDescription extends style_BorderedStyleDescription, style_TooltipStyleDescription, style_StyleDescription, style_LabelStyleDescription, style_HideLabelCapabilityStyleDescription {

    private String resizeKind;
    private String forbiddenSides;
    private String sizeComputationExpression;
    private String labelPosition;



    public diagram_style_NodeStyleDescription(
        String resizeKind,        String forbiddenSides,        String sizeComputationExpression,        String labelPosition    ) {
        super(
        );
        this.resizeKind = resizeKind;
        this.forbiddenSides = forbiddenSides;
        this.sizeComputationExpression = sizeComputationExpression;
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


}