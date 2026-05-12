





import java.util.List;
import java.util.ArrayList;

public class bibTeX_SeriesField  {

    private String series;





    private bibTeX_Book bibtex_book;


    public bibTeX_SeriesField(
        String series    ) {
        this.series = series;
    }


    public String getSeries() {
        return series;
    }

    public void setSeries(String series) {
        this.series = series;
    }

    public bibTeX_Book getBibtex_book() {
        return bibtex_book;
    }

    public void setBibtex_book(bibTeX_Book bibtex_book) {
        this.bibtex_book = bibtex_book;
    }

}