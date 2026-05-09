





import java.util.List;
import java.util.ArrayList;

public class gastm_ArrayType extends ConstructedType {






    private List<Dimension> dimensions;


    public gastm_ArrayType(
    ) {
        super(
        );
        this.dimensions = new ArrayList<>();
    }

    public gastm_ArrayType(
        ArrayList<Dimension> dimensions    ) {
        this.dimensions = dimensions;
    }


    public List<Dimension> getDimensions() {
        return dimensions;
    }

    public void addDimension(Dimension dimension) {
        this.dimensions.add(dimension);
    }

}