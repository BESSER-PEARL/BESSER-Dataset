





import java.util.List;
import java.util.ArrayList;

public class sparql_GroupGraphPattern extends LocatedElement {






    private sparql_WhereClause sparql_whereclause;




    private List<sparql_AdditionalGGPElement> sparql_additionalggpelements;


    public sparql_GroupGraphPattern(
    ) {
        super(
        );
        this.sparql_additionalggpelements = new ArrayList<>();
    }

    public sparql_GroupGraphPattern(
        ArrayList<sparql_AdditionalGGPElement> sparql_additionalggpelements    ) {
        this.sparql_additionalggpelements = sparql_additionalggpelements;
    }


    public sparql_WhereClause getSparql_whereclause() {
        return sparql_whereclause;
    }

    public void setSparql_whereclause(sparql_WhereClause sparql_whereclause) {
        this.sparql_whereclause = sparql_whereclause;
    }
    public List<sparql_AdditionalGGPElement> getSparql_additionalggpelements() {
        return sparql_additionalggpelements;
    }

    public void addSparql_additionalggpelement(Sparql_additionalggpelement sparql_additionalggpelement) {
        this.sparql_additionalggpelements.add(sparql_additionalggpelement);
    }

}