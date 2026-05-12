





import java.util.List;
import java.util.ArrayList;

public class sparqlas_ObjectPropertyDomain extends ObjectPropertyAtom {






    private sparqlas_ObjectPropertyExpression sparqlas_objectpropertyexpression;




    private sparqlas_ClassExpression sparqlas_classexpression;


    public sparqlas_ObjectPropertyDomain(
    ) {
        super(
        );
    }



    public sparqlas_ObjectPropertyExpression getSparqlas_objectpropertyexpression() {
        return sparqlas_objectpropertyexpression;
    }

    public void setSparqlas_objectpropertyexpression(sparqlas_ObjectPropertyExpression sparqlas_objectpropertyexpression) {
        this.sparqlas_objectpropertyexpression = sparqlas_objectpropertyexpression;
    }
    public sparqlas_ClassExpression getSparqlas_classexpression() {
        return sparqlas_classexpression;
    }

    public void setSparqlas_classexpression(sparqlas_ClassExpression sparqlas_classexpression) {
        this.sparqlas_classexpression = sparqlas_classexpression;
    }

}