





import java.util.List;
import java.util.ArrayList;

public class jPQL_InSeqExpression extends InExpression {






    private List<jPQL_Variable> jpql_variables;


    public jPQL_InSeqExpression(
    ) {
        super(
        );
        this.jpql_variables = new ArrayList<>();
    }

    public jPQL_InSeqExpression(
        ArrayList<jPQL_Variable> jpql_variables    ) {
        this.jpql_variables = jpql_variables;
    }


    public List<jPQL_Variable> getJpql_variables() {
        return jpql_variables;
    }

    public void addJpql_variable(Jpql_variable jpql_variable) {
        this.jpql_variables.add(jpql_variable);
    }

}