





import java.util.List;
import java.util.ArrayList;

public class shape_CommonLayout  {

    private int ycor;
    private int heigth;
    private int width;
    private int xcor;





    private shape_TextLayout shape_textlayout;




    private shape_RoundedRectangleLayout shape_roundedrectanglelayout;




    private shape_RectangleEllipseLayout shape_rectangleellipselayout;


    public shape_CommonLayout(
        int ycor,        int heigth,        int width,        int xcor    ) {
        this.ycor = ycor;
        this.heigth = heigth;
        this.width = width;
        this.xcor = xcor;
    }


    public int getYcor() {
        return ycor;
    }

    public void setYcor(int ycor) {
        this.ycor = ycor;
    }
    public int getHeigth() {
        return heigth;
    }

    public void setHeigth(int heigth) {
        this.heigth = heigth;
    }
    public int getWidth() {
        return width;
    }

    public void setWidth(int width) {
        this.width = width;
    }
    public int getXcor() {
        return xcor;
    }

    public void setXcor(int xcor) {
        this.xcor = xcor;
    }

    public shape_TextLayout getShape_textlayout() {
        return shape_textlayout;
    }

    public void setShape_textlayout(shape_TextLayout shape_textlayout) {
        this.shape_textlayout = shape_textlayout;
    }
    public shape_RoundedRectangleLayout getShape_roundedrectanglelayout() {
        return shape_roundedrectanglelayout;
    }

    public void setShape_roundedrectanglelayout(shape_RoundedRectangleLayout shape_roundedrectanglelayout) {
        this.shape_roundedrectanglelayout = shape_roundedrectanglelayout;
    }
    public shape_RectangleEllipseLayout getShape_rectangleellipselayout() {
        return shape_rectangleellipselayout;
    }

    public void setShape_rectangleellipselayout(shape_RectangleEllipseLayout shape_rectangleellipselayout) {
        this.shape_rectangleellipselayout = shape_rectangleellipselayout;
    }

}