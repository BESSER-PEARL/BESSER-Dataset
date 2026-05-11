





import java.util.List;
import java.util.ArrayList;

public class dbl_Clazz extends Classifier, ClassSimilar {

    private boolean active;





    private dbl_ClassSimilar dbl_classsimilar;




    private dbl_ClassAugment dbl_classaugment;


    public dbl_Clazz(
        boolean active    ) {
        super(
        );
        this.active = active;
    }


    public boolean getActive() {
        return active;
    }

    public void setActive(boolean active) {
        this.active = active;
    }

    public dbl_ClassSimilar getDbl_classsimilar() {
        return dbl_classsimilar;
    }

    public void setDbl_classsimilar(dbl_ClassSimilar dbl_classsimilar) {
        this.dbl_classsimilar = dbl_classsimilar;
    }
    public dbl_ClassAugment getDbl_classaugment() {
        return dbl_classaugment;
    }

    public void setDbl_classaugment(dbl_ClassAugment dbl_classaugment) {
        this.dbl_classaugment = dbl_classaugment;
    }

}