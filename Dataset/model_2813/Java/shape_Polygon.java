





import java.util.List;
import java.util.ArrayList;

public class shape_Polygon extends Shape {






    private shape_PolyLineLayout shape_polylinelayout;




    private List<shape_Shape> shape_shapes;


    public shape_Polygon(
    ) {
        super(
        );
        this.shape_shapes = new ArrayList<>();
    }

    public shape_Polygon(
        ArrayList<shape_Shape> shape_shapes    ) {
        this.shape_shapes = shape_shapes;
    }


    public shape_PolyLineLayout getShape_polylinelayout() {
        return shape_polylinelayout;
    }

    public void setShape_polylinelayout(shape_PolyLineLayout shape_polylinelayout) {
        this.shape_polylinelayout = shape_polylinelayout;
    }
    public List<shape_Shape> getShape_shapes() {
        return shape_shapes;
    }

    public void addShape_shape(Shape_shape shape_shape) {
        this.shape_shapes.add(shape_shape);
    }

}