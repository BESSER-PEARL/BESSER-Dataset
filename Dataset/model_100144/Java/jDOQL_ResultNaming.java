





import java.util.List;
import java.util.ArrayList;

public class jDOQL_ResultNaming  {

    private String identifier;





    private jDOQL_Expression jdoql_expression;


    public jDOQL_ResultNaming(
        String identifier    ) {
        this.identifier = identifier;
    }


    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }

    public jDOQL_Expression getJdoql_expression() {
        return jdoql_expression;
    }

    public void setJdoql_expression(jDOQL_Expression jdoql_expression) {
        this.jdoql_expression = jdoql_expression;
    }

}