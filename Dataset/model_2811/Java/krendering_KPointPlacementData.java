





import java.util.List;
import java.util.ArrayList;

public class krendering_KPointPlacementData extends KPlacementData {

    private float minHeight;
    private String horizontalAlignment;
    private String verticalAlignment;
    private float minWidth;
    private float horizontalMargin;
    private float verticalMargin;





    private krendering_KPosition krendering_kposition;


    public krendering_KPointPlacementData(
        float minHeight,        String horizontalAlignment,        String verticalAlignment,        float minWidth,        float horizontalMargin,        float verticalMargin    ) {
        super(
        );
        this.minHeight = minHeight;
        this.horizontalAlignment = horizontalAlignment;
        this.verticalAlignment = verticalAlignment;
        this.minWidth = minWidth;
        this.horizontalMargin = horizontalMargin;
        this.verticalMargin = verticalMargin;
    }


    public float getMinheight() {
        return minHeight;
    }

    public void setMinheight(float minHeight) {
        this.minHeight = minHeight;
    }
    public String getHorizontalalignment() {
        return horizontalAlignment;
    }

    public void setHorizontalalignment(String horizontalAlignment) {
        this.horizontalAlignment = horizontalAlignment;
    }
    public String getVerticalalignment() {
        return verticalAlignment;
    }

    public void setVerticalalignment(String verticalAlignment) {
        this.verticalAlignment = verticalAlignment;
    }
    public float getMinwidth() {
        return minWidth;
    }

    public void setMinwidth(float minWidth) {
        this.minWidth = minWidth;
    }
    public float getHorizontalmargin() {
        return horizontalMargin;
    }

    public void setHorizontalmargin(float horizontalMargin) {
        this.horizontalMargin = horizontalMargin;
    }
    public float getVerticalmargin() {
        return verticalMargin;
    }

    public void setVerticalmargin(float verticalMargin) {
        this.verticalMargin = verticalMargin;
    }

    public krendering_KPosition getKrendering_kposition() {
        return krendering_kposition;
    }

    public void setKrendering_kposition(krendering_KPosition krendering_kposition) {
        this.krendering_kposition = krendering_kposition;
    }

}