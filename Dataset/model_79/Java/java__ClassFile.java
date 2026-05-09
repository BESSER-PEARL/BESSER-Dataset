





import java.util.List;
import java.util.ArrayList;

public class java__ClassFile extends NamedElement {

    private String originalFilePath;





    private java__ASTNode java__astnode;




    private java__AbstractTypeDeclaration java__abstracttypedeclaration;




    private java__Package java__package;




    private java__CompilationUnit java__compilationunit;




    private java__Archive java__archive;


    public java__ClassFile(
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

    public java__ASTNode getJava__astnode() {
        return java__astnode;
    }

    public void setJava__astnode(java__ASTNode java__astnode) {
        this.java__astnode = java__astnode;
    }
    public java__AbstractTypeDeclaration getJava__abstracttypedeclaration() {
        return java__abstracttypedeclaration;
    }

    public void setJava__abstracttypedeclaration(java__AbstractTypeDeclaration java__abstracttypedeclaration) {
        this.java__abstracttypedeclaration = java__abstracttypedeclaration;
    }
    public java__Package getJava__package() {
        return java__package;
    }

    public void setJava__package(java__Package java__package) {
        this.java__package = java__package;
    }
    public java__CompilationUnit getJava__compilationunit() {
        return java__compilationunit;
    }

    public void setJava__compilationunit(java__CompilationUnit java__compilationunit) {
        this.java__compilationunit = java__compilationunit;
    }
    public java__Archive getJava__archive() {
        return java__archive;
    }

    public void setJava__archive(java__Archive java__archive) {
        this.java__archive = java__archive;
    }

}