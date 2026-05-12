





import java.util.List;
import java.util.ArrayList;

public class bibTeX_MonthField  {

    private String month;





    private bibTeX_BibtexEntryTypes bibtex_bibtexentrytypes;


    public bibTeX_MonthField(
        String month    ) {
        this.month = month;
    }


    public String getMonth() {
        return month;
    }

    public void setMonth(String month) {
        this.month = month;
    }

    public bibTeX_BibtexEntryTypes getBibtex_bibtexentrytypes() {
        return bibtex_bibtexentrytypes;
    }

    public void setBibtex_bibtexentrytypes(bibTeX_BibtexEntryTypes bibtex_bibtexentrytypes) {
        this.bibtex_bibtexentrytypes = bibtex_bibtexentrytypes;
    }

}