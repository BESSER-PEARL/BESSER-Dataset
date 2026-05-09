





import java.util.List;
import java.util.ArrayList;

public class Docbook_RefSynopsisDivType  {






    private List<Docbook_FuncsynopsisType> docbook_funcsynopsistypes;




    private Docbook_RefEntryType docbook_refentrytype;




    private List<Docbook_CmdsynopsisType> docbook_cmdsynopsistypes;


    public Docbook_RefSynopsisDivType(
    ) {
        this.docbook_funcsynopsistypes = new ArrayList<>();
        this.docbook_cmdsynopsistypes = new ArrayList<>();
    }

    public Docbook_RefSynopsisDivType(
        ArrayList<Docbook_FuncsynopsisType> docbook_funcsynopsistypes,        ArrayList<Docbook_CmdsynopsisType> docbook_cmdsynopsistypes    ) {
        this.docbook_funcsynopsistypes = docbook_funcsynopsistypes;
        this.docbook_cmdsynopsistypes = docbook_cmdsynopsistypes;
    }


    public List<Docbook_FuncsynopsisType> getDocbook_funcsynopsistypes() {
        return docbook_funcsynopsistypes;
    }

    public void addDocbook_funcsynopsistype(Docbook_funcsynopsistype docbook_funcsynopsistype) {
        this.docbook_funcsynopsistypes.add(docbook_funcsynopsistype);
    }
    public Docbook_RefEntryType getDocbook_refentrytype() {
        return docbook_refentrytype;
    }

    public void setDocbook_refentrytype(Docbook_RefEntryType docbook_refentrytype) {
        this.docbook_refentrytype = docbook_refentrytype;
    }
    public List<Docbook_CmdsynopsisType> getDocbook_cmdsynopsistypes() {
        return docbook_cmdsynopsistypes;
    }

    public void addDocbook_cmdsynopsistype(Docbook_cmdsynopsistype docbook_cmdsynopsistype) {
        this.docbook_cmdsynopsistypes.add(docbook_cmdsynopsistype);
    }

}