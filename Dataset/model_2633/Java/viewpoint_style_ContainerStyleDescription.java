





import java.util.List;
import java.util.ArrayList;

public class viewpoint_style_ContainerStyleDescription extends style_LabelStyleDescription, style_BorderedStyleDescription, style_RoundedCornerStyleDescription, style_TooltipStyleDescription {

    private boolean roundedCorner;



    public viewpoint_style_ContainerStyleDescription(
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