





import java.util.List;
import java.util.ArrayList;

public class DatadiagramMLBasicDef_ShapesCollection extends PageElt, MasterElt {






    private List<Shape> shapes;


    public DatadiagramMLBasicDef_ShapesCollection(
    ) {
        super(
        );
        this.shapes = new ArrayList<>();
    }

    public DatadiagramMLBasicDef_ShapesCollection(
        ArrayList<Shape> shapes    ) {
        this.shapes = shapes;
    }


    public List<Shape> getShapes() {
        return shapes;
    }

    public void addShape(Shape shape) {
        this.shapes.add(shape);
    }

}