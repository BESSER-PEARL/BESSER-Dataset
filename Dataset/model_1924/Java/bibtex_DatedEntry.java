





import java.util.List;
import java.util.ArrayList;

public class bibtex_DatedEntry extends BibTeXEntry {

    private int year;



    public bibtex_DatedEntry(
        int year    ) {
        super(
        );
        this.year = year;
    }


    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }


}