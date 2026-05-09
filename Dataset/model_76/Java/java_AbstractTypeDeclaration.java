





import java.util.List;
import java.util.ArrayList;

public class java_AbstractTypeDeclaration extends Type, BodyDeclaration {






    private java_CompilationUnit java_compilationunit;




    private java_ClassFile java_classfile;




    private List<java_Comment> java_comments;




    private java_Package java_package;




    private List<java_BodyDeclaration> java_bodydeclarations;




    private java_BodyDeclaration java_bodydeclaration;




    private List<java_TypeAccess> java_typeaccesss;




    private List<java_Comment> java_comments;




    private java_Package java_package;


    public java_AbstractTypeDeclaration(
    ) {
        super(
        );
        this.java_comments = new ArrayList<>();
        this.java_bodydeclarations = new ArrayList<>();
        this.java_typeaccesss = new ArrayList<>();
        this.java_comments = new ArrayList<>();
    }

    public java_AbstractTypeDeclaration(
        ArrayList<java_Comment> java_comments,        ArrayList<java_BodyDeclaration> java_bodydeclarations,        ArrayList<java_TypeAccess> java_typeaccesss,        ArrayList<java_Comment> java_comments    ) {
        this.java_comments = java_comments;
        this.java_bodydeclarations = java_bodydeclarations;
        this.java_typeaccesss = java_typeaccesss;
        this.java_comments = java_comments;
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
    public List<java_Comment> getJava_comments() {
        return java_comments;
    }

    public void addJava_comment(Java_comment java_comment) {
        this.java_comments.add(java_comment);
    }
    public java_Package getJava_package() {
        return java_package;
    }

    public void setJava_package(java_Package java_package) {
        this.java_package = java_package;
    }
    public List<java_BodyDeclaration> getJava_bodydeclarations() {
        return java_bodydeclarations;
    }

    public void addJava_bodydeclaration(Java_bodydeclaration java_bodydeclaration) {
        this.java_bodydeclarations.add(java_bodydeclaration);
    }
    public java_BodyDeclaration getJava_bodydeclaration() {
        return java_bodydeclaration;
    }

    public void setJava_bodydeclaration(java_BodyDeclaration java_bodydeclaration) {
        this.java_bodydeclaration = java_bodydeclaration;
    }
    public List<java_TypeAccess> getJava_typeaccesss() {
        return java_typeaccesss;
    }

    public void addJava_typeaccess(Java_typeaccess java_typeaccess) {
        this.java_typeaccesss.add(java_typeaccess);
    }
    public List<java_Comment> getJava_comments() {
        return java_comments;
    }

    public void addJava_comment(Java_comment java_comment) {
        this.java_comments.add(java_comment);
    }
    public java_Package getJava_package() {
        return java_package;
    }

    public void setJava_package(java_Package java_package) {
        this.java_package = java_package;
    }

}