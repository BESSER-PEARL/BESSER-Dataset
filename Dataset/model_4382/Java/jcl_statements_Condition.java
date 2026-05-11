





import java.util.List;
import java.util.ArrayList;

public class jcl_statements_Condition extends statements_Statement, statements_StatementContainer {

    private String endName;
    private String elseName;





    private List<Statement> statements;


    public jcl_statements_Condition(
        String endName,        String elseName    ) {
        super(
        );
        this.endName = endName;
        this.elseName = elseName;
        this.statements = new ArrayList<>();
    }

    public jcl_statements_Condition(
        String endName,        String elseName        ArrayList<Statement> statements    ) {
        this.endName = endName;
        this.elseName = elseName;
        this.statements = statements;
    }

    public String getEndname() {
        return endName;
    }

    public void setEndname(String endName) {
        this.endName = endName;
    }
    public String getElsename() {
        return elseName;
    }

    public void setElsename(String elseName) {
        this.elseName = elseName;
    }

    public List<Statement> getStatements() {
        return statements;
    }

    public void addStatement(Statement statement) {
        this.statements.add(statement);
    }

}