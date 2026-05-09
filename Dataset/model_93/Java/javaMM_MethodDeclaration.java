





import java.util.List;
import java.util.ArrayList;

public class javaMM_MethodDeclaration extends AbstractMethodDeclaration {

    private int extraArrayDimensions;





    private javaMM_TypeAccess javamm_typeaccess;




    private javaMM_MethodDeclaration javamm_methoddeclaration;




    private List<javaMM_MethodDeclaration> javamm_methoddeclarations;


    public javaMM_MethodDeclaration(
        int extraArrayDimensions    ) {
        super(
        );
        this.extraArrayDimensions = extraArrayDimensions;
        this.javamm_methoddeclarations = new ArrayList<>();
    }

    public javaMM_MethodDeclaration(
        int extraArrayDimensions        ArrayList<javaMM_MethodDeclaration> javamm_methoddeclarations    ) {
        this.extraArrayDimensions = extraArrayDimensions;
        this.javamm_methoddeclarations = javamm_methoddeclarations;
    }

    public int getExtraarraydimensions() {
        return extraArrayDimensions;
    }

    public void setExtraarraydimensions(int extraArrayDimensions) {
        this.extraArrayDimensions = extraArrayDimensions;
    }

    public javaMM_TypeAccess getJavamm_typeaccess() {
        return javamm_typeaccess;
    }

    public void setJavamm_typeaccess(javaMM_TypeAccess javamm_typeaccess) {
        this.javamm_typeaccess = javamm_typeaccess;
    }
    public javaMM_MethodDeclaration getJavamm_methoddeclaration() {
        return javamm_methoddeclaration;
    }

    public void setJavamm_methoddeclaration(javaMM_MethodDeclaration javamm_methoddeclaration) {
        this.javamm_methoddeclaration = javamm_methoddeclaration;
    }
    public List<javaMM_MethodDeclaration> getJavamm_methoddeclarations() {
        return javamm_methoddeclarations;
    }

    public void addJavamm_methoddeclaration(Javamm_methoddeclaration javamm_methoddeclaration) {
        this.javamm_methoddeclarations.add(javamm_methoddeclaration);
    }

}