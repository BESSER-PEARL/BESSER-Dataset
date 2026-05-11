





import java.util.List;
import java.util.ArrayList;

public class miniJava_MethodDeclaration  {






    private List<miniJava_VariableDeclaration> minijava_variabledeclarations;




    private List<miniJava_Statement> minijava_statements;




    private miniJava_Class minijava_class;




    private List<miniJava_VariableDeclaration> minijava_variabledeclarations;




    private miniJava_Identifier minijava_identifier;


    public miniJava_MethodDeclaration(
    ) {
        this.minijava_variabledeclarations = new ArrayList<>();
        this.minijava_statements = new ArrayList<>();
        this.minijava_variabledeclarations = new ArrayList<>();
    }

    public miniJava_MethodDeclaration(
        ArrayList<miniJava_VariableDeclaration> minijava_variabledeclarations,        ArrayList<miniJava_Statement> minijava_statements,        ArrayList<miniJava_VariableDeclaration> minijava_variabledeclarations    ) {
        this.minijava_variabledeclarations = minijava_variabledeclarations;
        this.minijava_statements = minijava_statements;
        this.minijava_variabledeclarations = minijava_variabledeclarations;
    }


    public List<miniJava_VariableDeclaration> getMinijava_variabledeclarations() {
        return minijava_variabledeclarations;
    }

    public void addMinijava_variabledeclaration(Minijava_variabledeclaration minijava_variabledeclaration) {
        this.minijava_variabledeclarations.add(minijava_variabledeclaration);
    }
    public List<miniJava_Statement> getMinijava_statements() {
        return minijava_statements;
    }

    public void addMinijava_statement(Minijava_statement minijava_statement) {
        this.minijava_statements.add(minijava_statement);
    }
    public miniJava_Class getMinijava_class() {
        return minijava_class;
    }

    public void setMinijava_class(miniJava_Class minijava_class) {
        this.minijava_class = minijava_class;
    }
    public List<miniJava_VariableDeclaration> getMinijava_variabledeclarations() {
        return minijava_variabledeclarations;
    }

    public void addMinijava_variabledeclaration(Minijava_variabledeclaration minijava_variabledeclaration) {
        this.minijava_variabledeclarations.add(minijava_variabledeclaration);
    }
    public miniJava_Identifier getMinijava_identifier() {
        return minijava_identifier;
    }

    public void setMinijava_identifier(miniJava_Identifier minijava_identifier) {
        this.minijava_identifier = minijava_identifier;
    }

}