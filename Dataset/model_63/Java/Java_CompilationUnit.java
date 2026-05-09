





import java.util.List;
import java.util.ArrayList;

public class Java_CompilationUnit extends NamedElement {

    private String originalFilePath;





    private Java_ClassFile java_classfile;




    private List<Java_ImportDeclaration> java_importdeclarations;




    private List<Java_AbstractTypeDeclaration> java_abstracttypedeclarations;




    private List<Java_Comment> java_comments;




    private Java_Package java_package;


    public Java_CompilationUnit(
        String originalFilePath    ) {
        super(
        );
        this.originalFilePath = originalFilePath;
        this.java_importdeclarations = new ArrayList<>();
        this.java_abstracttypedeclarations = new ArrayList<>();
        this.java_comments = new ArrayList<>();
    }

    public Java_CompilationUnit(
        String originalFilePath        ArrayList<Java_ImportDeclaration> java_importdeclarations,        ArrayList<Java_AbstractTypeDeclaration> java_abstracttypedeclarations,        ArrayList<Java_Comment> java_comments    ) {
        this.originalFilePath = originalFilePath;
        this.java_importdeclarations = java_importdeclarations;
        this.java_abstracttypedeclarations = java_abstracttypedeclarations;
        this.java_comments = java_comments;
    }

    public String getOriginalfilepath() {
        return originalFilePath;
    }

    public void setOriginalfilepath(String originalFilePath) {
        this.originalFilePath = originalFilePath;
    }

    public Java_ClassFile getJava_classfile() {
        return java_classfile;
    }

    public void setJava_classfile(Java_ClassFile java_classfile) {
        this.java_classfile = java_classfile;
    }
    public List<Java_ImportDeclaration> getJava_importdeclarations() {
        return java_importdeclarations;
    }

    public void addJava_importdeclaration(Java_importdeclaration java_importdeclaration) {
        this.java_importdeclarations.add(java_importdeclaration);
    }
    public List<Java_AbstractTypeDeclaration> getJava_abstracttypedeclarations() {
        return java_abstracttypedeclarations;
    }

    public void addJava_abstracttypedeclaration(Java_abstracttypedeclaration java_abstracttypedeclaration) {
        this.java_abstracttypedeclarations.add(java_abstracttypedeclaration);
    }
    public List<Java_Comment> getJava_comments() {
        return java_comments;
    }

    public void addJava_comment(Java_comment java_comment) {
        this.java_comments.add(java_comment);
    }
    public Java_Package getJava_package() {
        return java_package;
    }

    public void setJava_package(Java_Package java_package) {
        this.java_package = java_package;
    }

}