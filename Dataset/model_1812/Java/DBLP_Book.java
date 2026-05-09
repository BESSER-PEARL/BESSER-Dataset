





import java.util.List;
import java.util.ArrayList;

public class DBLP_Book extends Record {

    private int volume;
    private String series;
    private String isbn;
    private int edition;
    private String title;
    private String month;
    private int year;



    public DBLP_Book(
        int volume,        String series,        String isbn,        int edition,        String title,        String month,        int year    ) {
        super(
        );
        this.volume = volume;
        this.series = series;
        this.isbn = isbn;
        this.edition = edition;
        this.title = title;
        this.month = month;
        this.year = year;
    }


    public int getVolume() {
        return volume;
    }

    public void setVolume(int volume) {
        this.volume = volume;
    }
    public String getSeries() {
        return series;
    }

    public void setSeries(String series) {
        this.series = series;
    }
    public String getIsbn() {
        return isbn;
    }

    public void setIsbn(String isbn) {
        this.isbn = isbn;
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
    public String getMonth() {
        return month;
    }

    public void setMonth(String month) {
        this.month = month;
    }
    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }


}