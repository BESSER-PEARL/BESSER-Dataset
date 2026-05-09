





import java.util.List;
import java.util.ArrayList;

public class Docbook_ImportantType  {

    private String group;
    private String mixed;





    private Docbook_DocumentRoot docbook_documentroot;




    private Docbook_PrefaceType docbook_prefacetype;




    private List<Docbook_EmphasisType> docbook_emphasistypes;


    public Docbook_ImportantType(
        String group,        String mixed    ) {
        this.group = group;
        this.mixed = mixed;
        this.docbook_emphasistypes = new ArrayList<>();
    }

    public Docbook_ImportantType(
        String group,        String mixed        ArrayList<Docbook_EmphasisType> docbook_emphasistypes    ) {
        this.group = group;
        this.mixed = mixed;
        this.docbook_emphasistypes = docbook_emphasistypes;
    }

    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public Docbook_DocumentRoot getDocbook_documentroot() {
        return docbook_documentroot;
    }

    public void setDocbook_documentroot(Docbook_DocumentRoot docbook_documentroot) {
        this.docbook_documentroot = docbook_documentroot;
    }
    public Docbook_PrefaceType getDocbook_prefacetype() {
        return docbook_prefacetype;
    }

    public void setDocbook_prefacetype(Docbook_PrefaceType docbook_prefacetype) {
        this.docbook_prefacetype = docbook_prefacetype;
    }
    public List<Docbook_EmphasisType> getDocbook_emphasistypes() {
        return docbook_emphasistypes;
    }

    public void addDocbook_emphasistype(Docbook_emphasistype docbook_emphasistype) {
        this.docbook_emphasistypes.add(docbook_emphasistype);
    }

}