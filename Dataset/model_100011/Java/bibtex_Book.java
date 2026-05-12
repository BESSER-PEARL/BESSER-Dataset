





import java.util.List;
import java.util.ArrayList;

public class bibtex_Book extends DatedEntry, Entries, MonthEntry, AuthoredEntry {

    private int volume;
    private int edition;
    private int series;
    private String address;
    private String publisher;



    public bibtex_Book(
        int volume,        int edition,        int series,        String address,        String publisher    ) {
        super(
        );
        this.volume = volume;
        this.edition = edition;
        this.series = series;
        this.address = address;
        this.publisher = publisher;
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
    public int getSeries() {
        return series;
    }

    public void setSeries(int series) {
        this.series = series;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getPublisher() {
        return publisher;
    }

    public void setPublisher(String publisher) {
        this.publisher = publisher;
    }


}