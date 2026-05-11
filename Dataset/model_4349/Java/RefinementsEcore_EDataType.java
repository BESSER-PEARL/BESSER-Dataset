





import java.util.List;
import java.util.ArrayList;

public class RefinementsEcore_EDataType extends EClassifier {

    private boolean serializable;





    private RefinementsEcore_EAttribute refinementsecore_eattribute;


    public RefinementsEcore_EDataType(
        boolean serializable    ) {
        super(
        );
        this.serializable = serializable;
    }


    public boolean getSerializable() {
        return serializable;
    }

    public void setSerializable(boolean serializable) {
        this.serializable = serializable;
    }

    public RefinementsEcore_EAttribute getRefinementsecore_eattribute() {
        return refinementsecore_eattribute;
    }

    public void setRefinementsecore_eattribute(RefinementsEcore_EAttribute refinementsecore_eattribute) {
        this.refinementsecore_eattribute = refinementsecore_eattribute;
    }

}