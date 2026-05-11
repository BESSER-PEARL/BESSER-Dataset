





import java.util.List;
import java.util.ArrayList;

public class shape_Point  {

    private int curveBefore;
    private int curveAfter;
    private String xcor;
    private String ycor;





    private shape_PolyLineLayout shape_polylinelayout;




    private shape_LineLayout shape_linelayout;


    public shape_Point(
        int curveBefore,        int curveAfter,        String xcor,        String ycor    ) {
        this.curveBefore = curveBefore;
        this.curveAfter = curveAfter;
        this.xcor = xcor;
        this.ycor = ycor;
    }


    public int getCurvebefore() {
        return curveBefore;
    }

    public void setCurvebefore(int curveBefore) {
        this.curveBefore = curveBefore;
    }
    public int getCurveafter() {
        return curveAfter;
    }

    public void setCurveafter(int curveAfter) {
        this.curveAfter = curveAfter;
    }
    public String getXcor() {
        return xcor;
    }

    public void setXcor(String xcor) {
        this.xcor = xcor;
    }
    public String getYcor() {
        return ycor;
    }

    public void setYcor(String ycor) {
        this.ycor = ycor;
    }

    public shape_PolyLineLayout getShape_polylinelayout() {
        return shape_polylinelayout;
    }

    public void setShape_polylinelayout(shape_PolyLineLayout shape_polylinelayout) {
        this.shape_polylinelayout = shape_polylinelayout;
    }
    public shape_LineLayout getShape_linelayout() {
        return shape_linelayout;
    }

    public void setShape_linelayout(shape_LineLayout shape_linelayout) {
        this.shape_linelayout = shape_linelayout;
    }

}