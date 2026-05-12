





import java.util.List;
import java.util.ArrayList;

public class BIBTEXML_NotedEntry extends Entry {

    private String note;



    public BIBTEXML_NotedEntry(
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