





import java.util.List;
import java.util.ArrayList;

public class RobotProjectModel_Robot  {






    private List<RobotProjectModel_Instruction> robotprojectmodel_instructions;


    public RobotProjectModel_Robot(
    ) {
        this.robotprojectmodel_instructions = new ArrayList<>();
    }

    public RobotProjectModel_Robot(
        ArrayList<RobotProjectModel_Instruction> robotprojectmodel_instructions    ) {
        this.robotprojectmodel_instructions = robotprojectmodel_instructions;
    }


    public List<RobotProjectModel_Instruction> getRobotprojectmodel_instructions() {
        return robotprojectmodel_instructions;
    }

    public void addRobotprojectmodel_instruction(Robotprojectmodel_instruction robotprojectmodel_instruction) {
        this.robotprojectmodel_instructions.add(robotprojectmodel_instruction);
    }

}