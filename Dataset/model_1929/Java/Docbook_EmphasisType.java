





import java.util.List;
import java.util.ArrayList;

public class Docbook_EmphasisType  {

    private String mixed;
    private String role;





    private Docbook_TitleType docbook_titletype;




    private Docbook_ParaType docbook_paratype;




    private Docbook_EmphasisType docbook_emphasistype;




    private Docbook_DocumentRoot docbook_documentroot;


    public Docbook_EmphasisType(
        String mixed,        String role    ) {
        this.mixed = mixed;
        this.role = role;
    }


    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getRole() {
        return role;
    }

    public void setRole(String role) {
        this.role = role;
    }

    public Docbook_TitleType getDocbook_titletype() {
        return docbook_titletype;
    }

    public void setDocbook_titletype(Docbook_TitleType docbook_titletype) {
        this.docbook_titletype = docbook_titletype;
    }
    public Docbook_ParaType getDocbook_paratype() {
        return docbook_paratype;
    }

    public void setDocbook_paratype(Docbook_ParaType docbook_paratype) {
        this.docbook_paratype = docbook_paratype;
    }
    public Docbook_EmphasisType getDocbook_emphasistype() {
        return docbook_emphasistype;
    }

    public void setDocbook_emphasistype(Docbook_EmphasisType docbook_emphasistype) {
        this.docbook_emphasistype = docbook_emphasistype;
    }
    public Docbook_DocumentRoot getDocbook_documentroot() {
        return docbook_documentroot;
    }

    public void setDocbook_documentroot(Docbook_DocumentRoot docbook_documentroot) {
        this.docbook_documentroot = docbook_documentroot;
    }

}