





import java.util.List;
import java.util.ArrayList;

public class sparqlas_DisjointClasses extends ClassAtom {






    private List<sparqlas_ClassExpression> sparqlas_classexpressions;


    public sparqlas_DisjointClasses(
    ) {
        super(
        );
        this.sparqlas_classexpressions = new ArrayList<>();
    }

    public sparqlas_DisjointClasses(
        ArrayList<sparqlas_ClassExpression> sparqlas_classexpressions    ) {
        this.sparqlas_classexpressions = sparqlas_classexpressions;
    }


    public List<sparqlas_ClassExpression> getSparqlas_classexpressions() {
        return sparqlas_classexpressions;
    }

    public void addSparqlas_classexpression(Sparqlas_classexpression sparqlas_classexpression) {
        this.sparqlas_classexpressions.add(sparqlas_classexpression);
    }

}