





import java.util.List;
import java.util.ArrayList;

public class Storage  {

    private String instruction_ID;





    private List<Part> parts;


    public Storage(
        String instruction_ID    ) {
        this.instruction_ID = instruction_ID;
        this.parts = new ArrayList<>();
    }

    public Storage(
        String instruction_ID        ArrayList<Part> parts    ) {
        this.instruction_ID = instruction_ID;
        this.parts = parts;
    }

    public String getInstruction_id() {
        return instruction_ID;
    }

    public void setInstruction_id(String instruction_ID) {
        this.instruction_ID = instruction_ID;
    }

    public List<Part> getParts() {
        return parts;
    }

    public void addPart(Part part) {
        this.parts.add(part);
    }

}