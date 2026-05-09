





import java.util.List;
import java.util.ArrayList;

public class java_Expression extends ASTNode {






    private java_AnnotationMemberValuePair java_annotationmembervaluepair;




    private java_VariableDeclaration java_variabledeclaration;




    private java_AbstractMethodInvocation java_abstractmethodinvocation;




    private java_AnnotationTypeMemberDeclaration java_annotationtypememberdeclaration;




    private java_EnumConstantDeclaration java_enumconstantdeclaration;


    public java_Expression(
    ) {
        super(
        );
    }



    public java_AnnotationMemberValuePair getJava_annotationmembervaluepair() {
        return java_annotationmembervaluepair;
    }

    public void setJava_annotationmembervaluepair(java_AnnotationMemberValuePair java_annotationmembervaluepair) {
        this.java_annotationmembervaluepair = java_annotationmembervaluepair;
    }
    public java_VariableDeclaration getJava_variabledeclaration() {
        return java_variabledeclaration;
    }

    public void setJava_variabledeclaration(java_VariableDeclaration java_variabledeclaration) {
        this.java_variabledeclaration = java_variabledeclaration;
    }
    public java_AbstractMethodInvocation getJava_abstractmethodinvocation() {
        return java_abstractmethodinvocation;
    }

    public void setJava_abstractmethodinvocation(java_AbstractMethodInvocation java_abstractmethodinvocation) {
        this.java_abstractmethodinvocation = java_abstractmethodinvocation;
    }
    public java_AnnotationTypeMemberDeclaration getJava_annotationtypememberdeclaration() {
        return java_annotationtypememberdeclaration;
    }

    public void setJava_annotationtypememberdeclaration(java_AnnotationTypeMemberDeclaration java_annotationtypememberdeclaration) {
        this.java_annotationtypememberdeclaration = java_annotationtypememberdeclaration;
    }
    public java_EnumConstantDeclaration getJava_enumconstantdeclaration() {
        return java_enumconstantdeclaration;
    }

    public void setJava_enumconstantdeclaration(java_EnumConstantDeclaration java_enumconstantdeclaration) {
        this.java_enumconstantdeclaration = java_enumconstantdeclaration;
    }

}