





import java.util.List;
import java.util.ArrayList;

public class shape_ShapeLayout  {

    private int maxheight;
    private String stretchH;
    private String proportional;
    private int minheight;
    private int maxwidth;
    private String stretchV;
    private int minwidth;





    private shape_ShapeDefinition shape_shapedefinition;


    public shape_ShapeLayout(
        int maxheight,        String stretchH,        String proportional,        int minheight,        int maxwidth,        String stretchV,        int minwidth    ) {
        this.maxheight = maxheight;
        this.stretchH = stretchH;
        this.proportional = proportional;
        this.minheight = minheight;
        this.maxwidth = maxwidth;
        this.stretchV = stretchV;
        this.minwidth = minwidth;
    }


    public int getMaxheight() {
        return maxheight;
    }

    public void setMaxheight(int maxheight) {
        this.maxheight = maxheight;
    }
    public String getStretchh() {
        return stretchH;
    }

    public void setStretchh(String stretchH) {
        this.stretchH = stretchH;
    }
    public String getProportional() {
        return proportional;
    }

    public void setProportional(String proportional) {
        this.proportional = proportional;
    }
    public int getMinheight() {
        return minheight;
    }

    public void setMinheight(int minheight) {
        this.minheight = minheight;
    }
    public int getMaxwidth() {
        return maxwidth;
    }

    public void setMaxwidth(int maxwidth) {
        this.maxwidth = maxwidth;
    }
    public String getStretchv() {
        return stretchV;
    }

    public void setStretchv(String stretchV) {
        this.stretchV = stretchV;
    }
    public int getMinwidth() {
        return minwidth;
    }

    public void setMinwidth(int minwidth) {
        this.minwidth = minwidth;
    }

    public shape_ShapeDefinition getShape_shapedefinition() {
        return shape_shapedefinition;
    }

    public void setShape_shapedefinition(shape_ShapeDefinition shape_shapedefinition) {
        this.shape_shapedefinition = shape_shapedefinition;
    }

}