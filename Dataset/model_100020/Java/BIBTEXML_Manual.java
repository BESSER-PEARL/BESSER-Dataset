





import java.util.List;
import java.util.ArrayList;

public class BIBTEXML_Manual extends DatedEntry, TitledEntry, AuthoredEntry {

    private String note;
    private String organization;
    private String address;
    private String edition;



    public BIBTEXML_Manual(
        String note,        String organization,        String address,        String edition    ) {
        super(
        );
        this.note = note;
        this.organization = organization;
        this.address = address;
        this.edition = edition;
    }


    public String getNote() {
        return note;
    }

    public void setNote(String note) {
        this.note = note;
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
    public String getEdition() {
        return edition;
    }

    public void setEdition(String edition) {
        this.edition = edition;
    }


}