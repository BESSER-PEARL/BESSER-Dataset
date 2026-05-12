





import java.util.List;
import java.util.ArrayList;

public class BIBTEXML_Book extends TitledEntry, EditoredEntry, PublisheredEntry, AuthoredEntry, DatedEntry {

    private String note;
    private String number;
    private String volume;
    private String address;
    private String edition;
    private String series;



    public BIBTEXML_Book(
        String note,        String number,        String volume,        String address,        String edition,        String series    ) {
        super(
        );
        this.note = note;
        this.number = number;
        this.volume = volume;
        this.address = address;
        this.edition = edition;
        this.series = series;
    }


    public String getNote() {
        return note;
    }

    public void setNote(String note) {
        this.note = note;
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
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
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


}