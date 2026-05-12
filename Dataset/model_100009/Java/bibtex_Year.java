





import java.util.List;
import java.util.ArrayList;

public class bibtex_Year  {

    private String year;





    private bibtex_BibType bibtex_bibtype;


    public bibtex_Year(
        String year    ) {
        this.year = year;
    }


    public String getYear() {
        return year;
    }

    public void setYear(String year) {
        this.year = year;
    }

    public bibtex_BibType getBibtex_bibtype() {
        return bibtex_bibtype;
    }

    public void setBibtex_bibtype(bibtex_BibType bibtex_bibtype) {
        this.bibtex_bibtype = bibtex_bibtype;
    }

}