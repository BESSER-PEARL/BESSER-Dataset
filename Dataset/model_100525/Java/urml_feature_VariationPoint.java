





import java.util.List;
import java.util.ArrayList;

public class urml_feature_VariationPoint extends AbstractFeature {

    private int multiplicity;



    public urml_feature_VariationPoint(
        int multiplicity    ) {
        super(
        );
        this.multiplicity = multiplicity;
    }


    public int getMultiplicity() {
        return multiplicity;
    }

    public void setMultiplicity(int multiplicity) {
        this.multiplicity = multiplicity;
    }


}