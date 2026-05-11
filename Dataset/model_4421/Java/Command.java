





import java.util.List;
import java.util.ArrayList;

public class Command  {






    private robo_command_Branch robo_command_branch;




    private robo_Program robo_program;




    private robo_command_Loop robo_command_loop;


    public Command(
    ) {
    }



    public robo_command_Branch getRobo_command_branch() {
        return robo_command_branch;
    }

    public void setRobo_command_branch(robo_command_Branch robo_command_branch) {
        this.robo_command_branch = robo_command_branch;
    }
    public robo_Program getRobo_program() {
        return robo_program;
    }

    public void setRobo_program(robo_Program robo_program) {
        this.robo_program = robo_program;
    }
    public robo_command_Loop getRobo_command_loop() {
        return robo_command_loop;
    }

    public void setRobo_command_loop(robo_command_Loop robo_command_loop) {
        this.robo_command_loop = robo_command_loop;
    }

}