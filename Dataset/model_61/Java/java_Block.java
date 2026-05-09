





import java.util.List;
import java.util.ArrayList;

public class java_Block extends Statement {






    private java_AbstractMethodDeclaration java_abstractmethoddeclaration;




    private List<java_Statement> java_statements;




    private java_Initializer java_initializer;


    public java_Block(
    ) {
        super(
        );
        this.java_statements = new ArrayList<>();
    }

    public java_Block(
        ArrayList<java_Statement> java_statements    ) {
        this.java_statements = java_statements;
    }


    public java_AbstractMethodDeclaration getJava_abstractmethoddeclaration() {
        return java_abstractmethoddeclaration;
    }

    public void setJava_abstractmethoddeclaration(java_AbstractMethodDeclaration java_abstractmethoddeclaration) {
        this.java_abstractmethoddeclaration = java_abstractmethoddeclaration;
    }
    public List<java_Statement> getJava_statements() {
        return java_statements;
    }

    public void addJava_statement(Java_statement java_statement) {
        this.java_statements.add(java_statement);
    }
    public java_Initializer getJava_initializer() {
        return java_initializer;
    }

    public void setJava_initializer(java_Initializer java_initializer) {
        this.java_initializer = java_initializer;
    }

}