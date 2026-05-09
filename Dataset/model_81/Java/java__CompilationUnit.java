





import java.util.List;
import java.util.ArrayList;

public class java__CompilationUnit extends NamedElement {

    private String originalFilePath;





    private List<java__ImportDeclaration> java__importdeclarations;




    private java__ClassFile java__classfile;




    private List<java__AbstractTypeDeclaration> java__abstracttypedeclarations;




    private java__Model java__model;




    private List<java__Comment> java__comments;


    public java__CompilationUnit(
        String originalFilePath    ) {
        super(
        );
        this.originalFilePath = originalFilePath;
        this.java__importdeclarations = new ArrayList<>();
        this.java__abstracttypedeclarations = new ArrayList<>();
        this.java__comments = new ArrayList<>();
    }

    public java__CompilationUnit(
        String originalFilePath        ArrayList<java__ImportDeclaration> java__importdeclarations,        ArrayList<java__AbstractTypeDeclaration> java__abstracttypedeclarations,        ArrayList<java__Comment> java__comments    ) {
        this.originalFilePath = originalFilePath;
        this.java__importdeclarations = java__importdeclarations;
        this.java__abstracttypedeclarations = java__abstracttypedeclarations;
        this.java__comments = java__comments;
    }

    public String getOriginalfilepath() {
        return originalFilePath;
    }

    public void setOriginalfilepath(String originalFilePath) {
        this.originalFilePath = originalFilePath;
    }

    public List<java__ImportDeclaration> getJava__importdeclarations() {
        return java__importdeclarations;
    }

    public void addJava__importdeclaration(Java__importdeclaration java__importdeclaration) {
        this.java__importdeclarations.add(java__importdeclaration);
    }
    public java__ClassFile getJava__classfile() {
        return java__classfile;
    }

    public void setJava__classfile(java__ClassFile java__classfile) {
        this.java__classfile = java__classfile;
    }
    public List<java__AbstractTypeDeclaration> getJava__abstracttypedeclarations() {
        return java__abstracttypedeclarations;
    }

    public void addJava__abstracttypedeclaration(Java__abstracttypedeclaration java__abstracttypedeclaration) {
        this.java__abstracttypedeclarations.add(java__abstracttypedeclaration);
    }
    public java__Model getJava__model() {
        return java__model;
    }

    public void setJava__model(java__Model java__model) {
        this.java__model = java__model;
    }
    public List<java__Comment> getJava__comments() {
        return java__comments;
    }

    public void addJava__comment(Java__comment java__comment) {
        this.java__comments.add(java__comment);
    }

}