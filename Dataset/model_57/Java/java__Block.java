





import java.util.List;
import java.util.ArrayList;

public class java__Block extends Statement {






    private java__AbstractMethodDeclaration java__abstractmethoddeclaration;




    private List<java__Statement> java__statements;




    private java__Initializer java__initializer;


    public java__Block(
    ) {
        super(
        );
        this.java__statements = new ArrayList<>();
    }

    public java__Block(
        ArrayList<java__Statement> java__statements    ) {
        this.java__statements = java__statements;
    }


    public java__AbstractMethodDeclaration getJava__abstractmethoddeclaration() {
        return java__abstractmethoddeclaration;
    }

    public void setJava__abstractmethoddeclaration(java__AbstractMethodDeclaration java__abstractmethoddeclaration) {
        this.java__abstractmethoddeclaration = java__abstractmethoddeclaration;
    }
    public List<java__Statement> getJava__statements() {
        return java__statements;
    }

    public void addJava__statement(Java__statement java__statement) {
        this.java__statements.add(java__statement);
    }
    public java__Initializer getJava__initializer() {
        return java__initializer;
    }

    public void setJava__initializer(java__Initializer java__initializer) {
        this.java__initializer = java__initializer;
    }

}