





import java.util.List;
import java.util.ArrayList;

public class Docbook_ListitemType  {






    private List<Docbook_ParaType> docbook_paratypes;




    private Docbook_DocumentRoot docbook_documentroot;




    private Docbook_ItemizedlistType docbook_itemizedlisttype;




    private Docbook_ItemizedlistType docbook_itemizedlisttype;


    public Docbook_ListitemType(
    ) {
        this.docbook_paratypes = new ArrayList<>();
    }

    public Docbook_ListitemType(
        ArrayList<Docbook_ParaType> docbook_paratypes    ) {
        this.docbook_paratypes = docbook_paratypes;
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
    public Docbook_ItemizedlistType getDocbook_itemizedlisttype() {
        return docbook_itemizedlisttype;
    }

    public void setDocbook_itemizedlisttype(Docbook_ItemizedlistType docbook_itemizedlisttype) {
        this.docbook_itemizedlisttype = docbook_itemizedlisttype;
    }
    public Docbook_ItemizedlistType getDocbook_itemizedlisttype() {
        return docbook_itemizedlisttype;
    }

    public void setDocbook_itemizedlisttype(Docbook_ItemizedlistType docbook_itemizedlisttype) {
        this.docbook_itemizedlisttype = docbook_itemizedlisttype;
    }

}