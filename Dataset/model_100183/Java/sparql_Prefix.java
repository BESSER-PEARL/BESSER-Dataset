





import java.util.List;
import java.util.ArrayList;

public class sparql_Prefix  {

    private String iref;
    private String name;





    private sparql_SPARQLQuery sparql_sparqlquery;


    public sparql_Prefix(
        String iref,        String name    ) {
        this.iref = iref;
        this.name = name;
    }


    public String getIref() {
        return iref;
    }

    public void setIref(String iref) {
        this.iref = iref;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public sparql_SPARQLQuery getSparql_sparqlquery() {
        return sparql_sparqlquery;
    }

    public void setSparql_sparqlquery(sparql_SPARQLQuery sparql_sparqlquery) {
        this.sparql_sparqlquery = sparql_sparqlquery;
    }

}