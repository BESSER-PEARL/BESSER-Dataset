





import java.util.List;
import java.util.ArrayList;

public class BIBTEXML_Book extends TitledEntry, DatedEntry, AuthoredEntry, EditoredEntry, PublisheredEntry {

    private String address;
    private String volume;
    private String note;
    private String edition;
    private String series;
    private String number;



    public BIBTEXML_Book(
        String address,        String volume,        String note,        String edition,        String series,        String number    ) {
        super(
        );
        this.address = address;
        this.volume = volume;
        this.note = note;
        this.edition = edition;
        this.series = series;
        this.number = number;
    }


    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getVolume() {
        return volume;
    }

    public void setVolume(String volume) {
        this.volume = volume;
    }
    public String getNote() {
        return note;
    }

    public void setNote(String note) {
        this.note = note;
    }
    public String getEdition() {
        return edition;
    }

    public void setEdition(String edition) {
        this.edition = edition;
    }
    public String getSeries() {
        return series;
    }

    public void setSeries(String series) {
        this.series = series;
    }
    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }


}