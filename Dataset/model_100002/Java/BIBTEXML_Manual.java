





import java.util.List;
import java.util.ArrayList;

public class BIBTEXML_Manual extends TitledEntry, AuthoredEntry, DatedEntry {

    private String edition;
    private String address;
    private String organization;
    private String note;



    public BIBTEXML_Manual(
        String edition,        String address,        String organization,        String note    ) {
        super(
        );
        this.edition = edition;
        this.address = address;
        this.organization = organization;
        this.note = note;
    }


    public String getEdition() {
        return edition;
    }

    public void setEdition(String edition) {
        this.edition = edition;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getOrganization() {
        return organization;
    }

    public void setOrganization(String organization) {
        this.organization = organization;
    }
    public String getNote() {
        return note;
    }

    public void setNote(String note) {
        this.note = note;
    }


}