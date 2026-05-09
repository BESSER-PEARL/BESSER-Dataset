





import java.util.List;
import java.util.ArrayList;

public class BibTeX_Unpublished extends TitledEntry, AuthoredEntry {

    private String note;



    public BibTeX_Unpublished(
        String note    ) {
        super(
        );
        this.note = note;
    }


    public String getNote() {
        return note;
    }

    public void setNote(String note) {
        this.note = note;
    }


}