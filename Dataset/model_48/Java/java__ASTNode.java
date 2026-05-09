





import java.util.List;
import java.util.ArrayList;

public class java__ASTNode  {






    private java__ClassFile java__classfile;




    private java__CompilationUnit java__compilationunit;




    private List<java__Comment> java__comments;




    private java__TagElement java__tagelement;


    public java__ASTNode(
    ) {
        this.java__comments = new ArrayList<>();
    }

    public java__ASTNode(
        ArrayList<java__Comment> java__comments    ) {
        this.java__comments = java__comments;
    }


    public java__ClassFile getJava__classfile() {
        return java__classfile;
    }

    public void setJava__classfile(java__ClassFile java__classfile) {
        this.java__classfile = java__classfile;
    }
    public java__CompilationUnit getJava__compilationunit() {
        return java__compilationunit;
    }

    public void setJava__compilationunit(java__CompilationUnit java__compilationunit) {
        this.java__compilationunit = java__compilationunit;
    }
    public List<java__Comment> getJava__comments() {
        return java__comments;
    }

    public void addJava__comment(Java__comment java__comment) {
        this.java__comments.add(java__comment);
    }
    public java__TagElement getJava__tagelement() {
        return java__tagelement;
    }

    public void setJava__tagelement(java__TagElement java__tagelement) {
        this.java__tagelement = java__tagelement;
    }

}