





import java.util.List;
import java.util.ArrayList;

public class bibtexml_FileType  {






    private List<bibtexml_BibTeXMLEntryType> bibtexml_bibtexmlentrytypes;




    private bibtexml_DocumentRoot bibtexml_documentroot;


    public bibtexml_FileType(
    ) {
        this.bibtexml_bibtexmlentrytypes = new ArrayList<>();
    }

    public bibtexml_FileType(
        ArrayList<bibtexml_BibTeXMLEntryType> bibtexml_bibtexmlentrytypes    ) {
        this.bibtexml_bibtexmlentrytypes = bibtexml_bibtexmlentrytypes;
    }


    public List<bibtexml_BibTeXMLEntryType> getBibtexml_bibtexmlentrytypes() {
        return bibtexml_bibtexmlentrytypes;
    }

    public void addBibtexml_bibtexmlentrytype(Bibtexml_bibtexmlentrytype bibtexml_bibtexmlentrytype) {
        this.bibtexml_bibtexmlentrytypes.add(bibtexml_bibtexmlentrytype);
    }
    public bibtexml_DocumentRoot getBibtexml_documentroot() {
        return bibtexml_documentroot;
    }

    public void setBibtexml_documentroot(bibtexml_DocumentRoot bibtexml_documentroot) {
        this.bibtexml_documentroot = bibtexml_documentroot;
    }

}