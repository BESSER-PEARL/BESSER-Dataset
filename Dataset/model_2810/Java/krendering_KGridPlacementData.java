





import java.util.List;
import java.util.ArrayList;

public class krendering_KGridPlacementData extends KAreaPlacementData {

    private float minCellWidth;
    private String flexibleWidth;
    private float minCellHeight;
    private String flexibleHeight;



    public krendering_KGridPlacementData(
        float minCellWidth,        String flexibleWidth,        float minCellHeight,        String flexibleHeight    ) {
        super(
        );
        this.minCellWidth = minCellWidth;
        this.flexibleWidth = flexibleWidth;
        this.minCellHeight = minCellHeight;
        this.flexibleHeight = flexibleHeight;
    }


    public float getMincellwidth() {
        return minCellWidth;
    }

    public void setMincellwidth(float minCellWidth) {
        this.minCellWidth = minCellWidth;
    }
    public String getFlexiblewidth() {
        return flexibleWidth;
    }

    public void setFlexiblewidth(String flexibleWidth) {
        this.flexibleWidth = flexibleWidth;
    }
    public float getMincellheight() {
        return minCellHeight;
    }

    public void setMincellheight(float minCellHeight) {
        this.minCellHeight = minCellHeight;
    }
    public String getFlexibleheight() {
        return flexibleHeight;
    }

    public void setFlexibleheight(String flexibleHeight) {
        this.flexibleHeight = flexibleHeight;
    }


}