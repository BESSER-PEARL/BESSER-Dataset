





import java.util.List;
import java.util.ArrayList;

public class Docbook_EntryType  {

    private String nameend;
    private String valign;
    private String mixed;
    private String morerows;
    private String align;
    private String namest;





    private Docbook_DocumentRoot docbook_documentroot;




    private List<Docbook_ParaType> docbook_paratypes;


    public Docbook_EntryType(
        String nameend,        String valign,        String mixed,        String morerows,        String align,        String namest    ) {
        this.nameend = nameend;
        this.valign = valign;
        this.mixed = mixed;
        this.morerows = morerows;
        this.align = align;
        this.namest = namest;
        this.docbook_paratypes = new ArrayList<>();
    }

    public Docbook_EntryType(
        String nameend,        String valign,        String mixed,        String morerows,        String align,        String namest        ArrayList<Docbook_ParaType> docbook_paratypes    ) {
        this.nameend = nameend;
        this.valign = valign;
        this.mixed = mixed;
        this.morerows = morerows;
        this.align = align;
        this.namest = namest;
        this.docbook_paratypes = docbook_paratypes;
    }

    public String getNameend() {
        return nameend;
    }

    public void setNameend(String nameend) {
        this.nameend = nameend;
    }
    public String getValign() {
        return valign;
    }

    public void setValign(String valign) {
        this.valign = valign;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getMorerows() {
        return morerows;
    }

    public void setMorerows(String morerows) {
        this.morerows = morerows;
    }
    public String getAlign() {
        return align;
    }

    public void setAlign(String align) {
        this.align = align;
    }
    public String getNamest() {
        return namest;
    }

    public void setNamest(String namest) {
        this.namest = namest;
    }

    public Docbook_DocumentRoot getDocbook_documentroot() {
        return docbook_documentroot;
    }

    public void setDocbook_documentroot(Docbook_DocumentRoot docbook_documentroot) {
        this.docbook_documentroot = docbook_documentroot;
    }
    public List<Docbook_ParaType> getDocbook_paratypes() {
        return docbook_paratypes;
    }

    public void addDocbook_paratype(Docbook_paratype docbook_paratype) {
        this.docbook_paratypes.add(docbook_paratype);
    }

}