





import java.util.List;
import java.util.ArrayList;

public class sparql_DatasetClause  {






    private sparql_IRI sparql_iri;




    private sparql_SelectionQuery sparql_selectionquery;


    public sparql_DatasetClause(
    ) {
    }



    public sparql_IRI getSparql_iri() {
        return sparql_iri;
    }

    public void setSparql_iri(sparql_IRI sparql_iri) {
        this.sparql_iri = sparql_iri;
    }
    public sparql_SelectionQuery getSparql_selectionquery() {
        return sparql_selectionquery;
    }

    public void setSparql_selectionquery(sparql_SelectionQuery sparql_selectionquery) {
        this.sparql_selectionquery = sparql_selectionquery;
    }

}