





import java.util.List;
import java.util.ArrayList;

public class java_AbstractTypeDeclaration extends BodyDeclaration, Type {






    private List<java_Comment> java_comments;




    private List<java_Comment> java_comments;




    private List<java_TypeAccess> java_typeaccesss;


    public java_AbstractTypeDeclaration(
    ) {
        super(
        );
        this.java_comments = new ArrayList<>();
        this.java_comments = new ArrayList<>();
        this.java_typeaccesss = new ArrayList<>();
    }

    public java_AbstractTypeDeclaration(
        ArrayList<java_Comment> java_comments,        ArrayList<java_Comment> java_comments,        ArrayList<java_TypeAccess> java_typeaccesss    ) {
        this.java_comments = java_comments;
        this.java_comments = java_comments;
        this.java_typeaccesss = java_typeaccesss;
    }


    public List<java_Comment> getJava_comments() {
        return java_comments;
    }

    public void addJava_comment(Java_comment java_comment) {
        this.java_comments.add(java_comment);
    }
    public List<java_Comment> getJava_comments() {
        return java_comments;
    }

    public void addJava_comment(Java_comment java_comment) {
        this.java_comments.add(java_comment);
    }
    public List<java_TypeAccess> getJava_typeaccesss() {
        return java_typeaccesss;
    }

    public void addJava_typeaccess(Java_typeaccess java_typeaccess) {
        this.java_typeaccesss.add(java_typeaccess);
    }

}