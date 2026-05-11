





import java.util.List;
import java.util.ArrayList;

public class micro_API extends NamedElement {






    private micro_Command micro_command;




    private micro_Event micro_event;




    private micro_AggregateService micro_aggregateservice;




    private List<micro_Command> micro_commands;




    private List<micro_Event> micro_events;


    public micro_API(
    ) {
        super(
        );
        this.micro_commands = new ArrayList<>();
        this.micro_events = new ArrayList<>();
    }

    public micro_API(
        ArrayList<micro_Command> micro_commands,        ArrayList<micro_Event> micro_events    ) {
        this.micro_commands = micro_commands;
        this.micro_events = micro_events;
    }


    public micro_Command getMicro_command() {
        return micro_command;
    }

    public void setMicro_command(micro_Command micro_command) {
        this.micro_command = micro_command;
    }
    public micro_Event getMicro_event() {
        return micro_event;
    }

    public void setMicro_event(micro_Event micro_event) {
        this.micro_event = micro_event;
    }
    public micro_AggregateService getMicro_aggregateservice() {
        return micro_aggregateservice;
    }

    public void setMicro_aggregateservice(micro_AggregateService micro_aggregateservice) {
        this.micro_aggregateservice = micro_aggregateservice;
    }
    public List<micro_Command> getMicro_commands() {
        return micro_commands;
    }

    public void addMicro_command(Micro_command micro_command) {
        this.micro_commands.add(micro_command);
    }
    public List<micro_Event> getMicro_events() {
        return micro_events;
    }

    public void addMicro_event(Micro_event micro_event) {
        this.micro_events.add(micro_event);
    }

}