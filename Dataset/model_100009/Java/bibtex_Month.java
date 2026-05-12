





import java.util.List;
import java.util.ArrayList;

public class bibtex_Month  {

    private String month;





    private bibtex_BibType bibtex_bibtype;


    public bibtex_Month(
        String month    ) {
        this.month = month;
    }


    public String getMonth() {
        return month;
    }

    public void setMonth(String month) {
        this.month = month;
    }

    public bibtex_BibType getBibtex_bibtype() {
        return bibtex_bibtype;
    }

    public void setBibtex_bibtype(bibtex_BibType bibtex_bibtype) {
        this.bibtex_bibtype = bibtex_bibtype;
    }

}