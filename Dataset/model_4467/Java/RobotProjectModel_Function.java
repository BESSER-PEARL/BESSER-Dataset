





import java.util.List;
import java.util.ArrayList;

public class RobotProjectModel_Function extends Instruction {

    private String name;





    private RobotProjectModel_Call robotprojectmodel_call;




    private RobotProjectModel_InstructionBlock robotprojectmodel_instructionblock;


    public RobotProjectModel_Function(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public RobotProjectModel_Call getRobotprojectmodel_call() {
        return robotprojectmodel_call;
    }

    public void setRobotprojectmodel_call(RobotProjectModel_Call robotprojectmodel_call) {
        this.robotprojectmodel_call = robotprojectmodel_call;
    }
    public RobotProjectModel_InstructionBlock getRobotprojectmodel_instructionblock() {
        return robotprojectmodel_instructionblock;
    }

    public void setRobotprojectmodel_instructionblock(RobotProjectModel_InstructionBlock robotprojectmodel_instructionblock) {
        this.robotprojectmodel_instructionblock = robotprojectmodel_instructionblock;
    }

}