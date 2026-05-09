





import java.util.List;
import java.util.ArrayList;

public class astm_ArrayType extends ConstructedType {






    private List<astm_Dimension> astm_dimensions;


    public astm_ArrayType(
    ) {
        super(
        );
        this.astm_dimensions = new ArrayList<>();
    }

    public astm_ArrayType(
        ArrayList<astm_Dimension> astm_dimensions    ) {
        this.astm_dimensions = astm_dimensions;
    }


    public List<astm_Dimension> getAstm_dimensions() {
        return astm_dimensions;
    }

    public void addAstm_dimension(Astm_dimension astm_dimension) {
        this.astm_dimensions.add(astm_dimension);
    }

}