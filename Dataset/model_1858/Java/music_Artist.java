





import java.util.List;
import java.util.ArrayList;

public class music_Artist  {

    private String notes;
    private String name;



    public music_Artist(
        String notes,        String name    ) {
        this.notes = notes;
        this.name = name;
    }


    public String getNotes() {
        return notes;
    }

    public void setNotes(String notes) {
        this.notes = notes;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}