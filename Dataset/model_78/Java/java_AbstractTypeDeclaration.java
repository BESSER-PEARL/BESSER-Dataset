





import java.util.List;
import java.util.ArrayList;

public class java_AbstractTypeDeclaration extends BodyDeclaration, Type {






    private List<java_Comment> java_comments;




    private List<java_BodyDeclaration> java_bodydeclarations;




    private List<java_Comment> java_comments;




    private java_BodyDeclaration java_bodydeclaration;


    public java_AbstractTypeDeclaration(
    ) {
        super(
        );
        this.java_comments = new ArrayList<>();
        this.java_bodydeclarations = new ArrayList<>();
        this.java_comments = new ArrayList<>();
    }

    public java_AbstractTypeDeclaration(
        ArrayList<java_Comment> java_comments,        ArrayList<java_BodyDeclaration> java_bodydeclarations,        ArrayList<java_Comment> java_comments    ) {
        this.java_comments = java_comments;
        this.java_bodydeclarations = java_bodydeclarations;
        this.java_comments = java_comments;
    }


    public List<java_Comment> getJava_comments() {
        return java_comments;
    }

    public void addJava_comment(Java_comment java_comment) {
        this.java_comments.add(java_comment);
    }
    public List<java_BodyDeclaration> getJava_bodydeclarations() {
        return java_bodydeclarations;
    }

    public void addJava_bodydeclaration(Java_bodydeclaration java_bodydeclaration) {
        this.java_bodydeclarations.add(java_bodydeclaration);
    }
    public List<java_Comment> getJava_comments() {
        return java_comments;
    }

    public void addJava_comment(Java_comment java_comment) {
        this.java_comments.add(java_comment);
    }
    public java_BodyDeclaration getJava_bodydeclaration() {
        return java_bodydeclaration;
    }

    public void setJava_bodydeclaration(java_BodyDeclaration java_bodydeclaration) {
        this.java_bodydeclaration = java_bodydeclaration;
    }

}