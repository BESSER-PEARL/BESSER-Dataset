





import java.util.List;
import java.util.ArrayList;

public class smc_Block extends Command {






    private List<smc_Command> smc_commands;


    public smc_Block(
    ) {
        super(
        );
        this.smc_commands = new ArrayList<>();
    }

    public smc_Block(
        ArrayList<smc_Command> smc_commands    ) {
        this.smc_commands = smc_commands;
    }


    public List<smc_Command> getSmc_commands() {
        return smc_commands;
    }

    public void addSmc_command(Smc_command smc_command) {
        this.smc_commands.add(smc_command);
    }

}