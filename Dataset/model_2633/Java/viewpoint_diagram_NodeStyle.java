





import java.util.List;
import java.util.ArrayList;

public class viewpoint_diagram_NodeStyle extends Style, diagram_BorderedStyle, LabelStyle {

    private String labelPosition;
    private boolean hideLabelByDefault;



    public viewpoint_diagram_NodeStyle(
        String labelPosition,        boolean hideLabelByDefault    ) {
        super(
        );
        this.labelPosition = labelPosition;
        this.hideLabelByDefault = hideLabelByDefault;
    }


    public String getLabelposition() {
        return labelPosition;
    }

    public void setLabelposition(String labelPosition) {
        this.labelPosition = labelPosition;
    }
    public boolean getHidelabelbydefault() {
        return hideLabelByDefault;
    }

    public void setHidelabelbydefault(boolean hideLabelByDefault) {
        this.hideLabelByDefault = hideLabelByDefault;
    }


}