





import java.util.List;
import java.util.ArrayList;

public class Docbook_EntryType  {

    private String nameend;
    private String morerows;
    private String namest;
    private String align;
    private String valign;
    private String mixed;





    private List<Docbook_ParaType> docbook_paratypes;




    private Docbook_DocumentRoot docbook_documentroot;


    public Docbook_EntryType(
        String nameend,        String morerows,        String namest,        String align,        String valign,        String mixed    ) {
        this.nameend = nameend;
        this.morerows = morerows;
        this.namest = namest;
        this.align = align;
        this.valign = valign;
        this.mixed = mixed;
        this.docbook_paratypes = new ArrayList<>();
    }

    public Docbook_EntryType(
        String nameend,        String morerows,        String namest,        String align,        String valign,        String mixed        ArrayList<Docbook_ParaType> docbook_paratypes    ) {
        this.nameend = nameend;
        this.morerows = morerows;
        this.namest = namest;
        this.align = align;
        this.valign = valign;
        this.mixed = mixed;
        this.docbook_paratypes = docbook_paratypes;
    }

    public String getNameend() {
        return nameend;
    }

    public void setNameend(String nameend) {
        this.nameend = nameend;
    }
    public String getMorerows() {
        return morerows;
    }

    public void setMorerows(String morerows) {
        this.morerows = morerows;
    }
    public String getNamest() {
        return namest;
    }

    public void setNamest(String namest) {
        this.namest = namest;
    }
    public String getAlign() {
        return align;
    }

    public void setAlign(String align) {
        this.align = align;
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

    public List<Docbook_ParaType> getDocbook_paratypes() {
        return docbook_paratypes;
    }

    public void addDocbook_paratype(Docbook_paratype docbook_paratype) {
        this.docbook_paratypes.add(docbook_paratype);
    }
    public Docbook_DocumentRoot getDocbook_documentroot() {
        return docbook_documentroot;
    }

    public void setDocbook_documentroot(Docbook_DocumentRoot docbook_documentroot) {
        this.docbook_documentroot = docbook_documentroot;
    }

}