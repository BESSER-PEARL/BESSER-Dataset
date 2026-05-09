





import java.util.List;
import java.util.ArrayList;

public class sistedesMM_Book extends Publication {

    private String title;
    private String series;
    private String isbn;
    private String month;
    private String volume;
    private int edition;
    private int year;





    private sistedesMM_Publisher sistedesmm_publisher;


    public sistedesMM_Book(
        String title,        String series,        String isbn,        String month,        String volume,        int edition,        int year    ) {
        super(
        );
        this.title = title;
        this.series = series;
        this.isbn = isbn;
        this.month = month;
        this.volume = volume;
        this.edition = edition;
        this.year = year;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
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
    public String getMonth() {
        return month;
    }

    public void setMonth(String month) {
        this.month = month;
    }
    public String getVolume() {
        return volume;
    }

    public void setVolume(String volume) {
        this.volume = volume;
    }
    public int getEdition() {
        return edition;
    }

    public void setEdition(int edition) {
        this.edition = edition;
    }
    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }

    public sistedesMM_Publisher getSistedesmm_publisher() {
        return sistedesmm_publisher;
    }

    public void setSistedesmm_publisher(sistedesMM_Publisher sistedesmm_publisher) {
        this.sistedesmm_publisher = sistedesmm_publisher;
    }

}