





import java.util.List;
import java.util.ArrayList;

public class javaMM_CompilationUnit extends NamedElement {

    private String originalFilePath;





    private javaMM_Model javamm_model;




    private javaMM_Package javamm_package;




    private List<javaMM_Comment> javamm_comments;




    private List<javaMM_AbstractTypeDeclaration> javamm_abstracttypedeclarations;




    private List<javaMM_ImportDeclaration> javamm_importdeclarations;


    public javaMM_CompilationUnit(
        String originalFilePath    ) {
        super(
        );
        this.originalFilePath = originalFilePath;
        this.javamm_comments = new ArrayList<>();
        this.javamm_abstracttypedeclarations = new ArrayList<>();
        this.javamm_importdeclarations = new ArrayList<>();
    }

    public javaMM_CompilationUnit(
        String originalFilePath        ArrayList<javaMM_Comment> javamm_comments,        ArrayList<javaMM_AbstractTypeDeclaration> javamm_abstracttypedeclarations,        ArrayList<javaMM_ImportDeclaration> javamm_importdeclarations    ) {
        this.originalFilePath = originalFilePath;
        this.javamm_comments = javamm_comments;
        this.javamm_abstracttypedeclarations = javamm_abstracttypedeclarations;
        this.javamm_importdeclarations = javamm_importdeclarations;
    }

    public String getOriginalfilepath() {
        return originalFilePath;
    }

    public void setOriginalfilepath(String originalFilePath) {
        this.originalFilePath = originalFilePath;
    }

    public javaMM_Model getJavamm_model() {
        return javamm_model;
    }

    public void setJavamm_model(javaMM_Model javamm_model) {
        this.javamm_model = javamm_model;
    }
    public javaMM_Package getJavamm_package() {
        return javamm_package;
    }

    public void setJavamm_package(javaMM_Package javamm_package) {
        this.javamm_package = javamm_package;
    }
    public List<javaMM_Comment> getJavamm_comments() {
        return javamm_comments;
    }

    public void addJavamm_comment(Javamm_comment javamm_comment) {
        this.javamm_comments.add(javamm_comment);
    }
    public List<javaMM_AbstractTypeDeclaration> getJavamm_abstracttypedeclarations() {
        return javamm_abstracttypedeclarations;
    }

    public void addJavamm_abstracttypedeclaration(Javamm_abstracttypedeclaration javamm_abstracttypedeclaration) {
        this.javamm_abstracttypedeclarations.add(javamm_abstracttypedeclaration);
    }
    public List<javaMM_ImportDeclaration> getJavamm_importdeclarations() {
        return javamm_importdeclarations;
    }

    public void addJavamm_importdeclaration(Javamm_importdeclaration javamm_importdeclaration) {
        this.javamm_importdeclarations.add(javamm_importdeclaration);
    }

}