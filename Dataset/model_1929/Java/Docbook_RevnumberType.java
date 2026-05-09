





import java.util.List;
import java.util.ArrayList;

public class Docbook_RevnumberType  {

    private String mixed;





    private Docbook_RevisionType docbook_revisiontype;




    private List<Docbook_UlinkType> docbook_ulinktypes;


    public Docbook_RevnumberType(
        String mixed    ) {
        this.mixed = mixed;
        this.docbook_ulinktypes = new ArrayList<>();
    }

    public Docbook_RevnumberType(
        String mixed        ArrayList<Docbook_UlinkType> docbook_ulinktypes    ) {
        this.mixed = mixed;
        this.docbook_ulinktypes = docbook_ulinktypes;
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
    public List<Docbook_UlinkType> getDocbook_ulinktypes() {
        return docbook_ulinktypes;
    }

    public void addDocbook_ulinktype(Docbook_ulinktype docbook_ulinktype) {
        this.docbook_ulinktypes.add(docbook_ulinktype);
    }

}