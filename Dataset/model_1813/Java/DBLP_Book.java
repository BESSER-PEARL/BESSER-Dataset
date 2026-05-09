





import java.util.List;
import java.util.ArrayList;

public class DBLP_Book extends Record {

    private int year;
    private String isbn;
    private int volume;
    private String series;
    private String month;
    private String title;
    private int edition;



    public DBLP_Book(
        int year,        String isbn,        int volume,        String series,        String month,        String title,        int edition    ) {
        super(
        );
        this.year = year;
        this.isbn = isbn;
        this.volume = volume;
        this.series = series;
        this.month = month;
        this.title = title;
        this.edition = edition;
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
    public int getEdition() {
        return edition;
    }

    public void setEdition(int edition) {
        this.edition = edition;
    }


}