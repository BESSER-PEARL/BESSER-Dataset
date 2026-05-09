





import java.util.List;
import java.util.ArrayList;

public class java_CompilationUnit extends NamedElement {

    private String originalFilePath;





    private java_ClassFile java_classfile;




    private List<java_Comment> java_comments;




    private List<java_ImportDeclaration> java_importdeclarations;




    private List<java_AbstractTypeDeclaration> java_abstracttypedeclarations;




    private java_ASTNode java_astnode;




    private java_Package java_package;


    public java_CompilationUnit(
        String originalFilePath    ) {
        super(
        );
        this.originalFilePath = originalFilePath;
        this.java_comments = new ArrayList<>();
        this.java_importdeclarations = new ArrayList<>();
        this.java_abstracttypedeclarations = new ArrayList<>();
    }

    public java_CompilationUnit(
        String originalFilePath        ArrayList<java_Comment> java_comments,        ArrayList<java_ImportDeclaration> java_importdeclarations,        ArrayList<java_AbstractTypeDeclaration> java_abstracttypedeclarations    ) {
        this.originalFilePath = originalFilePath;
        this.java_comments = java_comments;
        this.java_importdeclarations = java_importdeclarations;
        this.java_abstracttypedeclarations = java_abstracttypedeclarations;
    }

    public String getOriginalfilepath() {
        return originalFilePath;
    }

    public void setOriginalfilepath(String originalFilePath) {
        this.originalFilePath = originalFilePath;
    }

    public java_ClassFile getJava_classfile() {
        return java_classfile;
    }

    public void setJava_classfile(java_ClassFile java_classfile) {
        this.java_classfile = java_classfile;
    }
    public List<java_Comment> getJava_comments() {
        return java_comments;
    }

    public void addJava_comment(Java_comment java_comment) {
        this.java_comments.add(java_comment);
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
    public java_ASTNode getJava_astnode() {
        return java_astnode;
    }

    public void setJava_astnode(java_ASTNode java_astnode) {
        this.java_astnode = java_astnode;
    }
    public java_Package getJava_package() {
        return java_package;
    }

    public void setJava_package(java_Package java_package) {
        this.java_package = java_package;
    }

}