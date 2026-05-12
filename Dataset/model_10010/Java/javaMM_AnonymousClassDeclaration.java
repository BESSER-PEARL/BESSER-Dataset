





import java.util.List;
import java.util.ArrayList;

public class javaMM_AnonymousClassDeclaration extends ASTNode {






    private javaMM_EnumConstantDeclaration javamm_enumconstantdeclaration;




    private List<javaMM_BodyDeclaration> javamm_bodydeclarations;




    private javaMM_BodyDeclaration javamm_bodydeclaration;


    public javaMM_AnonymousClassDeclaration(
    ) {
        super(
        );
        this.javamm_bodydeclarations = new ArrayList<>();
    }

    public javaMM_AnonymousClassDeclaration(
        ArrayList<javaMM_BodyDeclaration> javamm_bodydeclarations    ) {
        this.javamm_bodydeclarations = javamm_bodydeclarations;
    }


    public javaMM_EnumConstantDeclaration getJavamm_enumconstantdeclaration() {
        return javamm_enumconstantdeclaration;
    }

    public void setJavamm_enumconstantdeclaration(javaMM_EnumConstantDeclaration javamm_enumconstantdeclaration) {
        this.javamm_enumconstantdeclaration = javamm_enumconstantdeclaration;
    }
    public List<javaMM_BodyDeclaration> getJavamm_bodydeclarations() {
        return javamm_bodydeclarations;
    }

    public void addJavamm_bodydeclaration(Javamm_bodydeclaration javamm_bodydeclaration) {
        this.javamm_bodydeclarations.add(javamm_bodydeclaration);
    }
    public javaMM_BodyDeclaration getJavamm_bodydeclaration() {
        return javamm_bodydeclaration;
    }

    public void setJavamm_bodydeclaration(javaMM_BodyDeclaration javamm_bodydeclaration) {
        this.javamm_bodydeclaration = javamm_bodydeclaration;
    }

}