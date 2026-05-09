





import java.util.List;
import java.util.ArrayList;

public class gastm_ArrayType extends ConstructedType {






    private List<gastm_Dimension> gastm_dimensions;


    public gastm_ArrayType(
    ) {
        super(
        );
        this.gastm_dimensions = new ArrayList<>();
    }

    public gastm_ArrayType(
        ArrayList<gastm_Dimension> gastm_dimensions    ) {
        this.gastm_dimensions = gastm_dimensions;
    }


    public List<gastm_Dimension> getGastm_dimensions() {
        return gastm_dimensions;
    }

    public void addGastm_dimension(Gastm_dimension gastm_dimension) {
        this.gastm_dimensions.add(gastm_dimension);
    }

}