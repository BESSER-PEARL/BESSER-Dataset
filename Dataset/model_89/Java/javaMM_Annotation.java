





import java.util.List;
import java.util.ArrayList;

public class javaMM_Annotation extends Expression {






    private javaMM_TypeAccess javamm_typeaccess;




    private javaMM_SingleVariableDeclaration javamm_singlevariabledeclaration;




    private javaMM_BodyDeclaration javamm_bodydeclaration;


    public javaMM_Annotation(
    ) {
        super(
        );
    }



    public javaMM_TypeAccess getJavamm_typeaccess() {
        return javamm_typeaccess;
    }

    public void setJavamm_typeaccess(javaMM_TypeAccess javamm_typeaccess) {
        this.javamm_typeaccess = javamm_typeaccess;
    }
    public javaMM_SingleVariableDeclaration getJavamm_singlevariabledeclaration() {
        return javamm_singlevariabledeclaration;
    }

    public void setJavamm_singlevariabledeclaration(javaMM_SingleVariableDeclaration javamm_singlevariabledeclaration) {
        this.javamm_singlevariabledeclaration = javamm_singlevariabledeclaration;
    }
    public javaMM_BodyDeclaration getJavamm_bodydeclaration() {
        return javamm_bodydeclaration;
    }

    public void setJavamm_bodydeclaration(javaMM_BodyDeclaration javamm_bodydeclaration) {
        this.javamm_bodydeclaration = javamm_bodydeclaration;
    }

}