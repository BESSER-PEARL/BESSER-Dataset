





import java.util.List;
import java.util.ArrayList;

public class SecCon_Element  {






    private SecCon_Comment seccon_comment;




    private List<SecCon_Comment> seccon_comments;


    public SecCon_Element(
    ) {
        this.seccon_comments = new ArrayList<>();
    }

    public SecCon_Element(
        ArrayList<SecCon_Comment> seccon_comments    ) {
        this.seccon_comments = seccon_comments;
    }


    public SecCon_Comment getSeccon_comment() {
        return seccon_comment;
    }

    public void setSeccon_comment(SecCon_Comment seccon_comment) {
        this.seccon_comment = seccon_comment;
    }
    public List<SecCon_Comment> getSeccon_comments() {
        return seccon_comments;
    }

    public void addSeccon_comment(Seccon_comment seccon_comment) {
        this.seccon_comments.add(seccon_comment);
    }

}