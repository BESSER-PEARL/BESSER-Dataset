





import java.util.List;
import java.util.ArrayList;

public class BIBTEXML_Manual extends AuthoredEntry, TitledEntry, DatedEntry {

    private String note;
    private String edition;
    private String organization;
    private String address;



    public BIBTEXML_Manual(
        String note,        String edition,        String organization,        String address    ) {
        super(
        );
        this.note = note;
        this.edition = edition;
        this.organization = organization;
        this.address = address;
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


}