





import java.util.List;
import java.util.ArrayList;

public class shape_RoundedRectangle extends Shape {






    private List<shape_Shape> shape_shapes;




    private shape_RoundedRectangleLayout shape_roundedrectanglelayout;


    public shape_RoundedRectangle(
    ) {
        super(
        );
        this.shape_shapes = new ArrayList<>();
    }

    public shape_RoundedRectangle(
        ArrayList<shape_Shape> shape_shapes    ) {
        this.shape_shapes = shape_shapes;
    }


    public List<shape_Shape> getShape_shapes() {
        return shape_shapes;
    }

    public void addShape_shape(Shape_shape shape_shape) {
        this.shape_shapes.add(shape_shape);
    }
    public shape_RoundedRectangleLayout getShape_roundedrectanglelayout() {
        return shape_roundedrectanglelayout;
    }

    public void setShape_roundedrectanglelayout(shape_RoundedRectangleLayout shape_roundedrectanglelayout) {
        this.shape_roundedrectanglelayout = shape_roundedrectanglelayout;
    }

}