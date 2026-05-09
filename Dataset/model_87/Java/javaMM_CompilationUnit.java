





import java.util.List;
import java.util.ArrayList;

public class javaMM_CompilationUnit extends NamedElement {

    private String originalFilePath;





    private List<javaMM_AbstractTypeDeclaration> javamm_abstracttypedeclarations;




    private javaMM_Package javamm_package;


    public javaMM_CompilationUnit(
        String originalFilePath    ) {
        super(
        );
        this.originalFilePath = originalFilePath;
        this.javamm_abstracttypedeclarations = new ArrayList<>();
    }

    public javaMM_CompilationUnit(
        String originalFilePath        ArrayList<javaMM_AbstractTypeDeclaration> javamm_abstracttypedeclarations    ) {
        this.originalFilePath = originalFilePath;
        this.javamm_abstracttypedeclarations = javamm_abstracttypedeclarations;
    }

    public String getOriginalfilepath() {
        return originalFilePath;
    }

    public void setOriginalfilepath(String originalFilePath) {
        this.originalFilePath = originalFilePath;
    }

    public List<javaMM_AbstractTypeDeclaration> getJavamm_abstracttypedeclarations() {
        return javamm_abstracttypedeclarations;
    }

    public void addJavamm_abstracttypedeclaration(Javamm_abstracttypedeclaration javamm_abstracttypedeclaration) {
        this.javamm_abstracttypedeclarations.add(javamm_abstracttypedeclaration);
    }
    public javaMM_Package getJavamm_package() {
        return javamm_package;
    }

    public void setJavamm_package(javaMM_Package javamm_package) {
        this.javamm_package = javamm_package;
    }

}