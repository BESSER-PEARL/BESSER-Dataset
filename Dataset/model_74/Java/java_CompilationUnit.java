





import java.util.List;
import java.util.ArrayList;

public class java_CompilationUnit extends NamedElement {

    private String originalFilePath;





    private List<java_AbstractTypeDeclaration> java_abstracttypedeclarations;




    private java_Package java_package;




    private java_ClassFile java_classfile;


    public java_CompilationUnit(
        String originalFilePath    ) {
        super(
        );
        this.originalFilePath = originalFilePath;
        this.java_abstracttypedeclarations = new ArrayList<>();
    }

    public java_CompilationUnit(
        String originalFilePath        ArrayList<java_AbstractTypeDeclaration> java_abstracttypedeclarations    ) {
        this.originalFilePath = originalFilePath;
        this.java_abstracttypedeclarations = java_abstracttypedeclarations;
    }

    public String getOriginalfilepath() {
        return originalFilePath;
    }

    public void setOriginalfilepath(String originalFilePath) {
        this.originalFilePath = originalFilePath;
    }

    public List<java_AbstractTypeDeclaration> getJava_abstracttypedeclarations() {
        return java_abstracttypedeclarations;
    }

    public void addJava_abstracttypedeclaration(Java_abstracttypedeclaration java_abstracttypedeclaration) {
        this.java_abstracttypedeclarations.add(java_abstracttypedeclaration);
    }
    public java_Package getJava_package() {
        return java_package;
    }

    public void setJava_package(java_Package java_package) {
        this.java_package = java_package;
    }
    public java_ClassFile getJava_classfile() {
        return java_classfile;
    }

    public void setJava_classfile(java_ClassFile java_classfile) {
        this.java_classfile = java_classfile;
    }

}