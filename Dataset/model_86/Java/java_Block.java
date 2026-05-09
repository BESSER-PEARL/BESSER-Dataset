





import java.util.List;
import java.util.ArrayList;

public class java_Block extends Statement {






    private java_AbstractMethodDeclaration java_abstractmethoddeclaration;




    private java_TryStatement java_trystatement;




    private java_TryStatement java_trystatement;




    private List<java_Statement> java_statements;


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
    public java_TryStatement getJava_trystatement() {
        return java_trystatement;
    }

    public void setJava_trystatement(java_TryStatement java_trystatement) {
        this.java_trystatement = java_trystatement;
    }
    public java_TryStatement getJava_trystatement() {
        return java_trystatement;
    }

    public void setJava_trystatement(java_TryStatement java_trystatement) {
        this.java_trystatement = java_trystatement;
    }
    public List<java_Statement> getJava_statements() {
        return java_statements;
    }

    public void addJava_statement(Java_statement java_statement) {
        this.java_statements.add(java_statement);
    }

}