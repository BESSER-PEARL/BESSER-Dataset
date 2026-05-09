





import java.util.List;
import java.util.ArrayList;

public class Java_MethodRef extends ASTNode {






    private Java_AbstractMethodDeclaration java_abstractmethoddeclaration;




    private Java_AbstractMethodDeclaration java_abstractmethoddeclaration;




    private List<Java_MethodRefParameter> java_methodrefparameters;


    public Java_MethodRef(
    ) {
        super(
        );
        this.java_methodrefparameters = new ArrayList<>();
    }

    public Java_MethodRef(
        ArrayList<Java_MethodRefParameter> java_methodrefparameters    ) {
        this.java_methodrefparameters = java_methodrefparameters;
    }


    public Java_AbstractMethodDeclaration getJava_abstractmethoddeclaration() {
        return java_abstractmethoddeclaration;
    }

    public void setJava_abstractmethoddeclaration(Java_AbstractMethodDeclaration java_abstractmethoddeclaration) {
        this.java_abstractmethoddeclaration = java_abstractmethoddeclaration;
    }
    public Java_AbstractMethodDeclaration getJava_abstractmethoddeclaration() {
        return java_abstractmethoddeclaration;
    }

    public void setJava_abstractmethoddeclaration(Java_AbstractMethodDeclaration java_abstractmethoddeclaration) {
        this.java_abstractmethoddeclaration = java_abstractmethoddeclaration;
    }
    public List<Java_MethodRefParameter> getJava_methodrefparameters() {
        return java_methodrefparameters;
    }

    public void addJava_methodrefparameter(Java_methodrefparameter java_methodrefparameter) {
        this.java_methodrefparameters.add(java_methodrefparameter);
    }

}