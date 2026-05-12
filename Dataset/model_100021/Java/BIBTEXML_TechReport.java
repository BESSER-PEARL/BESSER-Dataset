





import java.util.List;
import java.util.ArrayList;

public class BIBTEXML_TechReport extends TitledEntry, AuthoredEntry, DatedEntry, InstitutionEntry {

    private String note;
    private String address;
    private String type;
    private String number;



    public BIBTEXML_TechReport(
        String note,        String address,        String type,        String number    ) {
        super(
        );
        this.note = note;
        this.address = address;
        this.type = type;
        this.number = number;
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
    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }


}