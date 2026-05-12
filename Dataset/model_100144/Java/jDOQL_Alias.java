





import java.util.List;
import java.util.ArrayList;

public class jDOQL_Alias  {

    private String identifier;





    private jDOQL_SubqueryFromClause jdoql_subqueryfromclause;


    public jDOQL_Alias(
        String identifier    ) {
        this.identifier = identifier;
    }


    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }

    public jDOQL_SubqueryFromClause getJdoql_subqueryfromclause() {
        return jdoql_subqueryfromclause;
    }

    public void setJdoql_subqueryfromclause(jDOQL_SubqueryFromClause jdoql_subqueryfromclause) {
        this.jdoql_subqueryfromclause = jdoql_subqueryfromclause;
    }

}