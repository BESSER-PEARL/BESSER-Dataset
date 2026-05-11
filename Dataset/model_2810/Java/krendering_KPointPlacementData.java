





import java.util.List;
import java.util.ArrayList;

public class krendering_KPointPlacementData extends KPlacementData {

    private String horizontalAlignment;
    private float minHeight;
    private String verticalAlignment;
    private float horizontalMargin;
    private float verticalMargin;
    private float minWidth;





    private krendering_KPosition krendering_kposition;


    public krendering_KPointPlacementData(
        String horizontalAlignment,        float minHeight,        String verticalAlignment,        float horizontalMargin,        float verticalMargin,        float minWidth    ) {
        super(
        );
        this.horizontalAlignment = horizontalAlignment;
        this.minHeight = minHeight;
        this.verticalAlignment = verticalAlignment;
        this.horizontalMargin = horizontalMargin;
        this.verticalMargin = verticalMargin;
        this.minWidth = minWidth;
    }


    public String getHorizontalalignment() {
        return horizontalAlignment;
    }

    public void setHorizontalalignment(String horizontalAlignment) {
        this.horizontalAlignment = horizontalAlignment;
    }
    public float getMinheight() {
        return minHeight;
    }

    public void setMinheight(float minHeight) {
        this.minHeight = minHeight;
    }
    public String getVerticalalignment() {
        return verticalAlignment;
    }

    public void setVerticalalignment(String verticalAlignment) {
        this.verticalAlignment = verticalAlignment;
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
    public float getMinwidth() {
        return minWidth;
    }

    public void setMinwidth(float minWidth) {
        this.minWidth = minWidth;
    }

    public krendering_KPosition getKrendering_kposition() {
        return krendering_kposition;
    }

    public void setKrendering_kposition(krendering_KPosition krendering_kposition) {
        this.krendering_kposition = krendering_kposition;
    }

}