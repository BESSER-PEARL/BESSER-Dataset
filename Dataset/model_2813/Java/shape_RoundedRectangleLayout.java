





import java.util.List;
import java.util.ArrayList;

public class shape_RoundedRectangleLayout  {

    private int curveHeight;
    private int curveWidth;





    private shape_ShapestyleLayout shape_shapestylelayout;




    private shape_CDRoundedRectangle shape_cdroundedrectangle;


    public shape_RoundedRectangleLayout(
        int curveHeight,        int curveWidth    ) {
        this.curveHeight = curveHeight;
        this.curveWidth = curveWidth;
    }


    public int getCurveheight() {
        return curveHeight;
    }

    public void setCurveheight(int curveHeight) {
        this.curveHeight = curveHeight;
    }
    public int getCurvewidth() {
        return curveWidth;
    }

    public void setCurvewidth(int curveWidth) {
        this.curveWidth = curveWidth;
    }

    public shape_ShapestyleLayout getShape_shapestylelayout() {
        return shape_shapestylelayout;
    }

    public void setShape_shapestylelayout(shape_ShapestyleLayout shape_shapestylelayout) {
        this.shape_shapestylelayout = shape_shapestylelayout;
    }
    public shape_CDRoundedRectangle getShape_cdroundedrectangle() {
        return shape_cdroundedrectangle;
    }

    public void setShape_cdroundedrectangle(shape_CDRoundedRectangle shape_cdroundedrectangle) {
        this.shape_cdroundedrectangle = shape_cdroundedrectangle;
    }

}