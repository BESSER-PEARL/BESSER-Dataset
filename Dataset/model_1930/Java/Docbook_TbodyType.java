





import java.util.List;
import java.util.ArrayList;

public class Docbook_TbodyType  {






    private Docbook_DocumentRoot docbook_documentroot;




    private List<Docbook_RowType> docbook_rowtypes;


    public Docbook_TbodyType(
    ) {
        this.docbook_rowtypes = new ArrayList<>();
    }

    public Docbook_TbodyType(
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

}