





import java.util.List;
import java.util.ArrayList;

public class vhdl_declaration_SubprogramBody extends VhdlObject {






    private List<Statement> statements;


    public vhdl_declaration_SubprogramBody(
    ) {
        super(
        );
        this.statements = new ArrayList<>();
    }

    public vhdl_declaration_SubprogramBody(
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