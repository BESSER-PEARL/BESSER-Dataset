





import java.util.List;
import java.util.ArrayList;

public class java_ASTNode  {






    private List<java_Comment> java_comments;




    private java_TagElement java_tagelement;


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
    public java_TagElement getJava_tagelement() {
        return java_tagelement;
    }

    public void setJava_tagelement(java_TagElement java_tagelement) {
        this.java_tagelement = java_tagelement;
    }

}