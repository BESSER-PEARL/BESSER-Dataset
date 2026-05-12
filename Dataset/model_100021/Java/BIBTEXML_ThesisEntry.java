





import java.util.List;
import java.util.ArrayList;

public class BIBTEXML_ThesisEntry extends AuthoredEntry, TitledEntry, DatedEntry, SchoolEntry {

    private String type;
    private String note;
    private String address;



    public BIBTEXML_ThesisEntry(
        String type,        String note,        String address    ) {
        super(
        );
        this.type = type;
        this.note = note;
        this.address = address;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
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


}