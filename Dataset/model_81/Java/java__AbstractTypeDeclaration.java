





import java.util.List;
import java.util.ArrayList;

public class java__AbstractTypeDeclaration extends BodyDeclaration, Type {






    private List<java__Comment> java__comments;




    private List<java__Comment> java__comments;




    private List<java__TypeAccess> java__typeaccesss;


    public java__AbstractTypeDeclaration(
    ) {
        super(
        );
        this.java__comments = new ArrayList<>();
        this.java__comments = new ArrayList<>();
        this.java__typeaccesss = new ArrayList<>();
    }

    public java__AbstractTypeDeclaration(
        ArrayList<java__Comment> java__comments,        ArrayList<java__Comment> java__comments,        ArrayList<java__TypeAccess> java__typeaccesss    ) {
        this.java__comments = java__comments;
        this.java__comments = java__comments;
        this.java__typeaccesss = java__typeaccesss;
    }


    public List<java__Comment> getJava__comments() {
        return java__comments;
    }

    public void addJava__comment(Java__comment java__comment) {
        this.java__comments.add(java__comment);
    }
    public List<java__Comment> getJava__comments() {
        return java__comments;
    }

    public void addJava__comment(Java__comment java__comment) {
        this.java__comments.add(java__comment);
    }
    public List<java__TypeAccess> getJava__typeaccesss() {
        return java__typeaccesss;
    }

    public void addJava__typeaccess(Java__typeaccess java__typeaccess) {
        this.java__typeaccesss.add(java__typeaccess);
    }

}