





import java.util.List;
import java.util.ArrayList;

public class sparqlas_ObjectPropertyChain  {






    private List<sparqlas_ObjectPropertyExpression> sparqlas_objectpropertyexpressions;




    private sparqlas_SubObjectPropertyOf sparqlas_subobjectpropertyof;


    public sparqlas_ObjectPropertyChain(
    ) {
        this.sparqlas_objectpropertyexpressions = new ArrayList<>();
    }

    public sparqlas_ObjectPropertyChain(
        ArrayList<sparqlas_ObjectPropertyExpression> sparqlas_objectpropertyexpressions    ) {
        this.sparqlas_objectpropertyexpressions = sparqlas_objectpropertyexpressions;
    }


    public List<sparqlas_ObjectPropertyExpression> getSparqlas_objectpropertyexpressions() {
        return sparqlas_objectpropertyexpressions;
    }

    public void addSparqlas_objectpropertyexpression(Sparqlas_objectpropertyexpression sparqlas_objectpropertyexpression) {
        this.sparqlas_objectpropertyexpressions.add(sparqlas_objectpropertyexpression);
    }
    public sparqlas_SubObjectPropertyOf getSparqlas_subobjectpropertyof() {
        return sparqlas_subobjectpropertyof;
    }

    public void setSparqlas_subobjectpropertyof(sparqlas_SubObjectPropertyOf sparqlas_subobjectpropertyof) {
        this.sparqlas_subobjectpropertyof = sparqlas_subobjectpropertyof;
    }

}