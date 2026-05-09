





import java.util.List;
import java.util.ArrayList;

public class java_CompilationUnit extends NamedElement {

    private String originalFilePath;





    private List<java_ImportDeclaration> java_importdeclarations;




    private List<java_AbstractTypeDeclaration> java_abstracttypedeclarations;


    public java_CompilationUnit(
        String originalFilePath    ) {
        super(
        );
        this.originalFilePath = originalFilePath;
        this.java_importdeclarations = new ArrayList<>();
        this.java_abstracttypedeclarations = new ArrayList<>();
    }

    public java_CompilationUnit(
        String originalFilePath        ArrayList<java_ImportDeclaration> java_importdeclarations,        ArrayList<java_AbstractTypeDeclaration> java_abstracttypedeclarations    ) {
        this.originalFilePath = originalFilePath;
        this.java_importdeclarations = java_importdeclarations;
        this.java_abstracttypedeclarations = java_abstracttypedeclarations;
    }

    public String getOriginalfilepath() {
        return originalFilePath;
    }

    public void setOriginalfilepath(String originalFilePath) {
        this.originalFilePath = originalFilePath;
    }

    public List<java_ImportDeclaration> getJava_importdeclarations() {
        return java_importdeclarations;
    }

    public void addJava_importdeclaration(Java_importdeclaration java_importdeclaration) {
        this.java_importdeclarations.add(java_importdeclaration);
    }
    public List<java_AbstractTypeDeclaration> getJava_abstracttypedeclarations() {
        return java_abstracttypedeclarations;
    }

    public void addJava_abstracttypedeclaration(Java_abstracttypedeclaration java_abstracttypedeclaration) {
        this.java_abstracttypedeclarations.add(java_abstracttypedeclaration);
    }

}