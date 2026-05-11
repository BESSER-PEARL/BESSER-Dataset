





import java.util.List;
import java.util.ArrayList;

public class leek_StatementBlock extends Statement {






    private leek_FunctionDeclaration leek_functiondeclaration;




    private List<leek_Statement> leek_statements;


    public leek_StatementBlock(
    ) {
        super(
        );
        this.leek_statements = new ArrayList<>();
    }

    public leek_StatementBlock(
        ArrayList<leek_Statement> leek_statements    ) {
        this.leek_statements = leek_statements;
    }


    public leek_FunctionDeclaration getLeek_functiondeclaration() {
        return leek_functiondeclaration;
    }

    public void setLeek_functiondeclaration(leek_FunctionDeclaration leek_functiondeclaration) {
        this.leek_functiondeclaration = leek_functiondeclaration;
    }
    public List<leek_Statement> getLeek_statements() {
        return leek_statements;
    }

    public void addLeek_statement(Leek_statement leek_statement) {
        this.leek_statements.add(leek_statement);
    }

}