





import java.util.List;
import java.util.ArrayList;

public class plsql_declaration_FunctionDeclaration extends declaration_Declaration, type_TypedElement {






    private List<Statement> statements;




    private ExceptionSection exceptionsection;




    private List<Declaration> declarations;


    public plsql_declaration_FunctionDeclaration(
    ) {
        super(
        );
        this.statements = new ArrayList<>();
        this.declarations = new ArrayList<>();
    }

    public plsql_declaration_FunctionDeclaration(
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
    public ExceptionSection getExceptionsection() {
        return exceptionsection;
    }

    public void setExceptionsection(ExceptionSection exceptionsection) {
        this.exceptionsection = exceptionsection;
    }
    public List<Declaration> getDeclarations() {
        return declarations;
    }

    public void addDeclaration(Declaration declaration) {
        this.declarations.add(declaration);
    }

}