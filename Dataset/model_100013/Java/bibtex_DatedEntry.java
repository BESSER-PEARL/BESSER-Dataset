





import java.util.List;
import java.util.ArrayList;

public class bibtex_DatedEntry extends BibTeXEntry {

    private String year;



    public bibtex_DatedEntry(
        String year    ) {
        super(
        );
        this.year = year;
    }


    public String getYear() {
        return year;
    }

    public void setYear(String year) {
        this.year = year;
    }


}