





import java.util.List;
import java.util.ArrayList;

public class sparqlas_OntologyDocument  {






    private sparqlas_Query sparqlas_query;




    private List<sparqlas_PrefixDefinition> sparqlas_prefixdefinitions;


    public sparqlas_OntologyDocument(
    ) {
        this.sparqlas_prefixdefinitions = new ArrayList<>();
    }

    public sparqlas_OntologyDocument(
        ArrayList<sparqlas_PrefixDefinition> sparqlas_prefixdefinitions    ) {
        this.sparqlas_prefixdefinitions = sparqlas_prefixdefinitions;
    }


    public sparqlas_Query getSparqlas_query() {
        return sparqlas_query;
    }

    public void setSparqlas_query(sparqlas_Query sparqlas_query) {
        this.sparqlas_query = sparqlas_query;
    }
    public List<sparqlas_PrefixDefinition> getSparqlas_prefixdefinitions() {
        return sparqlas_prefixdefinitions;
    }

    public void addSparqlas_prefixdefinition(Sparqlas_prefixdefinition sparqlas_prefixdefinition) {
        this.sparqlas_prefixdefinitions.add(sparqlas_prefixdefinition);
    }

}