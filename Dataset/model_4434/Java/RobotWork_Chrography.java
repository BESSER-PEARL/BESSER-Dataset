





import java.util.List;
import java.util.ArrayList;

public class RobotWork_Chrography extends Instruction {

    private String name;





    private List<RobotWork_Instruction> robotwork_instructions;


    public RobotWork_Chrography(
        String name    ) {
        super(
        );
        this.name = name;
        this.robotwork_instructions = new ArrayList<>();
    }

    public RobotWork_Chrography(
        String name        ArrayList<RobotWork_Instruction> robotwork_instructions    ) {
        this.name = name;
        this.robotwork_instructions = robotwork_instructions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<RobotWork_Instruction> getRobotwork_instructions() {
        return robotwork_instructions;
    }

    public void addRobotwork_instruction(Robotwork_instruction robotwork_instruction) {
        this.robotwork_instructions.add(robotwork_instruction);
    }

}