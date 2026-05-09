





import java.util.List;
import java.util.ArrayList;

public class Java_ASTNode  {






    private Java_TagElement java_tagelement;




    private Java_UnresolvedItemAccess java_unresolveditemaccess;




    private Java_CompilationUnit java_compilationunit;




    private Java_ClassFile java_classfile;




    private List<Java_Comment> java_comments;


    public Java_ASTNode(
    ) {
        this.java_comments = new ArrayList<>();
    }

    public Java_ASTNode(
        ArrayList<Java_Comment> java_comments    ) {
        this.java_comments = java_comments;
    }


    public Java_TagElement getJava_tagelement() {
        return java_tagelement;
    }

    public void setJava_tagelement(Java_TagElement java_tagelement) {
        this.java_tagelement = java_tagelement;
    }
    public Java_UnresolvedItemAccess getJava_unresolveditemaccess() {
        return java_unresolveditemaccess;
    }

    public void setJava_unresolveditemaccess(Java_UnresolvedItemAccess java_unresolveditemaccess) {
        this.java_unresolveditemaccess = java_unresolveditemaccess;
    }
    public Java_CompilationUnit getJava_compilationunit() {
        return java_compilationunit;
    }

    public void setJava_compilationunit(Java_CompilationUnit java_compilationunit) {
        this.java_compilationunit = java_compilationunit;
    }
    public Java_ClassFile getJava_classfile() {
        return java_classfile;
    }

    public void setJava_classfile(Java_ClassFile java_classfile) {
        this.java_classfile = java_classfile;
    }
    public List<Java_Comment> getJava_comments() {
        return java_comments;
    }

    public void addJava_comment(Java_comment java_comment) {
        this.java_comments.add(java_comment);
    }

}