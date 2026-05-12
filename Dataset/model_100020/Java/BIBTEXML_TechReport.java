





import java.util.List;
import java.util.ArrayList;

public class BIBTEXML_TechReport extends DatedEntry, InstitutionEntry, TitledEntry, AuthoredEntry {

    private String number;
    private String address;
    private String type;
    private String note;



    public BIBTEXML_TechReport(
        String number,        String address,        String type,        String note    ) {
        super(
        );
        this.number = number;
        this.address = address;
        this.type = type;
        this.note = note;
    }


    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
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
    public String getNote() {
        return note;
    }

    public void setNote(String note) {
        this.note = note;
    }


}