





import java.util.List;
import java.util.ArrayList;

public class baseCST_ConstraintCS extends NamedElementCS {

    private String stereotype;





    private baseCST_ClassifierCS basecst_classifiercs;


    public baseCST_ConstraintCS(
        String stereotype    ) {
        super(
        );
        this.stereotype = stereotype;
    }


    public String getStereotype() {
        return stereotype;
    }

    public void setStereotype(String stereotype) {
        this.stereotype = stereotype;
    }

    public baseCST_ClassifierCS getBasecst_classifiercs() {
        return basecst_classifiercs;
    }

    public void setBasecst_classifiercs(baseCST_ClassifierCS basecst_classifiercs) {
        this.basecst_classifiercs = basecst_classifiercs;
    }

}