





import java.util.List;
import java.util.ArrayList;

public class DBLP_Book extends Record {

    private String month;
    private String series;
    private int edition;
    private String title;
    private int volume;
    private String isbn;
    private int year;



    public DBLP_Book(
        String month,        String series,        int edition,        String title,        int volume,        String isbn,        int year    ) {
        super(
        );
        this.month = month;
        this.series = series;
        this.edition = edition;
        this.title = title;
        this.volume = volume;
        this.isbn = isbn;
        this.year = year;
    }


    public String getMonth() {
        return month;
    }

    public void setMonth(String month) {
        this.month = month;
    }
    public String getSeries() {
        return series;
    }

    public void setSeries(String series) {
        this.series = series;
    }
    public int getEdition() {
        return edition;
    }

    public void setEdition(int edition) {
        this.edition = edition;
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
    public String getIsbn() {
        return isbn;
    }

    public void setIsbn(String isbn) {
        this.isbn = isbn;
    }
    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }


}