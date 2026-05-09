





import java.util.List;
import java.util.ArrayList;

public class td1_Process  {

    private int StateSize;
    private int VarSize;
    private String Name;





    private td1_Component td1_component;




    private td1_Port td1_port;




    private td1_Program td1_program;




    private List<td1_Trigger> td1_triggers;


    public td1_Process(
        int StateSize,        int VarSize,        String Name    ) {
        this.StateSize = StateSize;
        this.VarSize = VarSize;
        this.Name = Name;
        this.td1_triggers = new ArrayList<>();
    }

    public td1_Process(
        int StateSize,        int VarSize,        String Name        ArrayList<td1_Trigger> td1_triggers    ) {
        this.StateSize = StateSize;
        this.VarSize = VarSize;
        this.Name = Name;
        this.td1_triggers = td1_triggers;
    }

    public int getStatesize() {
        return StateSize;
    }

    public void setStatesize(int StateSize) {
        this.StateSize = StateSize;
    }
    public int getVarsize() {
        return VarSize;
    }

    public void setVarsize(int VarSize) {
        this.VarSize = VarSize;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public td1_Component getTd1_component() {
        return td1_component;
    }

    public void setTd1_component(td1_Component td1_component) {
        this.td1_component = td1_component;
    }
    public td1_Port getTd1_port() {
        return td1_port;
    }

    public void setTd1_port(td1_Port td1_port) {
        this.td1_port = td1_port;
    }
    public td1_Program getTd1_program() {
        return td1_program;
    }

    public void setTd1_program(td1_Program td1_program) {
        this.td1_program = td1_program;
    }
    public List<td1_Trigger> getTd1_triggers() {
        return td1_triggers;
    }

    public void addTd1_trigger(Td1_trigger td1_trigger) {
        this.td1_triggers.add(td1_trigger);
    }

}