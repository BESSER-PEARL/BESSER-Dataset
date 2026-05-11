





import java.util.List;
import java.util.ArrayList;

public class diagram_style_ContainerStyleDescription extends style_LabelStyleDescription, style_TooltipStyleDescription, style_HideLabelCapabilityStyleDescription, style_RoundedCornerStyleDescription, style_BorderedStyleDescription {

    private boolean roundedCorner;



    public diagram_style_ContainerStyleDescription(
        boolean roundedCorner    ) {
        super(
        );
        this.roundedCorner = roundedCorner;
    }


    public boolean getRoundedcorner() {
        return roundedCorner;
    }

    public void setRoundedcorner(boolean roundedCorner) {
        this.roundedCorner = roundedCorner;
    }


}