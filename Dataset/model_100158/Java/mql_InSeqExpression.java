





import java.util.List;
import java.util.ArrayList;

public class mql_InSeqExpression extends InExpression {






    private List<mql_Variable> mql_variables;


    public mql_InSeqExpression(
    ) {
        super(
        );
        this.mql_variables = new ArrayList<>();
    }

    public mql_InSeqExpression(
        ArrayList<mql_Variable> mql_variables    ) {
        this.mql_variables = mql_variables;
    }


    public List<mql_Variable> getMql_variables() {
        return mql_variables;
    }

    public void addMql_variable(Mql_variable mql_variable) {
        this.mql_variables.add(mql_variable);
    }

}