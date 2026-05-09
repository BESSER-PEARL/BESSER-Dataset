





import java.util.List;
import java.util.ArrayList;

public class java__CompilationUnit extends NamedElement {

    private String originalFilePath;





    private java__ASTNode java__astnode;




    private List<java__AbstractTypeDeclaration> java__abstracttypedeclarations;




    private java__Package java__package;




    private List<java__ImportDeclaration> java__importdeclarations;




    private List<java__Comment> java__comments;


    public java__CompilationUnit(
        String originalFilePath    ) {
        super(
        );
        this.originalFilePath = originalFilePath;
        this.java__abstracttypedeclarations = new ArrayList<>();
        this.java__importdeclarations = new ArrayList<>();
        this.java__comments = new ArrayList<>();
    }

    public java__CompilationUnit(
        String originalFilePath        ArrayList<java__AbstractTypeDeclaration> java__abstracttypedeclarations,        ArrayList<java__ImportDeclaration> java__importdeclarations,        ArrayList<java__Comment> java__comments    ) {
        this.originalFilePath = originalFilePath;
        this.java__abstracttypedeclarations = java__abstracttypedeclarations;
        this.java__importdeclarations = java__importdeclarations;
        this.java__comments = java__comments;
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
    public List<java__AbstractTypeDeclaration> getJava__abstracttypedeclarations() {
        return java__abstracttypedeclarations;
    }

    public void addJava__abstracttypedeclaration(Java__abstracttypedeclaration java__abstracttypedeclaration) {
        this.java__abstracttypedeclarations.add(java__abstracttypedeclaration);
    }
    public java__Package getJava__package() {
        return java__package;
    }

    public void setJava__package(java__Package java__package) {
        this.java__package = java__package;
    }
    public List<java__ImportDeclaration> getJava__importdeclarations() {
        return java__importdeclarations;
    }

    public void addJava__importdeclaration(Java__importdeclaration java__importdeclaration) {
        this.java__importdeclarations.add(java__importdeclaration);
    }
    public List<java__Comment> getJava__comments() {
        return java__comments;
    }

    public void addJava__comment(Java__comment java__comment) {
        this.java__comments.add(java__comment);
    }

}