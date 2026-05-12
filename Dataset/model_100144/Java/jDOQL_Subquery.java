





import java.util.List;
import java.util.ArrayList;

public class jDOQL_Subquery extends Expression {






    private jDOQL_VariablesClause jdoql_variablesclause;




    private jDOQL_WhereClause jdoql_whereclause;




    private jDOQL_ImportClause jdoql_importclause;




    private jDOQL_SubqueryFromClause jdoql_subqueryfromclause;




    private jDOQL_ParametersClause jdoql_parametersclause;


    public jDOQL_Subquery(
    ) {
        super(
        );
    }



    public jDOQL_VariablesClause getJdoql_variablesclause() {
        return jdoql_variablesclause;
    }

    public void setJdoql_variablesclause(jDOQL_VariablesClause jdoql_variablesclause) {
        this.jdoql_variablesclause = jdoql_variablesclause;
    }
    public jDOQL_WhereClause getJdoql_whereclause() {
        return jdoql_whereclause;
    }

    public void setJdoql_whereclause(jDOQL_WhereClause jdoql_whereclause) {
        this.jdoql_whereclause = jdoql_whereclause;
    }
    public jDOQL_ImportClause getJdoql_importclause() {
        return jdoql_importclause;
    }

    public void setJdoql_importclause(jDOQL_ImportClause jdoql_importclause) {
        this.jdoql_importclause = jdoql_importclause;
    }
    public jDOQL_SubqueryFromClause getJdoql_subqueryfromclause() {
        return jdoql_subqueryfromclause;
    }

    public void setJdoql_subqueryfromclause(jDOQL_SubqueryFromClause jdoql_subqueryfromclause) {
        this.jdoql_subqueryfromclause = jdoql_subqueryfromclause;
    }
    public jDOQL_ParametersClause getJdoql_parametersclause() {
        return jdoql_parametersclause;
    }

    public void setJdoql_parametersclause(jDOQL_ParametersClause jdoql_parametersclause) {
        this.jdoql_parametersclause = jdoql_parametersclause;
    }

}