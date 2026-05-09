





import java.util.List;
import java.util.ArrayList;

public class Docbook_UlinkType  {

    private String url;
    private String type;
    private String mixed;





    private Docbook_NoteType docbook_notetype;




    private Docbook_ParaType docbook_paratype;




    private Docbook_ImportantType docbook_importanttype;




    private List<Docbook_EmphasisType> docbook_emphasistypes;




    private Docbook_TipType docbook_tiptype;




    private Docbook_DocumentRoot docbook_documentroot;




    private Docbook_OtheraddrType docbook_otheraddrtype;


    public Docbook_UlinkType(
        String url,        String type,        String mixed    ) {
        this.url = url;
        this.type = type;
        this.mixed = mixed;
        this.docbook_emphasistypes = new ArrayList<>();
    }

    public Docbook_UlinkType(
        String url,        String type,        String mixed        ArrayList<Docbook_EmphasisType> docbook_emphasistypes    ) {
        this.url = url;
        this.type = type;
        this.mixed = mixed;
        this.docbook_emphasistypes = docbook_emphasistypes;
    }

    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public Docbook_NoteType getDocbook_notetype() {
        return docbook_notetype;
    }

    public void setDocbook_notetype(Docbook_NoteType docbook_notetype) {
        this.docbook_notetype = docbook_notetype;
    }
    public Docbook_ParaType getDocbook_paratype() {
        return docbook_paratype;
    }

    public void setDocbook_paratype(Docbook_ParaType docbook_paratype) {
        this.docbook_paratype = docbook_paratype;
    }
    public Docbook_ImportantType getDocbook_importanttype() {
        return docbook_importanttype;
    }

    public void setDocbook_importanttype(Docbook_ImportantType docbook_importanttype) {
        this.docbook_importanttype = docbook_importanttype;
    }
    public List<Docbook_EmphasisType> getDocbook_emphasistypes() {
        return docbook_emphasistypes;
    }

    public void addDocbook_emphasistype(Docbook_emphasistype docbook_emphasistype) {
        this.docbook_emphasistypes.add(docbook_emphasistype);
    }
    public Docbook_TipType getDocbook_tiptype() {
        return docbook_tiptype;
    }

    public void setDocbook_tiptype(Docbook_TipType docbook_tiptype) {
        this.docbook_tiptype = docbook_tiptype;
    }
    public Docbook_DocumentRoot getDocbook_documentroot() {
        return docbook_documentroot;
    }

    public void setDocbook_documentroot(Docbook_DocumentRoot docbook_documentroot) {
        this.docbook_documentroot = docbook_documentroot;
    }
    public Docbook_OtheraddrType getDocbook_otheraddrtype() {
        return docbook_otheraddrtype;
    }

    public void setDocbook_otheraddrtype(Docbook_OtheraddrType docbook_otheraddrtype) {
        this.docbook_otheraddrtype = docbook_otheraddrtype;
    }

}