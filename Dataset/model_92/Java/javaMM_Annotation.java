





import java.util.List;
import java.util.ArrayList;

public class javaMM_Annotation extends Expression {






    private javaMM_SingleVariableDeclaration javamm_singlevariabledeclaration;




    private javaMM_VariableDeclarationExpression javamm_variabledeclarationexpression;




    private javaMM_BodyDeclaration javamm_bodydeclaration;




    private List<javaMM_AnnotationMemberValuePair> javamm_annotationmembervaluepairs;




    private javaMM_TypeAccess javamm_typeaccess;




    private javaMM_VariableDeclarationStatement javamm_variabledeclarationstatement;


    public javaMM_Annotation(
    ) {
        super(
        );
        this.javamm_annotationmembervaluepairs = new ArrayList<>();
    }

    public javaMM_Annotation(
        ArrayList<javaMM_AnnotationMemberValuePair> javamm_annotationmembervaluepairs    ) {
        this.javamm_annotationmembervaluepairs = javamm_annotationmembervaluepairs;
    }


    public javaMM_SingleVariableDeclaration getJavamm_singlevariabledeclaration() {
        return javamm_singlevariabledeclaration;
    }

    public void setJavamm_singlevariabledeclaration(javaMM_SingleVariableDeclaration javamm_singlevariabledeclaration) {
        this.javamm_singlevariabledeclaration = javamm_singlevariabledeclaration;
    }
    public javaMM_VariableDeclarationExpression getJavamm_variabledeclarationexpression() {
        return javamm_variabledeclarationexpression;
    }

    public void setJavamm_variabledeclarationexpression(javaMM_VariableDeclarationExpression javamm_variabledeclarationexpression) {
        this.javamm_variabledeclarationexpression = javamm_variabledeclarationexpression;
    }
    public javaMM_BodyDeclaration getJavamm_bodydeclaration() {
        return javamm_bodydeclaration;
    }

    public void setJavamm_bodydeclaration(javaMM_BodyDeclaration javamm_bodydeclaration) {
        this.javamm_bodydeclaration = javamm_bodydeclaration;
    }
    public List<javaMM_AnnotationMemberValuePair> getJavamm_annotationmembervaluepairs() {
        return javamm_annotationmembervaluepairs;
    }

    public void addJavamm_annotationmembervaluepair(Javamm_annotationmembervaluepair javamm_annotationmembervaluepair) {
        this.javamm_annotationmembervaluepairs.add(javamm_annotationmembervaluepair);
    }
    public javaMM_TypeAccess getJavamm_typeaccess() {
        return javamm_typeaccess;
    }

    public void setJavamm_typeaccess(javaMM_TypeAccess javamm_typeaccess) {
        this.javamm_typeaccess = javamm_typeaccess;
    }
    public javaMM_VariableDeclarationStatement getJavamm_variabledeclarationstatement() {
        return javamm_variabledeclarationstatement;
    }

    public void setJavamm_variabledeclarationstatement(javaMM_VariableDeclarationStatement javamm_variabledeclarationstatement) {
        this.javamm_variabledeclarationstatement = javamm_variabledeclarationstatement;
    }

}