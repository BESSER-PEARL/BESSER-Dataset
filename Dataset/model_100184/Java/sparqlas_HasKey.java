





import java.util.List;
import java.util.ArrayList;

public class sparqlas_HasKey extends Atom {






    private List<sparqlas_ObjectPropertyExpression> sparqlas_objectpropertyexpressions;


    public sparqlas_HasKey(
    ) {
        super(
        );
        this.sparqlas_objectpropertyexpressions = new ArrayList<>();
    }

    public sparqlas_HasKey(
        ArrayList<sparqlas_ObjectPropertyExpression> sparqlas_objectpropertyexpressions    ) {
        this.sparqlas_objectpropertyexpressions = sparqlas_objectpropertyexpressions;
    }


    public List<sparqlas_ObjectPropertyExpression> getSparqlas_objectpropertyexpressions() {
        return sparqlas_objectpropertyexpressions;
    }

    public void addSparqlas_objectpropertyexpression(Sparqlas_objectpropertyexpression sparqlas_objectpropertyexpression) {
        this.sparqlas_objectpropertyexpressions.add(sparqlas_objectpropertyexpression);
    }

}