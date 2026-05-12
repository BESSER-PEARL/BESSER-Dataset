





import java.util.List;
import java.util.ArrayList;

public class build_command_InvokeCommand extends BuildUnitCommand {

    private String action;



    public build_command_InvokeCommand(
        String action    ) {
        super(
        );
        this.action = action;
    }


    public String getAction() {
        return action;
    }

    public void setAction(String action) {
        this.action = action;
    }


}