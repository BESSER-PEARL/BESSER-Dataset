





import java.util.List;
import java.util.ArrayList;

public class miniJava_BlockStatement extends Statement {






    private List<miniJava_Statement> minijava_statements;


    public miniJava_BlockStatement(
    ) {
        super(
        );
        this.minijava_statements = new ArrayList<>();
    }

    public miniJava_BlockStatement(
        ArrayList<miniJava_Statement> minijava_statements    ) {
        this.minijava_statements = minijava_statements;
    }


    public List<miniJava_Statement> getMinijava_statements() {
        return minijava_statements;
    }

    public void addMinijava_statement(Minijava_statement minijava_statement) {
        this.minijava_statements.add(minijava_statement);
    }

}