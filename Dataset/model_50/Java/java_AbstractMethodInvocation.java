





import java.util.List;
import java.util.ArrayList;

public class java_AbstractMethodInvocation extends ASTNode {






    private java_AbstractMethodDeclaration java_abstractmethoddeclaration;




    private java_AbstractMethodDeclaration java_abstractmethoddeclaration;




    private List<java_TypeAccess> java_typeaccesss;




    private List<java_Expression> java_expressions;


    public java_AbstractMethodInvocation(
    ) {
        super(
        );
        this.java_typeaccesss = new ArrayList<>();
        this.java_expressions = new ArrayList<>();
    }

    public java_AbstractMethodInvocation(
        ArrayList<java_TypeAccess> java_typeaccesss,        ArrayList<java_Expression> java_expressions    ) {
        this.java_typeaccesss = java_typeaccesss;
        this.java_expressions = java_expressions;
    }


    public java_AbstractMethodDeclaration getJava_abstractmethoddeclaration() {
        return java_abstractmethoddeclaration;
    }

    public void setJava_abstractmethoddeclaration(java_AbstractMethodDeclaration java_abstractmethoddeclaration) {
        this.java_abstractmethoddeclaration = java_abstractmethoddeclaration;
    }
    public java_AbstractMethodDeclaration getJava_abstractmethoddeclaration() {
        return java_abstractmethoddeclaration;
    }

    public void setJava_abstractmethoddeclaration(java_AbstractMethodDeclaration java_abstractmethoddeclaration) {
        this.java_abstractmethoddeclaration = java_abstractmethoddeclaration;
    }
    public List<java_TypeAccess> getJava_typeaccesss() {
        return java_typeaccesss;
    }

    public void addJava_typeaccess(Java_typeaccess java_typeaccess) {
        this.java_typeaccesss.add(java_typeaccess);
    }
    public List<java_Expression> getJava_expressions() {
        return java_expressions;
    }

    public void addJava_expression(Java_expression java_expression) {
        this.java_expressions.add(java_expression);
    }

}