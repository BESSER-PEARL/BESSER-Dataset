





import java.util.List;
import java.util.ArrayList;

public class javaMM_EnumDeclaration extends AbstractTypeDeclaration {






    private List<javaMM_EnumConstantDeclaration> javamm_enumconstantdeclarations;


    public javaMM_EnumDeclaration(
    ) {
        super(
        );
        this.javamm_enumconstantdeclarations = new ArrayList<>();
    }

    public javaMM_EnumDeclaration(
        ArrayList<javaMM_EnumConstantDeclaration> javamm_enumconstantdeclarations    ) {
        this.javamm_enumconstantdeclarations = javamm_enumconstantdeclarations;
    }


    public List<javaMM_EnumConstantDeclaration> getJavamm_enumconstantdeclarations() {
        return javamm_enumconstantdeclarations;
    }

    public void addJavamm_enumconstantdeclaration(Javamm_enumconstantdeclaration javamm_enumconstantdeclaration) {
        this.javamm_enumconstantdeclarations.add(javamm_enumconstantdeclaration);
    }

}