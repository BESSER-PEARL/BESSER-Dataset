





import java.util.List;
import java.util.ArrayList;

public class polybot_IfObjectDetected extends Instruction {






    private List<polybot_Instruction> polybot_instructions;


    public polybot_IfObjectDetected(
    ) {
        super(
        );
        this.polybot_instructions = new ArrayList<>();
    }

    public polybot_IfObjectDetected(
        ArrayList<polybot_Instruction> polybot_instructions    ) {
        this.polybot_instructions = polybot_instructions;
    }


    public List<polybot_Instruction> getPolybot_instructions() {
        return polybot_instructions;
    }

    public void addPolybot_instruction(Polybot_instruction polybot_instruction) {
        this.polybot_instructions.add(polybot_instruction);
    }

}