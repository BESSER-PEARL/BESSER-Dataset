





import java.util.List;
import java.util.ArrayList;

public class java_ASTNode  {






    private List<java_Comment> java_comments;




    private java_CompilationUnit java_compilationunit;




    private java_ClassFile java_classfile;


    public java_ASTNode(
    ) {
        this.java_comments = new ArrayList<>();
    }

    public java_ASTNode(
        ArrayList<java_Comment> java_comments    ) {
        this.java_comments = java_comments;
    }


    public List<java_Comment> getJava_comments() {
        return java_comments;
    }

    public void addJava_comment(Java_comment java_comment) {
        this.java_comments.add(java_comment);
    }
    public java_CompilationUnit getJava_compilationunit() {
        return java_compilationunit;
    }

    public void setJava_compilationunit(java_CompilationUnit java_compilationunit) {
        this.java_compilationunit = java_compilationunit;
    }
    public java_ClassFile getJava_classfile() {
        return java_classfile;
    }

    public void setJava_classfile(java_ClassFile java_classfile) {
        this.java_classfile = java_classfile;
    }

}