





import java.util.List;
import java.util.ArrayList;

public class Docbook_TheadType  {






    private Docbook_DocumentRoot docbook_documentroot;




    private List<Docbook_RowType> docbook_rowtypes;




    private Docbook_TgroupType docbook_tgrouptype;


    public Docbook_TheadType(
    ) {
        this.docbook_rowtypes = new ArrayList<>();
    }

    public Docbook_TheadType(
        ArrayList<Docbook_RowType> docbook_rowtypes    ) {
        this.docbook_rowtypes = docbook_rowtypes;
    }


    public Docbook_DocumentRoot getDocbook_documentroot() {
        return docbook_documentroot;
    }

    public void setDocbook_documentroot(Docbook_DocumentRoot docbook_documentroot) {
        this.docbook_documentroot = docbook_documentroot;
    }
    public List<Docbook_RowType> getDocbook_rowtypes() {
        return docbook_rowtypes;
    }

    public void addDocbook_rowtype(Docbook_rowtype docbook_rowtype) {
        this.docbook_rowtypes.add(docbook_rowtype);
    }
    public Docbook_TgroupType getDocbook_tgrouptype() {
        return docbook_tgrouptype;
    }

    public void setDocbook_tgrouptype(Docbook_TgroupType docbook_tgrouptype) {
        this.docbook_tgrouptype = docbook_tgrouptype;
    }

}