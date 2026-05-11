





import java.util.List;
import java.util.ArrayList;

public class robot_While extends ExpBool {






    private List<robot_Instruction> robot_instructions;


    public robot_While(
    ) {
        super(
        );
        this.robot_instructions = new ArrayList<>();
    }

    public robot_While(
        ArrayList<robot_Instruction> robot_instructions    ) {
        this.robot_instructions = robot_instructions;
    }


    public List<robot_Instruction> getRobot_instructions() {
        return robot_instructions;
    }

    public void addRobot_instruction(Robot_instruction robot_instruction) {
        this.robot_instructions.add(robot_instruction);
    }

}