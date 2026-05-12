





import java.util.List;
import java.util.ArrayList;

public class jDOQL_ParameterDeclaration  {

    private String declaredParameterName;
    private String type;





    private jDOQL_ParametersClause jdoql_parametersclause;


    public jDOQL_ParameterDeclaration(
        String declaredParameterName,        String type    ) {
        this.declaredParameterName = declaredParameterName;
        this.type = type;
    }


    public String getDeclaredparametername() {
        return declaredParameterName;
    }

    public void setDeclaredparametername(String declaredParameterName) {
        this.declaredParameterName = declaredParameterName;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public jDOQL_ParametersClause getJdoql_parametersclause() {
        return jdoql_parametersclause;
    }

    public void setJdoql_parametersclause(jDOQL_ParametersClause jdoql_parametersclause) {
        this.jdoql_parametersclause = jdoql_parametersclause;
    }

}