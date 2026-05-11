





import java.util.List;
import java.util.ArrayList;

public class machine_Symbol  {

    private String position;
    private String value;
    private String name;





    private machine_Head machine_head;




    private machine_Tape machine_tape;




    private machine_Symbol machine_symbol;


    public machine_Symbol(
        String position,        String value,        String name    ) {
        this.position = position;
        this.value = value;
        this.name = name;
    }


    public String getPosition() {
        return position;
    }

    public void setPosition(String position) {
        this.position = position;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public machine_Head getMachine_head() {
        return machine_head;
    }

    public void setMachine_head(machine_Head machine_head) {
        this.machine_head = machine_head;
    }
    public machine_Tape getMachine_tape() {
        return machine_tape;
    }

    public void setMachine_tape(machine_Tape machine_tape) {
        this.machine_tape = machine_tape;
    }
    public machine_Symbol getMachine_symbol() {
        return machine_symbol;
    }

    public void setMachine_symbol(machine_Symbol machine_symbol) {
        this.machine_symbol = machine_symbol;
    }

}