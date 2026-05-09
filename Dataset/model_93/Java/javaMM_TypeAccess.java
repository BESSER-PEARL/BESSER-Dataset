





import java.util.List;
import java.util.ArrayList;

public class javaMM_TypeAccess extends Expression, NamespaceAccess {






    private javaMM_AnnotationTypeMemberDeclaration javamm_annotationtypememberdeclaration;




    private javaMM_AbstractTypeDeclaration javamm_abstracttypedeclaration;




    private javaMM_Annotation javamm_annotation;




    private javaMM_AbstractTypeQualifiedExpression javamm_abstracttypequalifiedexpression;




    private javaMM_AbstractMethodDeclaration javamm_abstractmethoddeclaration;


    public javaMM_TypeAccess(
    ) {
        super(
        );
    }



    public javaMM_AnnotationTypeMemberDeclaration getJavamm_annotationtypememberdeclaration() {
        return javamm_annotationtypememberdeclaration;
    }

    public void setJavamm_annotationtypememberdeclaration(javaMM_AnnotationTypeMemberDeclaration javamm_annotationtypememberdeclaration) {
        this.javamm_annotationtypememberdeclaration = javamm_annotationtypememberdeclaration;
    }
    public javaMM_AbstractTypeDeclaration getJavamm_abstracttypedeclaration() {
        return javamm_abstracttypedeclaration;
    }

    public void setJavamm_abstracttypedeclaration(javaMM_AbstractTypeDeclaration javamm_abstracttypedeclaration) {
        this.javamm_abstracttypedeclaration = javamm_abstracttypedeclaration;
    }
    public javaMM_Annotation getJavamm_annotation() {
        return javamm_annotation;
    }

    public void setJavamm_annotation(javaMM_Annotation javamm_annotation) {
        this.javamm_annotation = javamm_annotation;
    }
    public javaMM_AbstractTypeQualifiedExpression getJavamm_abstracttypequalifiedexpression() {
        return javamm_abstracttypequalifiedexpression;
    }

    public void setJavamm_abstracttypequalifiedexpression(javaMM_AbstractTypeQualifiedExpression javamm_abstracttypequalifiedexpression) {
        this.javamm_abstracttypequalifiedexpression = javamm_abstracttypequalifiedexpression;
    }
    public javaMM_AbstractMethodDeclaration getJavamm_abstractmethoddeclaration() {
        return javamm_abstractmethoddeclaration;
    }

    public void setJavamm_abstractmethoddeclaration(javaMM_AbstractMethodDeclaration javamm_abstractmethoddeclaration) {
        this.javamm_abstractmethoddeclaration = javamm_abstractmethoddeclaration;
    }

}