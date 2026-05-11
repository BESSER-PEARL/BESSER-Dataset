





import java.util.List;
import java.util.ArrayList;

public class frontend_chain_ChainTransformation extends TransformationDefinition {






    private List<CompositeTransformation> compositetransformations;


    public frontend_chain_ChainTransformation(
    ) {
        super(
        );
        this.compositetransformations = new ArrayList<>();
    }

    public frontend_chain_ChainTransformation(
        ArrayList<CompositeTransformation> compositetransformations    ) {
        this.compositetransformations = compositetransformations;
    }


    public List<CompositeTransformation> getCompositetransformations() {
        return compositetransformations;
    }

    public void addCompositetransformation(Compositetransformation compositetransformation) {
        this.compositetransformations.add(compositetransformation);
    }

}