





import java.util.List;
import java.util.ArrayList;

public class BIBTEXML_ThesisEntry extends TitledEntry, AuthoredEntry, DatedEntry, SchoolEntry {

    private String address;
    private String note;
    private String type;



    public BIBTEXML_ThesisEntry(
        String address,        String note,        String type    ) {
        super(
        );
        this.address = address;
        this.note = note;
        this.type = type;
    }


    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getNote() {
        return note;
    }

    public void setNote(String note) {
        this.note = note;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}