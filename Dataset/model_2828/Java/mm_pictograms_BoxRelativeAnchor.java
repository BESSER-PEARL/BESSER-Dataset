





import java.util.List;
import java.util.ArrayList;

public class mm_pictograms_BoxRelativeAnchor extends AdvancedAnchor {

    private float relativeWidth;
    private float relativeHeight;



    public mm_pictograms_BoxRelativeAnchor(
        float relativeWidth,        float relativeHeight    ) {
        super(
        );
        this.relativeWidth = relativeWidth;
        this.relativeHeight = relativeHeight;
    }


    public float getRelativewidth() {
        return relativeWidth;
    }

    public void setRelativewidth(float relativeWidth) {
        this.relativeWidth = relativeWidth;
    }
    public float getRelativeheight() {
        return relativeHeight;
    }

    public void setRelativeheight(float relativeHeight) {
        this.relativeHeight = relativeHeight;
    }


}