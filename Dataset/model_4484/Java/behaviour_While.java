





import java.util.List;
import java.util.ArrayList;

public class behaviour_While extends Instruction {






    private behaviour_Condition behaviour_condition;




    private List<behaviour_Instruction> behaviour_instructions;


    public behaviour_While(
    ) {
        super(
        );
        this.behaviour_instructions = new ArrayList<>();
    }

    public behaviour_While(
        ArrayList<behaviour_Instruction> behaviour_instructions    ) {
        this.behaviour_instructions = behaviour_instructions;
    }


    public behaviour_Condition getBehaviour_condition() {
        return behaviour_condition;
    }

    public void setBehaviour_condition(behaviour_Condition behaviour_condition) {
        this.behaviour_condition = behaviour_condition;
    }
    public List<behaviour_Instruction> getBehaviour_instructions() {
        return behaviour_instructions;
    }

    public void addBehaviour_instruction(Behaviour_instruction behaviour_instruction) {
        this.behaviour_instructions.add(behaviour_instruction);
    }

}