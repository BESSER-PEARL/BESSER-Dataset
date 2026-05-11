





import java.util.List;
import java.util.ArrayList;

public class machine_Transition  {

    private String moveTo;
    private String read;
    private String name;
    private String write;





    private machine_State machine_state;




    private machine_State machine_state;


    public machine_Transition(
        String moveTo,        String read,        String name,        String write    ) {
        this.moveTo = moveTo;
        this.read = read;
        this.name = name;
        this.write = write;
    }


    public String getMoveto() {
        return moveTo;
    }

    public void setMoveto(String moveTo) {
        this.moveTo = moveTo;
    }
    public String getRead() {
        return read;
    }

    public void setRead(String read) {
        this.read = read;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getWrite() {
        return write;
    }

    public void setWrite(String write) {
        this.write = write;
    }

    public machine_State getMachine_state() {
        return machine_state;
    }

    public void setMachine_state(machine_State machine_state) {
        this.machine_state = machine_state;
    }
    public machine_State getMachine_state() {
        return machine_state;
    }

    public void setMachine_state(machine_State machine_state) {
        this.machine_state = machine_state;
    }

}