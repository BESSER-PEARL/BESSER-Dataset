





import java.util.List;
import java.util.ArrayList;

public class jpql_InSeqExpression extends InExpression {






    private List<jpql_Variable> jpql_variables;


    public jpql_InSeqExpression(
    ) {
        super(
        );
        this.jpql_variables = new ArrayList<>();
    }

    public jpql_InSeqExpression(
        ArrayList<jpql_Variable> jpql_variables    ) {
        this.jpql_variables = jpql_variables;
    }


    public List<jpql_Variable> getJpql_variables() {
        return jpql_variables;
    }

    public void addJpql_variable(Jpql_variable jpql_variable) {
        this.jpql_variables.add(jpql_variable);
    }

}