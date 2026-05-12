





import java.util.List;
import java.util.ArrayList;

public class jDOQL_HavingClause  {






    private jDOQL_Expression jdoql_expression;




    private jDOQL_GroupByClause jdoql_groupbyclause;


    public jDOQL_HavingClause(
    ) {
    }



    public jDOQL_Expression getJdoql_expression() {
        return jdoql_expression;
    }

    public void setJdoql_expression(jDOQL_Expression jdoql_expression) {
        this.jdoql_expression = jdoql_expression;
    }
    public jDOQL_GroupByClause getJdoql_groupbyclause() {
        return jdoql_groupbyclause;
    }

    public void setJdoql_groupbyclause(jDOQL_GroupByClause jdoql_groupbyclause) {
        this.jdoql_groupbyclause = jdoql_groupbyclause;
    }

}