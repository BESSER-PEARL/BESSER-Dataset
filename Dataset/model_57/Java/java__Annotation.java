





import java.util.List;
import java.util.ArrayList;

public class java__Annotation extends Expression {






    private List<java__AnnotationMemberValuePair> java__annotationmembervaluepairs;




    private java__VariableDeclarationExpression java__variabledeclarationexpression;




    private java__BodyDeclaration java__bodydeclaration;




    private java__VariableDeclarationStatement java__variabledeclarationstatement;




    private java__TypeAccess java__typeaccess;




    private java__SingleVariableDeclaration java__singlevariabledeclaration;


    public java__Annotation(
    ) {
        super(
        );
        this.java__annotationmembervaluepairs = new ArrayList<>();
    }

    public java__Annotation(
        ArrayList<java__AnnotationMemberValuePair> java__annotationmembervaluepairs    ) {
        this.java__annotationmembervaluepairs = java__annotationmembervaluepairs;
    }


    public List<java__AnnotationMemberValuePair> getJava__annotationmembervaluepairs() {
        return java__annotationmembervaluepairs;
    }

    public void addJava__annotationmembervaluepair(Java__annotationmembervaluepair java__annotationmembervaluepair) {
        this.java__annotationmembervaluepairs.add(java__annotationmembervaluepair);
    }
    public java__VariableDeclarationExpression getJava__variabledeclarationexpression() {
        return java__variabledeclarationexpression;
    }

    public void setJava__variabledeclarationexpression(java__VariableDeclarationExpression java__variabledeclarationexpression) {
        this.java__variabledeclarationexpression = java__variabledeclarationexpression;
    }
    public java__BodyDeclaration getJava__bodydeclaration() {
        return java__bodydeclaration;
    }

    public void setJava__bodydeclaration(java__BodyDeclaration java__bodydeclaration) {
        this.java__bodydeclaration = java__bodydeclaration;
    }
    public java__VariableDeclarationStatement getJava__variabledeclarationstatement() {
        return java__variabledeclarationstatement;
    }

    public void setJava__variabledeclarationstatement(java__VariableDeclarationStatement java__variabledeclarationstatement) {
        this.java__variabledeclarationstatement = java__variabledeclarationstatement;
    }
    public java__TypeAccess getJava__typeaccess() {
        return java__typeaccess;
    }

    public void setJava__typeaccess(java__TypeAccess java__typeaccess) {
        this.java__typeaccess = java__typeaccess;
    }
    public java__SingleVariableDeclaration getJava__singlevariabledeclaration() {
        return java__singlevariabledeclaration;
    }

    public void setJava__singlevariabledeclaration(java__SingleVariableDeclaration java__singlevariabledeclaration) {
        this.java__singlevariabledeclaration = java__singlevariabledeclaration;
    }

}