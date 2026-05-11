





import java.util.List;
import java.util.ArrayList;

public class odemcustom_Clazz extends Classifier, ClassSimilar {

    private boolean active;





    private odemcustom_ClassAugment odemcustom_classaugment;




    private odemcustom_ClassSimilar odemcustom_classsimilar;




    private List<odemcustom_Expression> odemcustom_expressions;


    public odemcustom_Clazz(
        boolean active    ) {
        super(
        );
        this.active = active;
        this.odemcustom_expressions = new ArrayList<>();
    }

    public odemcustom_Clazz(
        boolean active        ArrayList<odemcustom_Expression> odemcustom_expressions    ) {
        this.active = active;
        this.odemcustom_expressions = odemcustom_expressions;
    }

    public boolean getActive() {
        return active;
    }

    public void setActive(boolean active) {
        this.active = active;
    }

    public odemcustom_ClassAugment getOdemcustom_classaugment() {
        return odemcustom_classaugment;
    }

    public void setOdemcustom_classaugment(odemcustom_ClassAugment odemcustom_classaugment) {
        this.odemcustom_classaugment = odemcustom_classaugment;
    }
    public odemcustom_ClassSimilar getOdemcustom_classsimilar() {
        return odemcustom_classsimilar;
    }

    public void setOdemcustom_classsimilar(odemcustom_ClassSimilar odemcustom_classsimilar) {
        this.odemcustom_classsimilar = odemcustom_classsimilar;
    }
    public List<odemcustom_Expression> getOdemcustom_expressions() {
        return odemcustom_expressions;
    }

    public void addOdemcustom_expression(Odemcustom_expression odemcustom_expression) {
        this.odemcustom_expressions.add(odemcustom_expression);
    }

}