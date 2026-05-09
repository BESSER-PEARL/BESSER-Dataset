





import java.util.List;
import java.util.ArrayList;

public class ccsl_filters_BlockLastStatementFilter extends AtomicFilter {






    private statements_Statement statements_statement;




    private Context context;


    public ccsl_filters_BlockLastStatementFilter(
    ) {
        super(
        );
    }



    public statements_Statement getStatements_statement() {
        return statements_statement;
    }

    public void setStatements_statement(statements_Statement statements_statement) {
        this.statements_statement = statements_statement;
    }
    public Context getContext() {
        return context;
    }

    public void setContext(Context context) {
        this.context = context;
    }

}