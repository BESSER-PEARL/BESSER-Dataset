





import java.util.List;
import java.util.ArrayList;

public class pascal_if_statement  {






    private pascal_conditional_statement pascal_conditional_statement;




    private pascal_expression pascal_expression;




    private List<pascal_statement> pascal_statements;


    public pascal_if_statement(
    ) {
        this.pascal_statements = new ArrayList<>();
    }

    public pascal_if_statement(
        ArrayList<pascal_statement> pascal_statements    ) {
        this.pascal_statements = pascal_statements;
    }


    public pascal_conditional_statement getPascal_conditional_statement() {
        return pascal_conditional_statement;
    }

    public void setPascal_conditional_statement(pascal_conditional_statement pascal_conditional_statement) {
        this.pascal_conditional_statement = pascal_conditional_statement;
    }
    public pascal_expression getPascal_expression() {
        return pascal_expression;
    }

    public void setPascal_expression(pascal_expression pascal_expression) {
        this.pascal_expression = pascal_expression;
    }
    public List<pascal_statement> getPascal_statements() {
        return pascal_statements;
    }

    public void addPascal_statement(Pascal_statement pascal_statement) {
        this.pascal_statements.add(pascal_statement);
    }

}