





import java.util.List;
import java.util.ArrayList;

public class diagram_style_NodeStyleDescription extends style_LabelStyleDescription, style_TooltipStyleDescription, style_BorderedStyleDescription, style_StyleDescription {

    private boolean hideLabelByDefault;
    private String labelPosition;
    private String sizeComputationExpression;
    private String resizeKind;



    public diagram_style_NodeStyleDescription(
        boolean hideLabelByDefault,        String labelPosition,        String sizeComputationExpression,        String resizeKind    ) {
        super(
        );
        this.hideLabelByDefault = hideLabelByDefault;
        this.labelPosition = labelPosition;
        this.sizeComputationExpression = sizeComputationExpression;
        this.resizeKind = resizeKind;
    }


    public boolean getHidelabelbydefault() {
        return hideLabelByDefault;
    }

    public void setHidelabelbydefault(boolean hideLabelByDefault) {
        this.hideLabelByDefault = hideLabelByDefault;
    }
    public String getLabelposition() {
        return labelPosition;
    }

    public void setLabelposition(String labelPosition) {
        this.labelPosition = labelPosition;
    }
    public String getSizecomputationexpression() {
        return sizeComputationExpression;
    }

    public void setSizecomputationexpression(String sizeComputationExpression) {
        this.sizeComputationExpression = sizeComputationExpression;
    }
    public String getResizekind() {
        return resizeKind;
    }

    public void setResizekind(String resizeKind) {
        this.resizeKind = resizeKind;
    }


}