





import java.util.List;
import java.util.ArrayList;

public class micro_API extends NamedElement {






    private micro_Command micro_command;




    private List<micro_Info> micro_infos;




    private micro_Info micro_info;




    private List<micro_Command> micro_commands;


    public micro_API(
    ) {
        super(
        );
        this.micro_infos = new ArrayList<>();
        this.micro_commands = new ArrayList<>();
    }

    public micro_API(
        ArrayList<micro_Info> micro_infos,        ArrayList<micro_Command> micro_commands    ) {
        this.micro_infos = micro_infos;
        this.micro_commands = micro_commands;
    }


    public micro_Command getMicro_command() {
        return micro_command;
    }

    public void setMicro_command(micro_Command micro_command) {
        this.micro_command = micro_command;
    }
    public List<micro_Info> getMicro_infos() {
        return micro_infos;
    }

    public void addMicro_info(Micro_info micro_info) {
        this.micro_infos.add(micro_info);
    }
    public micro_Info getMicro_info() {
        return micro_info;
    }

    public void setMicro_info(micro_Info micro_info) {
        this.micro_info = micro_info;
    }
    public List<micro_Command> getMicro_commands() {
        return micro_commands;
    }

    public void addMicro_command(Micro_command micro_command) {
        this.micro_commands.add(micro_command);
    }

}