





import java.util.List;
import java.util.ArrayList;

public class javaMM_ASTNode  {






    private javaMM_TagElement javamm_tagelement;




    private List<javaMM_Comment> javamm_comments;


    public javaMM_ASTNode(
    ) {
        this.javamm_comments = new ArrayList<>();
    }

    public javaMM_ASTNode(
        ArrayList<javaMM_Comment> javamm_comments    ) {
        this.javamm_comments = javamm_comments;
    }


    public javaMM_TagElement getJavamm_tagelement() {
        return javamm_tagelement;
    }

    public void setJavamm_tagelement(javaMM_TagElement javamm_tagelement) {
        this.javamm_tagelement = javamm_tagelement;
    }
    public List<javaMM_Comment> getJavamm_comments() {
        return javamm_comments;
    }

    public void addJavamm_comment(Javamm_comment javamm_comment) {
        this.javamm_comments.add(javamm_comment);
    }

}