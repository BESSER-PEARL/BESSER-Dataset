





import java.util.List;
import java.util.ArrayList;

public class Docbook_RowType  {






    private Docbook_DocumentRoot docbook_documentroot;




    private List<Docbook_EntryType> docbook_entrytypes;


    public Docbook_RowType(
    ) {
        this.docbook_entrytypes = new ArrayList<>();
    }

    public Docbook_RowType(
        ArrayList<Docbook_EntryType> docbook_entrytypes    ) {
        this.docbook_entrytypes = docbook_entrytypes;
    }


    public Docbook_DocumentRoot getDocbook_documentroot() {
        return docbook_documentroot;
    }

    public void setDocbook_documentroot(Docbook_DocumentRoot docbook_documentroot) {
        this.docbook_documentroot = docbook_documentroot;
    }
    public List<Docbook_EntryType> getDocbook_entrytypes() {
        return docbook_entrytypes;
    }

    public void addDocbook_entrytype(Docbook_entrytype docbook_entrytype) {
        this.docbook_entrytypes.add(docbook_entrytype);
    }

}