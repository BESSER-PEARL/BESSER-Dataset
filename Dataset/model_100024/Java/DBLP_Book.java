





import java.util.List;
import java.util.ArrayList;

public class DBLP_Book extends Record {

    private int year;
    private String isbn;
    private String month;
    private String title;
    private int volume;
    private int edition;
    private String series;





    private DBLP_Publisher dblp_publisher;


    public DBLP_Book(
        int year,        String isbn,        String month,        String title,        int volume,        int edition,        String series    ) {
        super(
        );
        this.year = year;
        this.isbn = isbn;
        this.month = month;
        this.title = title;
        this.volume = volume;
        this.edition = edition;
        this.series = series;
    }


    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }
    public String getIsbn() {
        return isbn;
    }

    public void setIsbn(String isbn) {
        this.isbn = isbn;
    }
    public String getMonth() {
        return month;
    }

    public void setMonth(String month) {
        this.month = month;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public int getVolume() {
        return volume;
    }

    public void setVolume(int volume) {
        this.volume = volume;
    }
    public int getEdition() {
        return edition;
    }

    public void setEdition(int edition) {
        this.edition = edition;
    }
    public String getSeries() {
        return series;
    }

    public void setSeries(String series) {
        this.series = series;
    }

    public DBLP_Publisher getDblp_publisher() {
        return dblp_publisher;
    }

    public void setDblp_publisher(DBLP_Publisher dblp_publisher) {
        this.dblp_publisher = dblp_publisher;
    }

}