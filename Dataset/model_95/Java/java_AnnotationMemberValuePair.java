





import java.util.List;
import java.util.ArrayList;

public class java_AnnotationMemberValuePair extends NamedElement {






    private java_Annotation java_annotation;




    private java_AnnotationTypeMemberDeclaration java_annotationtypememberdeclaration;




    private java_Expression java_expression;


    public java_AnnotationMemberValuePair(
    ) {
        super(
        );
    }



    public java_Annotation getJava_annotation() {
        return java_annotation;
    }

    public void setJava_annotation(java_Annotation java_annotation) {
        this.java_annotation = java_annotation;
    }
    public java_AnnotationTypeMemberDeclaration getJava_annotationtypememberdeclaration() {
        return java_annotationtypememberdeclaration;
    }

    public void setJava_annotationtypememberdeclaration(java_AnnotationTypeMemberDeclaration java_annotationtypememberdeclaration) {
        this.java_annotationtypememberdeclaration = java_annotationtypememberdeclaration;
    }
    public java_Expression getJava_expression() {
        return java_expression;
    }

    public void setJava_expression(java_Expression java_expression) {
        this.java_expression = java_expression;
    }

}