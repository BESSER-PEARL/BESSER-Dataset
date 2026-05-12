





import java.util.List;
import java.util.ArrayList;

public class sparql_IRI_REF extends IRIreference, VarOrIRIref {

    private String iri_ref;





    private sparql_BaseDecl sparql_basedecl;




    private sparql_PrefixDecl sparql_prefixdecl;


    public sparql_IRI_REF(
        String iri_ref    ) {
        super(
        );
        this.iri_ref = iri_ref;
    }


    public String getIri_ref() {
        return iri_ref;
    }

    public void setIri_ref(String iri_ref) {
        this.iri_ref = iri_ref;
    }

    public sparql_BaseDecl getSparql_basedecl() {
        return sparql_basedecl;
    }

    public void setSparql_basedecl(sparql_BaseDecl sparql_basedecl) {
        this.sparql_basedecl = sparql_basedecl;
    }
    public sparql_PrefixDecl getSparql_prefixdecl() {
        return sparql_prefixdecl;
    }

    public void setSparql_prefixdecl(sparql_PrefixDecl sparql_prefixdecl) {
        this.sparql_prefixdecl = sparql_prefixdecl;
    }

}