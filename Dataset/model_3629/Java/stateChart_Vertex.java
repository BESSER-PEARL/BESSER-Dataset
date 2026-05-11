





import java.util.List;
import java.util.ArrayList;

public class stateChart_Vertex  {

    private boolean isActive;
    private String name;
    private String note;



    public stateChart_Vertex(
        boolean isActive,        String name,        String note    ) {
        this.isActive = isActive;
        this.name = name;
        this.note = note;
    }


    public boolean getIsactive() {
        return isActive;
    }

    public void setIsactive(boolean isActive) {
        this.isActive = isActive;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getNote() {
        return note;
    }

    public void setNote(String note) {
        this.note = note;
    }


}