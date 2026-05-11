





import java.util.List;
import java.util.ArrayList;

public class muddle_MuddleElement  {

    private String id;





    private muddle_Slot muddle_slot;




    private muddle_Muddle muddle_muddle;




    private List<muddle_Slot> muddle_slots;




    private muddle_Muddle muddle_muddle;


    public muddle_MuddleElement(
        String id    ) {
        this.id = id;
        this.muddle_slots = new ArrayList<>();
    }

    public muddle_MuddleElement(
        String id        ArrayList<muddle_Slot> muddle_slots    ) {
        this.id = id;
        this.muddle_slots = muddle_slots;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public muddle_Slot getMuddle_slot() {
        return muddle_slot;
    }

    public void setMuddle_slot(muddle_Slot muddle_slot) {
        this.muddle_slot = muddle_slot;
    }
    public muddle_Muddle getMuddle_muddle() {
        return muddle_muddle;
    }

    public void setMuddle_muddle(muddle_Muddle muddle_muddle) {
        this.muddle_muddle = muddle_muddle;
    }
    public List<muddle_Slot> getMuddle_slots() {
        return muddle_slots;
    }

    public void addMuddle_slot(Muddle_slot muddle_slot) {
        this.muddle_slots.add(muddle_slot);
    }
    public muddle_Muddle getMuddle_muddle() {
        return muddle_muddle;
    }

    public void setMuddle_muddle(muddle_Muddle muddle_muddle) {
        this.muddle_muddle = muddle_muddle;
    }

}