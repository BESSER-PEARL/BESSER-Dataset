





import java.util.List;
import java.util.ArrayList;

public class javaMM_AbstractTypeDeclaration extends Type, BodyDeclaration {






    private List<javaMM_Comment> javamm_comments;




    private javaMM_TypeDeclarationStatement javamm_typedeclarationstatement;




    private List<javaMM_TypeAccess> javamm_typeaccesss;




    private List<javaMM_Comment> javamm_comments;


    public javaMM_AbstractTypeDeclaration(
    ) {
        super(
        );
        this.javamm_comments = new ArrayList<>();
        this.javamm_typeaccesss = new ArrayList<>();
        this.javamm_comments = new ArrayList<>();
    }

    public javaMM_AbstractTypeDeclaration(
        ArrayList<javaMM_Comment> javamm_comments,        ArrayList<javaMM_TypeAccess> javamm_typeaccesss,        ArrayList<javaMM_Comment> javamm_comments    ) {
        this.javamm_comments = javamm_comments;
        this.javamm_typeaccesss = javamm_typeaccesss;
        this.javamm_comments = javamm_comments;
    }


    public List<javaMM_Comment> getJavamm_comments() {
        return javamm_comments;
    }

    public void addJavamm_comment(Javamm_comment javamm_comment) {
        this.javamm_comments.add(javamm_comment);
    }
    public javaMM_TypeDeclarationStatement getJavamm_typedeclarationstatement() {
        return javamm_typedeclarationstatement;
    }

    public void setJavamm_typedeclarationstatement(javaMM_TypeDeclarationStatement javamm_typedeclarationstatement) {
        this.javamm_typedeclarationstatement = javamm_typedeclarationstatement;
    }
    public List<javaMM_TypeAccess> getJavamm_typeaccesss() {
        return javamm_typeaccesss;
    }

    public void addJavamm_typeaccess(Javamm_typeaccess javamm_typeaccess) {
        this.javamm_typeaccesss.add(javamm_typeaccess);
    }
    public List<javaMM_Comment> getJavamm_comments() {
        return javamm_comments;
    }

    public void addJavamm_comment(Javamm_comment javamm_comment) {
        this.javamm_comments.add(javamm_comment);
    }

}