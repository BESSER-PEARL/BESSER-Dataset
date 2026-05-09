





import java.util.List;
import java.util.ArrayList;

public class java_Annotation extends Expression {






    private java_BodyDeclaration java_bodydeclaration;




    private java_TypeAccess java_typeaccess;




    private List<java_AnnotationMemberValuePair> java_annotationmembervaluepairs;




    private java_VariableDeclarationStatement java_variabledeclarationstatement;




    private java_VariableDeclarationExpression java_variabledeclarationexpression;




    private java_SingleVariableDeclaration java_singlevariabledeclaration;


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
    public java_VariableDeclarationStatement getJava_variabledeclarationstatement() {
        return java_variabledeclarationstatement;
    }

    public void setJava_variabledeclarationstatement(java_VariableDeclarationStatement java_variabledeclarationstatement) {
        this.java_variabledeclarationstatement = java_variabledeclarationstatement;
    }
    public java_VariableDeclarationExpression getJava_variabledeclarationexpression() {
        return java_variabledeclarationexpression;
    }

    public void setJava_variabledeclarationexpression(java_VariableDeclarationExpression java_variabledeclarationexpression) {
        this.java_variabledeclarationexpression = java_variabledeclarationexpression;
    }
    public java_SingleVariableDeclaration getJava_singlevariabledeclaration() {
        return java_singlevariabledeclaration;
    }

    public void setJava_singlevariabledeclaration(java_SingleVariableDeclaration java_singlevariabledeclaration) {
        this.java_singlevariabledeclaration = java_singlevariabledeclaration;
    }

}