





import java.util.List;
import java.util.ArrayList;

public class jDOQL_VariableDeclaration  {

    private String type;
    private String variableName;





    private jDOQL_VariablesClause jdoql_variablesclause;


    public jDOQL_VariableDeclaration(
        String type,        String variableName    ) {
        this.type = type;
        this.variableName = variableName;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getVariablename() {
        return variableName;
    }

    public void setVariablename(String variableName) {
        this.variableName = variableName;
    }

    public jDOQL_VariablesClause getJdoql_variablesclause() {
        return jdoql_variablesclause;
    }

    public void setJdoql_variablesclause(jDOQL_VariablesClause jdoql_variablesclause) {
        this.jdoql_variablesclause = jdoql_variablesclause;
    }

}