





import java.util.List;
import java.util.ArrayList;

public class bibTeX_DatedEntry extends BibTeXEntry {

    private String year;



    public bibTeX_DatedEntry(
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