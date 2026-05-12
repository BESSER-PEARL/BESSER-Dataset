





import java.util.List;
import java.util.ArrayList;

public class BIBTEXML_Proceedings extends TitledEntry, DatedEntry {

    private String editor;
    private String volume;
    private String note;
    private String number;
    private String series;
    private String address;
    private String publisher;
    private String organization;



    public BIBTEXML_Proceedings(
        String editor,        String volume,        String note,        String number,        String series,        String address,        String publisher,        String organization    ) {
        super(
        );
        this.editor = editor;
        this.volume = volume;
        this.note = note;
        this.number = number;
        this.series = series;
        this.address = address;
        this.publisher = publisher;
        this.organization = organization;
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
    public String getSeries() {
        return series;
    }

    public void setSeries(String series) {
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
    public String getOrganization() {
        return organization;
    }

    public void setOrganization(String organization) {
        this.organization = organization;
    }


}