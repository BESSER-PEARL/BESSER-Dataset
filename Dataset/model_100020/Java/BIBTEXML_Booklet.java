





import java.util.List;
import java.util.ArrayList;

public class BIBTEXML_Booklet extends DatedEntry, TitledEntry {

    private String address;
    private String note;
    private String howpublished;



    public BIBTEXML_Booklet(
        String address,        String note,        String howpublished    ) {
        super(
        );
        this.address = address;
        this.note = note;
        this.howpublished = howpublished;
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
    public String getHowpublished() {
        return howpublished;
    }

    public void setHowpublished(String howpublished) {
        this.howpublished = howpublished;
    }


}