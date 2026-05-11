





import java.util.List;
import java.util.ArrayList;

public class mm_pictograms_BoxRelativeAnchor extends AdvancedAnchor {

    private float relativeHeight;
    private float relativeWidth;



    public mm_pictograms_BoxRelativeAnchor(
        float relativeHeight,        float relativeWidth    ) {
        super(
        );
        this.relativeHeight = relativeHeight;
        this.relativeWidth = relativeWidth;
    }


    public float getRelativeheight() {
        return relativeHeight;
    }

    public void setRelativeheight(float relativeHeight) {
        this.relativeHeight = relativeHeight;
    }
    public float getRelativewidth() {
        return relativeWidth;
    }

    public void setRelativewidth(float relativeWidth) {
        this.relativeWidth = relativeWidth;
    }


}