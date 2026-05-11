





import java.util.List;
import java.util.ArrayList;

public class shape_TextLayout  {

    private String vAlign;
    private String hAlign;





    private shape_ShapestyleLayout shape_shapestylelayout;




    private shape_CDText shape_cdtext;


    public shape_TextLayout(
        String vAlign,        String hAlign    ) {
        this.vAlign = vAlign;
        this.hAlign = hAlign;
    }


    public String getValign() {
        return vAlign;
    }

    public void setValign(String vAlign) {
        this.vAlign = vAlign;
    }
    public String getHalign() {
        return hAlign;
    }

    public void setHalign(String hAlign) {
        this.hAlign = hAlign;
    }

    public shape_ShapestyleLayout getShape_shapestylelayout() {
        return shape_shapestylelayout;
    }

    public void setShape_shapestylelayout(shape_ShapestyleLayout shape_shapestylelayout) {
        this.shape_shapestylelayout = shape_shapestylelayout;
    }
    public shape_CDText getShape_cdtext() {
        return shape_cdtext;
    }

    public void setShape_cdtext(shape_CDText shape_cdtext) {
        this.shape_cdtext = shape_cdtext;
    }

}