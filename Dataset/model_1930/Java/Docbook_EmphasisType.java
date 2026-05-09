





import java.util.List;
import java.util.ArrayList;

public class Docbook_EmphasisType  {

    private String role;
    private String mixed;





    private Docbook_TitleType docbook_titletype;




    private Docbook_DocumentRoot docbook_documentroot;




    private Docbook_ParaType docbook_paratype;




    private List<Docbook_EmphasisType> docbook_emphasistypes;


    public Docbook_EmphasisType(
        String role,        String mixed    ) {
        this.role = role;
        this.mixed = mixed;
        this.docbook_emphasistypes = new ArrayList<>();
    }

    public Docbook_EmphasisType(
        String role,        String mixed        ArrayList<Docbook_EmphasisType> docbook_emphasistypes    ) {
        this.role = role;
        this.mixed = mixed;
        this.docbook_emphasistypes = docbook_emphasistypes;
    }

    public String getRole() {
        return role;
    }

    public void setRole(String role) {
        this.role = role;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public Docbook_TitleType getDocbook_titletype() {
        return docbook_titletype;
    }

    public void setDocbook_titletype(Docbook_TitleType docbook_titletype) {
        this.docbook_titletype = docbook_titletype;
    }
    public Docbook_DocumentRoot getDocbook_documentroot() {
        return docbook_documentroot;
    }

    public void setDocbook_documentroot(Docbook_DocumentRoot docbook_documentroot) {
        this.docbook_documentroot = docbook_documentroot;
    }
    public Docbook_ParaType getDocbook_paratype() {
        return docbook_paratype;
    }

    public void setDocbook_paratype(Docbook_ParaType docbook_paratype) {
        this.docbook_paratype = docbook_paratype;
    }
    public List<Docbook_EmphasisType> getDocbook_emphasistypes() {
        return docbook_emphasistypes;
    }

    public void addDocbook_emphasistype(Docbook_emphasistype docbook_emphasistype) {
        this.docbook_emphasistypes.add(docbook_emphasistype);
    }

}