





import java.util.List;
import java.util.ArrayList;

public class plsql_declaration_Package extends NamedElement {






    private List<Declaration> declarations;




    private List<Statement> statements;


    public plsql_declaration_Package(
    ) {
        super(
        );
        this.declarations = new ArrayList<>();
        this.statements = new ArrayList<>();
    }

    public plsql_declaration_Package(
        ArrayList<Declaration> declarations,        ArrayList<Statement> statements    ) {
        this.declarations = declarations;
        this.statements = statements;
    }


    public List<Declaration> getDeclarations() {
        return declarations;
    }

    public void addDeclaration(Declaration declaration) {
        this.declarations.add(declaration);
    }
    public List<Statement> getStatements() {
        return statements;
    }

    public void addStatement(Statement statement) {
        this.statements.add(statement);
    }

}