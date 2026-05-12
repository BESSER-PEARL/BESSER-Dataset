





import java.util.List;
import java.util.ArrayList;

public class sistedesMM_Book extends Publication {

    private String volume;
    private String series;
    private int year;
    private String isbn;
    private int edition;
    private String month;
    private String title;



    public sistedesMM_Book(
        String volume,        String series,        int year,        String isbn,        int edition,        String month,        String title    ) {
        super(
        );
        this.volume = volume;
        this.series = series;
        this.year = year;
        this.isbn = isbn;
        this.edition = edition;
        this.month = month;
        this.title = title;
    }


    public String getVolume() {
        return volume;
    }

    public void setVolume(String volume) {
        this.volume = volume;
    }
    public String getSeries() {
        return series;
    }

    public void setSeries(String series) {
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
    public int getEdition() {
        return edition;
    }

    public void setEdition(int edition) {
        this.edition = edition;
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


}