





import java.util.List;
import java.util.ArrayList;

public class viewpoint_style_NodeStyleDescription extends style_LabelStyleDescription, style_BorderedStyleDescription, style_StyleDescription, style_TooltipStyleDescription {

    private String labelPosition;
    private String sizeComputationExpression;
    private String resizeKind;
    private boolean hideLabelByDefault;



    public viewpoint_style_NodeStyleDescription(
        String labelPosition,        String sizeComputationExpression,        String resizeKind,        boolean hideLabelByDefault    ) {
        super(
        );
        this.labelPosition = labelPosition;
        this.sizeComputationExpression = sizeComputationExpression;
        this.resizeKind = resizeKind;
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
    public boolean getHidelabelbydefault() {
        return hideLabelByDefault;
    }

    public void setHidelabelbydefault(boolean hideLabelByDefault) {
        this.hideLabelByDefault = hideLabelByDefault;
    }


}