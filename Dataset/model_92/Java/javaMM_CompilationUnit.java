





import java.util.List;
import java.util.ArrayList;

public class javaMM_CompilationUnit extends NamedElement {

    private String originalFilePath;





    private javaMM_Package javamm_package;




    private javaMM_ClassFile javamm_classfile;




    private javaMM_Model javamm_model;




    private List<javaMM_Comment> javamm_comments;




    private List<javaMM_ImportDeclaration> javamm_importdeclarations;




    private List<javaMM_AbstractTypeDeclaration> javamm_abstracttypedeclarations;


    public javaMM_CompilationUnit(
        String originalFilePath    ) {
        super(
        );
        this.originalFilePath = originalFilePath;
        this.javamm_comments = new ArrayList<>();
        this.javamm_importdeclarations = new ArrayList<>();
        this.javamm_abstracttypedeclarations = new ArrayList<>();
    }

    public javaMM_CompilationUnit(
        String originalFilePath        ArrayList<javaMM_Comment> javamm_comments,        ArrayList<javaMM_ImportDeclaration> javamm_importdeclarations,        ArrayList<javaMM_AbstractTypeDeclaration> javamm_abstracttypedeclarations    ) {
        this.originalFilePath = originalFilePath;
        this.javamm_comments = javamm_comments;
        this.javamm_importdeclarations = javamm_importdeclarations;
        this.javamm_abstracttypedeclarations = javamm_abstracttypedeclarations;
    }

    public String getOriginalfilepath() {
        return originalFilePath;
    }

    public void setOriginalfilepath(String originalFilePath) {
        this.originalFilePath = originalFilePath;
    }

    public javaMM_Package getJavamm_package() {
        return javamm_package;
    }

    public void setJavamm_package(javaMM_Package javamm_package) {
        this.javamm_package = javamm_package;
    }
    public javaMM_ClassFile getJavamm_classfile() {
        return javamm_classfile;
    }

    public void setJavamm_classfile(javaMM_ClassFile javamm_classfile) {
        this.javamm_classfile = javamm_classfile;
    }
    public javaMM_Model getJavamm_model() {
        return javamm_model;
    }

    public void setJavamm_model(javaMM_Model javamm_model) {
        this.javamm_model = javamm_model;
    }
    public List<javaMM_Comment> getJavamm_comments() {
        return javamm_comments;
    }

    public void addJavamm_comment(Javamm_comment javamm_comment) {
        this.javamm_comments.add(javamm_comment);
    }
    public List<javaMM_ImportDeclaration> getJavamm_importdeclarations() {
        return javamm_importdeclarations;
    }

    public void addJavamm_importdeclaration(Javamm_importdeclaration javamm_importdeclaration) {
        this.javamm_importdeclarations.add(javamm_importdeclaration);
    }
    public List<javaMM_AbstractTypeDeclaration> getJavamm_abstracttypedeclarations() {
        return javamm_abstracttypedeclarations;
    }

    public void addJavamm_abstracttypedeclaration(Javamm_abstracttypedeclaration javamm_abstracttypedeclaration) {
        this.javamm_abstracttypedeclarations.add(javamm_abstracttypedeclaration);
    }

}