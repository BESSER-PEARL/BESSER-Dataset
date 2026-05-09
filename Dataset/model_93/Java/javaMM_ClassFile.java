





import java.util.List;
import java.util.ArrayList;

public class javaMM_ClassFile extends NamedElement {

    private String originalFilePath;





    private javaMM_AbstractTypeDeclaration javamm_abstracttypedeclaration;




    private javaMM_Archive javamm_archive;




    private javaMM_Model javamm_model;




    private javaMM_Package javamm_package;




    private javaMM_CompilationUnit javamm_compilationunit;


    public javaMM_ClassFile(
        String originalFilePath    ) {
        super(
        );
        this.originalFilePath = originalFilePath;
    }


    public String getOriginalfilepath() {
        return originalFilePath;
    }

    public void setOriginalfilepath(String originalFilePath) {
        this.originalFilePath = originalFilePath;
    }

    public javaMM_AbstractTypeDeclaration getJavamm_abstracttypedeclaration() {
        return javamm_abstracttypedeclaration;
    }

    public void setJavamm_abstracttypedeclaration(javaMM_AbstractTypeDeclaration javamm_abstracttypedeclaration) {
        this.javamm_abstracttypedeclaration = javamm_abstracttypedeclaration;
    }
    public javaMM_Archive getJavamm_archive() {
        return javamm_archive;
    }

    public void setJavamm_archive(javaMM_Archive javamm_archive) {
        this.javamm_archive = javamm_archive;
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
    public javaMM_CompilationUnit getJavamm_compilationunit() {
        return javamm_compilationunit;
    }

    public void setJavamm_compilationunit(javaMM_CompilationUnit javamm_compilationunit) {
        this.javamm_compilationunit = javamm_compilationunit;
    }

}