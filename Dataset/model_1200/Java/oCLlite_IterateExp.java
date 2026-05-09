





import java.util.List;
import java.util.ArrayList;

public class oCLlite_IterateExp extends OclLExpression {






    private List<oCLlite_Iterator> ocllite_iterators;




    private oCLlite_LocalVariable ocllite_localvariable;




    private oCLlite_OclLExpression ocllite_ocllexpression;


    public oCLlite_IterateExp(
    ) {
        super(
        );
        this.ocllite_iterators = new ArrayList<>();
    }

    public oCLlite_IterateExp(
        ArrayList<oCLlite_Iterator> ocllite_iterators    ) {
        this.ocllite_iterators = ocllite_iterators;
    }


    public List<oCLlite_Iterator> getOcllite_iterators() {
        return ocllite_iterators;
    }

    public void addOcllite_iterator(Ocllite_iterator ocllite_iterator) {
        this.ocllite_iterators.add(ocllite_iterator);
    }
    public oCLlite_LocalVariable getOcllite_localvariable() {
        return ocllite_localvariable;
    }

    public void setOcllite_localvariable(oCLlite_LocalVariable ocllite_localvariable) {
        this.ocllite_localvariable = ocllite_localvariable;
    }
    public oCLlite_OclLExpression getOcllite_ocllexpression() {
        return ocllite_ocllexpression;
    }

    public void setOcllite_ocllexpression(oCLlite_OclLExpression ocllite_ocllexpression) {
        this.ocllite_ocllexpression = ocllite_ocllexpression;
    }

}