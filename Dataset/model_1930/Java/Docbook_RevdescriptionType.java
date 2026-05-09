





import java.util.List;
import java.util.ArrayList;

public class Docbook_RevdescriptionType  {

    private String mixed;





    private Docbook_RevisionType docbook_revisiontype;




    private List<Docbook_ParaType> docbook_paratypes;


    public Docbook_RevdescriptionType(
        String mixed    ) {
        this.mixed = mixed;
        this.docbook_paratypes = new ArrayList<>();
    }

    public Docbook_RevdescriptionType(
        String mixed        ArrayList<Docbook_ParaType> docbook_paratypes    ) {
        this.mixed = mixed;
        this.docbook_paratypes = docbook_paratypes;
    }

    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public Docbook_RevisionType getDocbook_revisiontype() {
        return docbook_revisiontype;
    }

    public void setDocbook_revisiontype(Docbook_RevisionType docbook_revisiontype) {
        this.docbook_revisiontype = docbook_revisiontype;
    }
    public List<Docbook_ParaType> getDocbook_paratypes() {
        return docbook_paratypes;
    }

    public void addDocbook_paratype(Docbook_paratype docbook_paratype) {
        this.docbook_paratypes.add(docbook_paratype);
    }

}