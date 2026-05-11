





import java.util.List;
import java.util.ArrayList;

public class diagram_style_ContainerStyleDescription extends style_LabelStyleDescription, style_BorderedStyleDescription, style_HideLabelCapabilityStyleDescription, style_TooltipStyleDescription, style_RoundedCornerStyleDescription {

    private boolean roundedCorner;
    private String containerLabelDirection;



    public diagram_style_ContainerStyleDescription(
        boolean roundedCorner,        String containerLabelDirection    ) {
        super(
        );
        this.roundedCorner = roundedCorner;
        this.containerLabelDirection = containerLabelDirection;
    }


    public boolean getRoundedcorner() {
        return roundedCorner;
    }

    public void setRoundedcorner(boolean roundedCorner) {
        this.roundedCorner = roundedCorner;
    }
    public String getContainerlabeldirection() {
        return containerLabelDirection;
    }

    public void setContainerlabeldirection(String containerLabelDirection) {
        this.containerLabelDirection = containerLabelDirection;
    }


}