





import java.util.List;
import java.util.ArrayList;

public class plsql_declaration_Package extends NamedElement {






    private List<Statement> statements;




    private List<Declaration> declarations;


    public plsql_declaration_Package(
    ) {
        super(
        );
        this.statements = new ArrayList<>();
        this.declarations = new ArrayList<>();
    }

    public plsql_declaration_Package(
        ArrayList<Statement> statements,        ArrayList<Declaration> declarations    ) {
        this.statements = statements;
        this.declarations = declarations;
    }


    public List<Statement> getStatements() {
        return statements;
    }

    public void addStatement(Statement statement) {
        this.statements.add(statement);
    }
    public List<Declaration> getDeclarations() {
        return declarations;
    }

    public void addDeclaration(Declaration declaration) {
        this.declarations.add(declaration);
    }

}