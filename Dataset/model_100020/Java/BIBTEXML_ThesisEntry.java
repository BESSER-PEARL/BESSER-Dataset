





import java.util.List;
import java.util.ArrayList;

public class BIBTEXML_ThesisEntry extends DatedEntry, SchoolEntry, TitledEntry, AuthoredEntry {

    private String note;
    private String address;
    private String type;



    public BIBTEXML_ThesisEntry(
        String note,        String address,        String type    ) {
        super(
        );
        this.note = note;
        this.address = address;
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
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}