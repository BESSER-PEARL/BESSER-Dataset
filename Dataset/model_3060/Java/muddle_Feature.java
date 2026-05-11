





import java.util.List;
import java.util.ArrayList;

public class muddle_Feature  {

    private boolean runtime;
    private boolean primary;
    private String name;
    private boolean many;





    private muddle_LinkElementType muddle_linkelementtype;




    private muddle_MuddleElementType muddle_muddleelementtype;




    private muddle_LinkElementType muddle_linkelementtype;




    private muddle_Slot muddle_slot;




    private List<muddle_Slot> muddle_slots;




    private muddle_Type muddle_type;




    private muddle_LinkElementType muddle_linkelementtype;




    private muddle_MuddleElementType muddle_muddleelementtype;




    private muddle_LinkElementType muddle_linkelementtype;


    public muddle_Feature(
        boolean runtime,        boolean primary,        String name,        boolean many    ) {
        this.runtime = runtime;
        this.primary = primary;
        this.name = name;
        this.many = many;
        this.muddle_slots = new ArrayList<>();
    }

    public muddle_Feature(
        boolean runtime,        boolean primary,        String name,        boolean many        ArrayList<muddle_Slot> muddle_slots    ) {
        this.runtime = runtime;
        this.primary = primary;
        this.name = name;
        this.many = many;
        this.muddle_slots = muddle_slots;
    }

    public boolean getRuntime() {
        return runtime;
    }

    public void setRuntime(boolean runtime) {
        this.runtime = runtime;
    }
    public boolean getPrimary() {
        return primary;
    }

    public void setPrimary(boolean primary) {
        this.primary = primary;
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

    public muddle_LinkElementType getMuddle_linkelementtype() {
        return muddle_linkelementtype;
    }

    public void setMuddle_linkelementtype(muddle_LinkElementType muddle_linkelementtype) {
        this.muddle_linkelementtype = muddle_linkelementtype;
    }
    public muddle_MuddleElementType getMuddle_muddleelementtype() {
        return muddle_muddleelementtype;
    }

    public void setMuddle_muddleelementtype(muddle_MuddleElementType muddle_muddleelementtype) {
        this.muddle_muddleelementtype = muddle_muddleelementtype;
    }
    public muddle_LinkElementType getMuddle_linkelementtype() {
        return muddle_linkelementtype;
    }

    public void setMuddle_linkelementtype(muddle_LinkElementType muddle_linkelementtype) {
        this.muddle_linkelementtype = muddle_linkelementtype;
    }
    public muddle_Slot getMuddle_slot() {
        return muddle_slot;
    }

    public void setMuddle_slot(muddle_Slot muddle_slot) {
        this.muddle_slot = muddle_slot;
    }
    public List<muddle_Slot> getMuddle_slots() {
        return muddle_slots;
    }

    public void addMuddle_slot(Muddle_slot muddle_slot) {
        this.muddle_slots.add(muddle_slot);
    }
    public muddle_Type getMuddle_type() {
        return muddle_type;
    }

    public void setMuddle_type(muddle_Type muddle_type) {
        this.muddle_type = muddle_type;
    }
    public muddle_LinkElementType getMuddle_linkelementtype() {
        return muddle_linkelementtype;
    }

    public void setMuddle_linkelementtype(muddle_LinkElementType muddle_linkelementtype) {
        this.muddle_linkelementtype = muddle_linkelementtype;
    }
    public muddle_MuddleElementType getMuddle_muddleelementtype() {
        return muddle_muddleelementtype;
    }

    public void setMuddle_muddleelementtype(muddle_MuddleElementType muddle_muddleelementtype) {
        this.muddle_muddleelementtype = muddle_muddleelementtype;
    }
    public muddle_LinkElementType getMuddle_linkelementtype() {
        return muddle_linkelementtype;
    }

    public void setMuddle_linkelementtype(muddle_LinkElementType muddle_linkelementtype) {
        this.muddle_linkelementtype = muddle_linkelementtype;
    }

}