





import java.util.List;
import java.util.ArrayList;

public class java_AbstractTypeDeclaration extends Type, BodyDeclaration {






    private java_Package java_package;




    private List<java_TypeAccess> java_typeaccesss;




    private List<java_Comment> java_comments;




    private java_TypeDeclarationStatement java_typedeclarationstatement;




    private List<java_Comment> java_comments;


    public java_AbstractTypeDeclaration(
    ) {
        super(
        );
        this.java_typeaccesss = new ArrayList<>();
        this.java_comments = new ArrayList<>();
        this.java_comments = new ArrayList<>();
    }

    public java_AbstractTypeDeclaration(
        ArrayList<java_TypeAccess> java_typeaccesss,        ArrayList<java_Comment> java_comments,        ArrayList<java_Comment> java_comments    ) {
        this.java_typeaccesss = java_typeaccesss;
        this.java_comments = java_comments;
        this.java_comments = java_comments;
    }


    public java_Package getJava_package() {
        return java_package;
    }

    public void setJava_package(java_Package java_package) {
        this.java_package = java_package;
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
    public java_TypeDeclarationStatement getJava_typedeclarationstatement() {
        return java_typedeclarationstatement;
    }

    public void setJava_typedeclarationstatement(java_TypeDeclarationStatement java_typedeclarationstatement) {
        this.java_typedeclarationstatement = java_typedeclarationstatement;
    }
    public List<java_Comment> getJava_comments() {
        return java_comments;
    }

    public void addJava_comment(Java_comment java_comment) {
        this.java_comments.add(java_comment);
    }

}