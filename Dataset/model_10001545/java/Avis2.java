





import java.util.List;
import java.util.ArrayList;

public class Avis2  {

    private String description;
    private int note;



    public Avis2(
        String description,        int note    ) {
        this.description = description;
        this.note = note;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public int getNote() {
        return note;
    }

    public void setNote(int note) {
        this.note = note;
    }


}