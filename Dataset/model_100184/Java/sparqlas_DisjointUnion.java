





import java.util.List;
import java.util.ArrayList;

public class sparqlas_DisjointUnion extends ClassAtom {






    private List<sparqlas_ClassExpression> sparqlas_classexpressions;




    private sparqlas_ClassVariable sparqlas_classvariable;




    private sparqlas_Class sparqlas_class;


    public sparqlas_DisjointUnion(
    ) {
        super(
        );
        this.sparqlas_classexpressions = new ArrayList<>();
    }

    public sparqlas_DisjointUnion(
        ArrayList<sparqlas_ClassExpression> sparqlas_classexpressions    ) {
        this.sparqlas_classexpressions = sparqlas_classexpressions;
    }


    public List<sparqlas_ClassExpression> getSparqlas_classexpressions() {
        return sparqlas_classexpressions;
    }

    public void addSparqlas_classexpression(Sparqlas_classexpression sparqlas_classexpression) {
        this.sparqlas_classexpressions.add(sparqlas_classexpression);
    }
    public sparqlas_ClassVariable getSparqlas_classvariable() {
        return sparqlas_classvariable;
    }

    public void setSparqlas_classvariable(sparqlas_ClassVariable sparqlas_classvariable) {
        this.sparqlas_classvariable = sparqlas_classvariable;
    }
    public sparqlas_Class getSparqlas_class() {
        return sparqlas_class;
    }

    public void setSparqlas_class(sparqlas_Class sparqlas_class) {
        this.sparqlas_class = sparqlas_class;
    }

}