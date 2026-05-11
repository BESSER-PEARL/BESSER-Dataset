





import java.util.List;
import java.util.ArrayList;

public class kernel_statements_Condition extends statements_Conditional, statements_StatementContainer, statements_Statement {






    private Statement statement;


    public kernel_statements_Condition(
    ) {
        super(
        );
    }



    public Statement getStatement() {
        return statement;
    }

    public void setStatement(Statement statement) {
        this.statement = statement;
    }

}