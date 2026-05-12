





import java.util.List;
import java.util.ArrayList;

public class sparqlas_DisjointDataProperties extends DataPropertyAtom {






    private List<sparqlas_DataPropertyExpression> sparqlas_datapropertyexpressions;


    public sparqlas_DisjointDataProperties(
    ) {
        super(
        );
        this.sparqlas_datapropertyexpressions = new ArrayList<>();
    }

    public sparqlas_DisjointDataProperties(
        ArrayList<sparqlas_DataPropertyExpression> sparqlas_datapropertyexpressions    ) {
        this.sparqlas_datapropertyexpressions = sparqlas_datapropertyexpressions;
    }


    public List<sparqlas_DataPropertyExpression> getSparqlas_datapropertyexpressions() {
        return sparqlas_datapropertyexpressions;
    }

    public void addSparqlas_datapropertyexpression(Sparqlas_datapropertyexpression sparqlas_datapropertyexpression) {
        this.sparqlas_datapropertyexpressions.add(sparqlas_datapropertyexpression);
    }

}