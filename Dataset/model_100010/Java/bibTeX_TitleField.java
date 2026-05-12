





import java.util.List;
import java.util.ArrayList;

public class bibTeX_TitleField  {

    private String title;





    private bibTeX_BibtexEntryTypes bibtex_bibtexentrytypes;


    public bibTeX_TitleField(
        String title    ) {
        this.title = title;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public bibTeX_BibtexEntryTypes getBibtex_bibtexentrytypes() {
        return bibtex_bibtexentrytypes;
    }

    public void setBibtex_bibtexentrytypes(bibTeX_BibtexEntryTypes bibtex_bibtexentrytypes) {
        this.bibtex_bibtexentrytypes = bibtex_bibtexentrytypes;
    }

}