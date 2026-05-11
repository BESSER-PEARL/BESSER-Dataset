





import java.util.List;
import java.util.ArrayList;

public class robo_command_Assignment extends Command {

    private String variable;



    public robo_command_Assignment(
        String variable    ) {
        super(
        );
        this.variable = variable;
    }


    public String getVariable() {
        return variable;
    }

    public void setVariable(String variable) {
        this.variable = variable;
    }


}