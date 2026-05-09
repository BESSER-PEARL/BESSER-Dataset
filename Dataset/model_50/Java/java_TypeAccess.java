





import java.util.List;
import java.util.ArrayList;

public class java_TypeAccess extends NamespaceAccess, Expression {






    private java_WildCardType java_wildcardtype;




    private java_AnnotationTypeMemberDeclaration java_annotationtypememberdeclaration;




    private java_TypeLiteral java_typeliteral;




    private java_SingleVariableDeclaration java_singlevariabledeclaration;




    private java_AbstractTypeDeclaration java_abstracttypedeclaration;




    private java_AbstractMethodDeclaration java_abstractmethoddeclaration;


    public java_TypeAccess(
    ) {
        super(
        );
    }



    public java_WildCardType getJava_wildcardtype() {
        return java_wildcardtype;
    }

    public void setJava_wildcardtype(java_WildCardType java_wildcardtype) {
        this.java_wildcardtype = java_wildcardtype;
    }
    public java_AnnotationTypeMemberDeclaration getJava_annotationtypememberdeclaration() {
        return java_annotationtypememberdeclaration;
    }

    public void setJava_annotationtypememberdeclaration(java_AnnotationTypeMemberDeclaration java_annotationtypememberdeclaration) {
        this.java_annotationtypememberdeclaration = java_annotationtypememberdeclaration;
    }
    public java_TypeLiteral getJava_typeliteral() {
        return java_typeliteral;
    }

    public void setJava_typeliteral(java_TypeLiteral java_typeliteral) {
        this.java_typeliteral = java_typeliteral;
    }
    public java_SingleVariableDeclaration getJava_singlevariabledeclaration() {
        return java_singlevariabledeclaration;
    }

    public void setJava_singlevariabledeclaration(java_SingleVariableDeclaration java_singlevariabledeclaration) {
        this.java_singlevariabledeclaration = java_singlevariabledeclaration;
    }
    public java_AbstractTypeDeclaration getJava_abstracttypedeclaration() {
        return java_abstracttypedeclaration;
    }

    public void setJava_abstracttypedeclaration(java_AbstractTypeDeclaration java_abstracttypedeclaration) {
        this.java_abstracttypedeclaration = java_abstracttypedeclaration;
    }
    public java_AbstractMethodDeclaration getJava_abstractmethoddeclaration() {
        return java_abstractmethoddeclaration;
    }

    public void setJava_abstractmethoddeclaration(java_AbstractMethodDeclaration java_abstractmethoddeclaration) {
        this.java_abstractmethoddeclaration = java_abstractmethoddeclaration;
    }

}