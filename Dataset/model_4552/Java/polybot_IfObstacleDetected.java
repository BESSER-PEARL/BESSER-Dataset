





import java.util.List;
import java.util.ArrayList;

public class polybot_IfObstacleDetected extends Instruction {






    private List<polybot_Instruction> polybot_instructions;


    public polybot_IfObstacleDetected(
    ) {
        super(
        );
        this.polybot_instructions = new ArrayList<>();
    }

    public polybot_IfObstacleDetected(
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