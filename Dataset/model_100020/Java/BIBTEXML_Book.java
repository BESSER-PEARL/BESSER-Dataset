





import java.util.List;
import java.util.ArrayList;

public class BIBTEXML_Book extends PublisheredEntry, EditoredEntry, TitledEntry, DatedEntry, AuthoredEntry {

    private String note;
    private String address;
    private String series;
    private String edition;
    private String number;
    private String volume;



    public BIBTEXML_Book(
        String note,        String address,        String series,        String edition,        String number,        String volume    ) {
        super(
        );
        this.note = note;
        this.address = address;
        this.series = series;
        this.edition = edition;
        this.number = number;
        this.volume = volume;
    }


    public String getNote() {
        return note;
    }

    public void setNote(String note) {
        this.note = note;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getSeries() {
        return series;
    }

    public void setSeries(String series) {
        this.series = series;
    }
    public String getEdition() {
        return edition;
    }

    public void setEdition(String edition) {
        this.edition = edition;
    }
    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }
    public String getVolume() {
        return volume;
    }

    public void setVolume(String volume) {
        this.volume = volume;
    }


}