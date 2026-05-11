





import java.util.List;
import java.util.ArrayList;

public class RobotProjectModel_InstructionBlock extends Instruction {






    private RobotProjectModel_If robotprojectmodel_if;




    private List<RobotProjectModel_Instruction> robotprojectmodel_instructions;




    private RobotProjectModel_If robotprojectmodel_if;


    public RobotProjectModel_InstructionBlock(
    ) {
        super(
        );
        this.robotprojectmodel_instructions = new ArrayList<>();
    }

    public RobotProjectModel_InstructionBlock(
        ArrayList<RobotProjectModel_Instruction> robotprojectmodel_instructions    ) {
        this.robotprojectmodel_instructions = robotprojectmodel_instructions;
    }


    public RobotProjectModel_If getRobotprojectmodel_if() {
        return robotprojectmodel_if;
    }

    public void setRobotprojectmodel_if(RobotProjectModel_If robotprojectmodel_if) {
        this.robotprojectmodel_if = robotprojectmodel_if;
    }
    public List<RobotProjectModel_Instruction> getRobotprojectmodel_instructions() {
        return robotprojectmodel_instructions;
    }

    public void addRobotprojectmodel_instruction(Robotprojectmodel_instruction robotprojectmodel_instruction) {
        this.robotprojectmodel_instructions.add(robotprojectmodel_instruction);
    }
    public RobotProjectModel_If getRobotprojectmodel_if() {
        return robotprojectmodel_if;
    }

    public void setRobotprojectmodel_if(RobotProjectModel_If robotprojectmodel_if) {
        this.robotprojectmodel_if = robotprojectmodel_if;
    }

}