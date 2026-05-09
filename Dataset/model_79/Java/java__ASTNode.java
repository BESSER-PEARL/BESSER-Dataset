





import java.util.List;
import java.util.ArrayList;

public class java__ASTNode  {






    private java__TagElement java__tagelement;




    private List<java__Comment> java__comments;




    private java__UnresolvedItemAccess java__unresolveditemaccess;


    public java__ASTNode(
    ) {
        this.java__comments = new ArrayList<>();
    }

    public java__ASTNode(
        ArrayList<java__Comment> java__comments    ) {
        this.java__comments = java__comments;
    }


    public java__TagElement getJava__tagelement() {
        return java__tagelement;
    }

    public void setJava__tagelement(java__TagElement java__tagelement) {
        this.java__tagelement = java__tagelement;
    }
    public List<java__Comment> getJava__comments() {
        return java__comments;
    }

    public void addJava__comment(Java__comment java__comment) {
        this.java__comments.add(java__comment);
    }
    public java__UnresolvedItemAccess getJava__unresolveditemaccess() {
        return java__unresolveditemaccess;
    }

    public void setJava__unresolveditemaccess(java__UnresolvedItemAccess java__unresolveditemaccess) {
        this.java__unresolveditemaccess = java__unresolveditemaccess;
    }

}