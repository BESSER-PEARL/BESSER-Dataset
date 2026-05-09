





import java.util.List;
import java.util.ArrayList;

public class basecs_ConstraintCS extends NamedElementCS {

    private String stereotype;





    private basecs_ClassifierCS basecs_classifiercs;


    public basecs_ConstraintCS(
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

    public basecs_ClassifierCS getBasecs_classifiercs() {
        return basecs_classifiercs;
    }

    public void setBasecs_classifiercs(basecs_ClassifierCS basecs_classifiercs) {
        this.basecs_classifiercs = basecs_classifiercs;
    }

}