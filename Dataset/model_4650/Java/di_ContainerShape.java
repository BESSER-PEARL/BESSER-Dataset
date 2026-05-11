





import java.util.List;
import java.util.ArrayList;

public class di_ContainerShape extends DiNode {






    private List<di_Shape> di_shapes;


    public di_ContainerShape(
    ) {
        super(
        );
        this.di_shapes = new ArrayList<>();
    }

    public di_ContainerShape(
        ArrayList<di_Shape> di_shapes    ) {
        this.di_shapes = di_shapes;
    }


    public List<di_Shape> getDi_shapes() {
        return di_shapes;
    }

    public void addDi_shape(Di_shape di_shape) {
        this.di_shapes.add(di_shape);
    }

}