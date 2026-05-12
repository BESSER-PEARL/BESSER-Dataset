





import java.util.List;
import java.util.ArrayList;

public class BIBTEXML_Booklet extends TitledEntry, DatedEntry {

    private String address;
    private String howpublished;
    private String note;



    public BIBTEXML_Booklet(
        String address,        String howpublished,        String note    ) {
        super(
        );
        this.address = address;
        this.howpublished = howpublished;
        this.note = note;
    }


    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getHowpublished() {
        return howpublished;
    }

    public void setHowpublished(String howpublished) {
        this.howpublished = howpublished;
    }
    public String getNote() {
        return note;
    }

    public void setNote(String note) {
        this.note = note;
    }


}