





import java.util.List;
import java.util.ArrayList;

public class sparqlas_DataPropertyDomain extends DataPropertyAtom {






    private sparqlas_DataPropertyExpression sparqlas_datapropertyexpression;




    private sparqlas_ClassExpression sparqlas_classexpression;


    public sparqlas_DataPropertyDomain(
    ) {
        super(
        );
    }



    public sparqlas_DataPropertyExpression getSparqlas_datapropertyexpression() {
        return sparqlas_datapropertyexpression;
    }

    public void setSparqlas_datapropertyexpression(sparqlas_DataPropertyExpression sparqlas_datapropertyexpression) {
        this.sparqlas_datapropertyexpression = sparqlas_datapropertyexpression;
    }
    public sparqlas_ClassExpression getSparqlas_classexpression() {
        return sparqlas_classexpression;
    }

    public void setSparqlas_classexpression(sparqlas_ClassExpression sparqlas_classexpression) {
        this.sparqlas_classexpression = sparqlas_classexpression;
    }

}