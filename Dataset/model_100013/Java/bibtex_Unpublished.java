





import java.util.List;
import java.util.ArrayList;

public class bibtex_Unpublished extends TitledEntry, AuthoredEntry {

    private String note;



    public bibtex_Unpublished(
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