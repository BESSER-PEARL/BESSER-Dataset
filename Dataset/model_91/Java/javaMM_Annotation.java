





import java.util.List;
import java.util.ArrayList;

public class javaMM_Annotation extends Expression {






    private javaMM_SingleVariableDeclaration javamm_singlevariabledeclaration;




    private javaMM_TypeAccess javamm_typeaccess;




    private javaMM_VariableDeclarationExpression javamm_variabledeclarationexpression;




    private javaMM_VariableDeclarationStatement javamm_variabledeclarationstatement;


    public javaMM_Annotation(
    ) {
        super(
        );
    }



    public javaMM_SingleVariableDeclaration getJavamm_singlevariabledeclaration() {
        return javamm_singlevariabledeclaration;
    }

    public void setJavamm_singlevariabledeclaration(javaMM_SingleVariableDeclaration javamm_singlevariabledeclaration) {
        this.javamm_singlevariabledeclaration = javamm_singlevariabledeclaration;
    }
    public javaMM_TypeAccess getJavamm_typeaccess() {
        return javamm_typeaccess;
    }

    public void setJavamm_typeaccess(javaMM_TypeAccess javamm_typeaccess) {
        this.javamm_typeaccess = javamm_typeaccess;
    }
    public javaMM_VariableDeclarationExpression getJavamm_variabledeclarationexpression() {
        return javamm_variabledeclarationexpression;
    }

    public void setJavamm_variabledeclarationexpression(javaMM_VariableDeclarationExpression javamm_variabledeclarationexpression) {
        this.javamm_variabledeclarationexpression = javamm_variabledeclarationexpression;
    }
    public javaMM_VariableDeclarationStatement getJavamm_variabledeclarationstatement() {
        return javamm_variabledeclarationstatement;
    }

    public void setJavamm_variabledeclarationstatement(javaMM_VariableDeclarationStatement javamm_variabledeclarationstatement) {
        this.javamm_variabledeclarationstatement = javamm_variabledeclarationstatement;
    }

}