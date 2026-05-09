





import java.util.List;
import java.util.ArrayList;

public class java_Annotation extends Expression {






    private java_BodyDeclaration java_bodydeclaration;




    private java_SingleVariableDeclaration java_singlevariabledeclaration;




    private List<java_AnnotationMemberValuePair> java_annotationmembervaluepairs;


    public java_Annotation(
    ) {
        super(
        );
        this.java_annotationmembervaluepairs = new ArrayList<>();
    }

    public java_Annotation(
        ArrayList<java_AnnotationMemberValuePair> java_annotationmembervaluepairs    ) {
        this.java_annotationmembervaluepairs = java_annotationmembervaluepairs;
    }


    public java_BodyDeclaration getJava_bodydeclaration() {
        return java_bodydeclaration;
    }

    public void setJava_bodydeclaration(java_BodyDeclaration java_bodydeclaration) {
        this.java_bodydeclaration = java_bodydeclaration;
    }
    public java_SingleVariableDeclaration getJava_singlevariabledeclaration() {
        return java_singlevariabledeclaration;
    }

    public void setJava_singlevariabledeclaration(java_SingleVariableDeclaration java_singlevariabledeclaration) {
        this.java_singlevariabledeclaration = java_singlevariabledeclaration;
    }
    public List<java_AnnotationMemberValuePair> getJava_annotationmembervaluepairs() {
        return java_annotationmembervaluepairs;
    }

    public void addJava_annotationmembervaluepair(Java_annotationmembervaluepair java_annotationmembervaluepair) {
        this.java_annotationmembervaluepairs.add(java_annotationmembervaluepair);
    }

}