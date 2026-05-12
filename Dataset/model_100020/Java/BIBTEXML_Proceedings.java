





import java.util.List;
import java.util.ArrayList;

public class BIBTEXML_Proceedings extends DatedEntry, TitledEntry {

    private String organization;
    private String number;
    private String series;
    private String note;
    private String publisher;
    private String volume;
    private String editor;
    private String address;



    public BIBTEXML_Proceedings(
        String organization,        String number,        String series,        String note,        String publisher,        String volume,        String editor,        String address    ) {
        super(
        );
        this.organization = organization;
        this.number = number;
        this.series = series;
        this.note = note;
        this.publisher = publisher;
        this.volume = volume;
        this.editor = editor;
        this.address = address;
    }


    public String getOrganization() {
        return organization;
    }

    public void setOrganization(String organization) {
        this.organization = organization;
    }
    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }
    public String getSeries() {
        return series;
    }

    public void setSeries(String series) {
        this.series = series;
    }
    public String getNote() {
        return note;
    }

    public void setNote(String note) {
        this.note = note;
    }
    public String getPublisher() {
        return publisher;
    }

    public void setPublisher(String publisher) {
        this.publisher = publisher;
    }
    public String getVolume() {
        return volume;
    }

    public void setVolume(String volume) {
        this.volume = volume;
    }
    public String getEditor() {
        return editor;
    }

    public void setEditor(String editor) {
        this.editor = editor;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }


}