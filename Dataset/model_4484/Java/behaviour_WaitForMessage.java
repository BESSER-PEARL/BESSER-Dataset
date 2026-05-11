





import java.util.List;
import java.util.ArrayList;

public class behaviour_WaitForMessage extends Instruction {

    private float timeout;
    private String type;





    private List<behaviour_Instruction> behaviour_instructions;




    private List<behaviour_Instruction> behaviour_instructions;


    public behaviour_WaitForMessage(
        float timeout,        String type    ) {
        super(
        );
        this.timeout = timeout;
        this.type = type;
        this.behaviour_instructions = new ArrayList<>();
        this.behaviour_instructions = new ArrayList<>();
    }

    public behaviour_WaitForMessage(
        float timeout,        String type        ArrayList<behaviour_Instruction> behaviour_instructions,        ArrayList<behaviour_Instruction> behaviour_instructions    ) {
        this.timeout = timeout;
        this.type = type;
        this.behaviour_instructions = behaviour_instructions;
        this.behaviour_instructions = behaviour_instructions;
    }

    public float getTimeout() {
        return timeout;
    }

    public void setTimeout(float timeout) {
        this.timeout = timeout;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public List<behaviour_Instruction> getBehaviour_instructions() {
        return behaviour_instructions;
    }

    public void addBehaviour_instruction(Behaviour_instruction behaviour_instruction) {
        this.behaviour_instructions.add(behaviour_instruction);
    }
    public List<behaviour_Instruction> getBehaviour_instructions() {
        return behaviour_instructions;
    }

    public void addBehaviour_instruction(Behaviour_instruction behaviour_instruction) {
        this.behaviour_instructions.add(behaviour_instruction);
    }

}