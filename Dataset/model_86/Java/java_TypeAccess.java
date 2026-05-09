





import java.util.List;
import java.util.ArrayList;

public class java_TypeAccess extends Expression, NamespaceAccess {






    private java_InstanceofExpression java_instanceofexpression;




    private java_AbstractMethodDeclaration java_abstractmethoddeclaration;




    private java_TypeLiteral java_typeliteral;




    private java_AbstractTypeQualifiedExpression java_abstracttypequalifiedexpression;


    public java_TypeAccess(
    ) {
        super(
        );
    }



    public java_InstanceofExpression getJava_instanceofexpression() {
        return java_instanceofexpression;
    }

    public void setJava_instanceofexpression(java_InstanceofExpression java_instanceofexpression) {
        this.java_instanceofexpression = java_instanceofexpression;
    }
    public java_AbstractMethodDeclaration getJava_abstractmethoddeclaration() {
        return java_abstractmethoddeclaration;
    }

    public void setJava_abstractmethoddeclaration(java_AbstractMethodDeclaration java_abstractmethoddeclaration) {
        this.java_abstractmethoddeclaration = java_abstractmethoddeclaration;
    }
    public java_TypeLiteral getJava_typeliteral() {
        return java_typeliteral;
    }

    public void setJava_typeliteral(java_TypeLiteral java_typeliteral) {
        this.java_typeliteral = java_typeliteral;
    }
    public java_AbstractTypeQualifiedExpression getJava_abstracttypequalifiedexpression() {
        return java_abstracttypequalifiedexpression;
    }

    public void setJava_abstracttypequalifiedexpression(java_AbstractTypeQualifiedExpression java_abstracttypequalifiedexpression) {
        this.java_abstracttypequalifiedexpression = java_abstracttypequalifiedexpression;
    }

}