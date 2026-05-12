





import java.util.List;
import java.util.ArrayList;

public class BIBTEXML_DatedEntry extends Entry {

    private String year;
    private String month;



    public BIBTEXML_DatedEntry(
        String year,        String month    ) {
        super(
        );
        this.year = year;
        this.month = month;
    }


    public String getYear() {
        return year;
    }

    public void setYear(String year) {
        this.year = year;
    }
    public String getMonth() {
        return month;
    }

    public void setMonth(String month) {
        this.month = month;
    }


}