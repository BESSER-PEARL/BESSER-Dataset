





import java.util.List;
import java.util.ArrayList;

public class RefinementsEcore_EAttribute extends EStructuralFeature {

    private int iD;





    private RefinementsEcore_EAttribute refinementsecore_eattribute;


    public RefinementsEcore_EAttribute(
        int iD    ) {
        super(
        );
        this.iD = iD;
    }


    public int getId() {
        return iD;
    }

    public void setId(int iD) {
        this.iD = iD;
    }

    public RefinementsEcore_EAttribute getRefinementsecore_eattribute() {
        return refinementsecore_eattribute;
    }

    public void setRefinementsecore_eattribute(RefinementsEcore_EAttribute refinementsecore_eattribute) {
        this.refinementsecore_eattribute = refinementsecore_eattribute;
    }

}