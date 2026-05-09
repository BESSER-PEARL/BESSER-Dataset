





import java.util.List;
import java.util.ArrayList;

public class c_sharp_statements_SwitchSection  {






    private List<Statement> statements;


    public c_sharp_statements_SwitchSection(
    ) {
        this.statements = new ArrayList<>();
    }

    public c_sharp_statements_SwitchSection(
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