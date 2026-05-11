





import java.util.List;
import java.util.ArrayList;

public class muddle_Feature  {

    private String name;
    private boolean many;
    private boolean primary;
    private boolean runtime;





    private muddle_MuddleElementType muddle_muddleelementtype;




    private muddle_MuddleElementType muddle_muddleelementtype;




    private muddle_Type muddle_type;




    private List<muddle_Slot> muddle_slots;




    private muddle_Slot muddle_slot;


    public muddle_Feature(
        String name,        boolean many,        boolean primary,        boolean runtime    ) {
        this.name = name;
        this.many = many;
        this.primary = primary;
        this.runtime = runtime;
        this.muddle_slots = new ArrayList<>();
    }

    public muddle_Feature(
        String name,        boolean many,        boolean primary,        boolean runtime        ArrayList<muddle_Slot> muddle_slots    ) {
        this.name = name;
        this.many = many;
        this.primary = primary;
        this.runtime = runtime;
        this.muddle_slots = muddle_slots;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getMany() {
        return many;
    }

    public void setMany(boolean many) {
        this.many = many;
    }
    public boolean getPrimary() {
        return primary;
    }

    public void setPrimary(boolean primary) {
        this.primary = primary;
    }
    public boolean getRuntime() {
        return runtime;
    }

    public void setRuntime(boolean runtime) {
        this.runtime = runtime;
    }

    public muddle_MuddleElementType getMuddle_muddleelementtype() {
        return muddle_muddleelementtype;
    }

    public void setMuddle_muddleelementtype(muddle_MuddleElementType muddle_muddleelementtype) {
        this.muddle_muddleelementtype = muddle_muddleelementtype;
    }
    public muddle_MuddleElementType getMuddle_muddleelementtype() {
        return muddle_muddleelementtype;
    }

    public void setMuddle_muddleelementtype(muddle_MuddleElementType muddle_muddleelementtype) {
        this.muddle_muddleelementtype = muddle_muddleelementtype;
    }
    public muddle_Type getMuddle_type() {
        return muddle_type;
    }

    public void setMuddle_type(muddle_Type muddle_type) {
        this.muddle_type = muddle_type;
    }
    public List<muddle_Slot> getMuddle_slots() {
        return muddle_slots;
    }

    public void addMuddle_slot(Muddle_slot muddle_slot) {
        this.muddle_slots.add(muddle_slot);
    }
    public muddle_Slot getMuddle_slot() {
        return muddle_slot;
    }

    public void setMuddle_slot(muddle_Slot muddle_slot) {
        this.muddle_slot = muddle_slot;
    }

}