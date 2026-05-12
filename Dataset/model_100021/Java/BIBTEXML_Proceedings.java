





import java.util.List;
import java.util.ArrayList;

public class BIBTEXML_Proceedings extends TitledEntry, DatedEntry {

    private String editor;
    private String volume;
    private String organization;
    private String address;
    private String publisher;
    private String number;
    private String note;
    private String series;



    public BIBTEXML_Proceedings(
        String editor,        String volume,        String organization,        String address,        String publisher,        String number,        String note,        String series    ) {
        super(
        );
        this.editor = editor;
        this.volume = volume;
        this.organization = organization;
        this.address = address;
        this.publisher = publisher;
        this.number = number;
        this.note = note;
        this.series = series;
    }


    public String getEditor() {
        return editor;
    }

    public void setEditor(String editor) {
        this.editor = editor;
    }
    public String getVolume() {
        return volume;
    }

    public void setVolume(String volume) {
        this.volume = volume;
    }
    public String getOrganization() {
        return organization;
    }

    public void setOrganization(String organization) {
        this.organization = organization;
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
    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }
    public String getNote() {
        return note;
    }

    public void setNote(String note) {
        this.note = note;
    }
    public String getSeries() {
        return series;
    }

    public void setSeries(String series) {
        this.series = series;
    }


}