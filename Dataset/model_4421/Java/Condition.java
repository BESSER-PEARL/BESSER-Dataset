





import java.util.List;
import java.util.ArrayList;

public class Condition  {






    private robo_command_Drive robo_command_drive;




    private robo_command_Loop robo_command_loop;




    private robo_command_Branch robo_command_branch;


    public Condition(
    ) {
    }



    public robo_command_Drive getRobo_command_drive() {
        return robo_command_drive;
    }

    public void setRobo_command_drive(robo_command_Drive robo_command_drive) {
        this.robo_command_drive = robo_command_drive;
    }
    public robo_command_Loop getRobo_command_loop() {
        return robo_command_loop;
    }

    public void setRobo_command_loop(robo_command_Loop robo_command_loop) {
        this.robo_command_loop = robo_command_loop;
    }
    public robo_command_Branch getRobo_command_branch() {
        return robo_command_branch;
    }

    public void setRobo_command_branch(robo_command_Branch robo_command_branch) {
        this.robo_command_branch = robo_command_branch;
    }

}