





import java.util.List;
import java.util.ArrayList;

public class behaviour_Choice extends Instruction {






    private List<behaviour_Instruction> behaviour_instructions;




    private List<behaviour_Instruction> behaviour_instructions;


    public behaviour_Choice(
    ) {
        super(
        );
        this.behaviour_instructions = new ArrayList<>();
        this.behaviour_instructions = new ArrayList<>();
    }

    public behaviour_Choice(
        ArrayList<behaviour_Instruction> behaviour_instructions,        ArrayList<behaviour_Instruction> behaviour_instructions    ) {
        this.behaviour_instructions = behaviour_instructions;
        this.behaviour_instructions = behaviour_instructions;
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