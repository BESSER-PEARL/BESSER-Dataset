





import java.util.List;
import java.util.ArrayList;

public class sparql_PNAME_NS extends PrefixedName, VarOrIRIref {

    private String pn_prefix;





    private sparql_PrefixDecl sparql_prefixdecl;


    public sparql_PNAME_NS(
        String pn_prefix    ) {
        super(
        );
        this.pn_prefix = pn_prefix;
    }


    public String getPn_prefix() {
        return pn_prefix;
    }

    public void setPn_prefix(String pn_prefix) {
        this.pn_prefix = pn_prefix;
    }

    public sparql_PrefixDecl getSparql_prefixdecl() {
        return sparql_prefixdecl;
    }

    public void setSparql_prefixdecl(sparql_PrefixDecl sparql_prefixdecl) {
        this.sparql_prefixdecl = sparql_prefixdecl;
    }

}