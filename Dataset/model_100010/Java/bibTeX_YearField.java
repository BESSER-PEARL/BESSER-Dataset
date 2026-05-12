





import java.util.List;
import java.util.ArrayList;

public class bibTeX_YearField  {

    private String year;





    private bibTeX_BibtexEntryTypes bibtex_bibtexentrytypes;


    public bibTeX_YearField(
        String year    ) {
        this.year = year;
    }


    public String getYear() {
        return year;
    }

    public void setYear(String year) {
        this.year = year;
    }

    public bibTeX_BibtexEntryTypes getBibtex_bibtexentrytypes() {
        return bibtex_bibtexentrytypes;
    }

    public void setBibtex_bibtexentrytypes(bibTeX_BibtexEntryTypes bibtex_bibtexentrytypes) {
        this.bibtex_bibtexentrytypes = bibtex_bibtexentrytypes;
    }

}