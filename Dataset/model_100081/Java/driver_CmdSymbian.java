





import java.util.List;
import java.util.ArrayList;

public class driver_CmdSymbian  {

    private String output;
    private String sync;
    private String argument;
    private String statCommand;



    public driver_CmdSymbian(
        String output,        String sync,        String argument,        String statCommand    ) {
        this.output = output;
        this.sync = sync;
        this.argument = argument;
        this.statCommand = statCommand;
    }


    public String getOutput() {
        return output;
    }

    public void setOutput(String output) {
        this.output = output;
    }
    public String getSync() {
        return sync;
    }

    public void setSync(String sync) {
        this.sync = sync;
    }
    public String getArgument() {
        return argument;
    }

    public void setArgument(String argument) {
        this.argument = argument;
    }
    public String getStatcommand() {
        return statCommand;
    }

    public void setStatcommand(String statCommand) {
        this.statCommand = statCommand;
    }


}