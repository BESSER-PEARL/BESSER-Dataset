





import java.util.List;
import java.util.ArrayList;

public class java_AnnotationTypeMemberDeclaration extends BodyDeclaration {






    private java_AnnotationMemberValuePair java_annotationmembervaluepair;




    private java_TypeAccess java_typeaccess;




    private List<java_AnnotationMemberValuePair> java_annotationmembervaluepairs;




    private java_Expression java_expression;


    public java_AnnotationTypeMemberDeclaration(
    ) {
        super(
        );
        this.java_annotationmembervaluepairs = new ArrayList<>();
    }

    public java_AnnotationTypeMemberDeclaration(
        ArrayList<java_AnnotationMemberValuePair> java_annotationmembervaluepairs    ) {
        this.java_annotationmembervaluepairs = java_annotationmembervaluepairs;
    }


    public java_AnnotationMemberValuePair getJava_annotationmembervaluepair() {
        return java_annotationmembervaluepair;
    }

    public void setJava_annotationmembervaluepair(java_AnnotationMemberValuePair java_annotationmembervaluepair) {
        this.java_annotationmembervaluepair = java_annotationmembervaluepair;
    }
    public java_TypeAccess getJava_typeaccess() {
        return java_typeaccess;
    }

    public void setJava_typeaccess(java_TypeAccess java_typeaccess) {
        this.java_typeaccess = java_typeaccess;
    }
    public List<java_AnnotationMemberValuePair> getJava_annotationmembervaluepairs() {
        return java_annotationmembervaluepairs;
    }

    public void addJava_annotationmembervaluepair(Java_annotationmembervaluepair java_annotationmembervaluepair) {
        this.java_annotationmembervaluepairs.add(java_annotationmembervaluepair);
    }
    public java_Expression getJava_expression() {
        return java_expression;
    }

    public void setJava_expression(java_Expression java_expression) {
        this.java_expression = java_expression;
    }

}