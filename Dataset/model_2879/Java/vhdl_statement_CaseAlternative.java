





import java.util.List;
import java.util.ArrayList;

public class vhdl_statement_CaseAlternative extends VhdlObject {






    private List<Statement> statements;


    public vhdl_statement_CaseAlternative(
    ) {
        super(
        );
        this.statements = new ArrayList<>();
    }

    public vhdl_statement_CaseAlternative(
        ArrayList<Statement> statements    ) {
        this.statements = statements;
    }


    public List<Statement> getStatements() {
        return statements;
    }

    public void addStatement(Statement statement) {
        this.statements.add(statement);
    }

}