





import java.util.List;
import java.util.ArrayList;

public class shape_Ellipse extends Shape {






    private shape_RectangleEllipseLayout shape_rectangleellipselayout;




    private List<shape_Shape> shape_shapes;


    public shape_Ellipse(
    ) {
        super(
        );
        this.shape_shapes = new ArrayList<>();
    }

    public shape_Ellipse(
        ArrayList<shape_Shape> shape_shapes    ) {
        this.shape_shapes = shape_shapes;
    }


    public shape_RectangleEllipseLayout getShape_rectangleellipselayout() {
        return shape_rectangleellipselayout;
    }

    public void setShape_rectangleellipselayout(shape_RectangleEllipseLayout shape_rectangleellipselayout) {
        this.shape_rectangleellipselayout = shape_rectangleellipselayout;
    }
    public List<shape_Shape> getShape_shapes() {
        return shape_shapes;
    }

    public void addShape_shape(Shape_shape shape_shape) {
        this.shape_shapes.add(shape_shape);
    }

}