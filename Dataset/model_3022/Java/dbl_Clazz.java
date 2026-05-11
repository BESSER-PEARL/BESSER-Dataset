





import java.util.List;
import java.util.ArrayList;

public class dbl_Clazz extends Classifier, ClassSimilar {

    private boolean active;





    private dbl_ClassAugment dbl_classaugment;




    private dbl_ClassSimilar dbl_classsimilar;




    private List<dbl_Expression> dbl_expressions;


    public dbl_Clazz(
        boolean active    ) {
        super(
        );
        this.active = active;
        this.dbl_expressions = new ArrayList<>();
    }

    public dbl_Clazz(
        boolean active        ArrayList<dbl_Expression> dbl_expressions    ) {
        this.active = active;
        this.dbl_expressions = dbl_expressions;
    }

    public boolean getActive() {
        return active;
    }

    public void setActive(boolean active) {
        this.active = active;
    }

    public dbl_ClassAugment getDbl_classaugment() {
        return dbl_classaugment;
    }

    public void setDbl_classaugment(dbl_ClassAugment dbl_classaugment) {
        this.dbl_classaugment = dbl_classaugment;
    }
    public dbl_ClassSimilar getDbl_classsimilar() {
        return dbl_classsimilar;
    }

    public void setDbl_classsimilar(dbl_ClassSimilar dbl_classsimilar) {
        this.dbl_classsimilar = dbl_classsimilar;
    }
    public List<dbl_Expression> getDbl_expressions() {
        return dbl_expressions;
    }

    public void addDbl_expression(Dbl_expression dbl_expression) {
        this.dbl_expressions.add(dbl_expression);
    }

}