





import java.util.List;
import java.util.ArrayList;

public class td1_Variable  {

    private String initVal;
    private String Name;





    private td1_Process td1_process;




    private td1_Component td1_component;




    private td1_Program td1_program;




    private List<td1_Process> td1_processs;




    private List<td1_Component> td1_components;




    private td1_DataType td1_datatype;




    private td1_Trigger td1_trigger;


    public td1_Variable(
        String initVal,        String Name    ) {
        this.initVal = initVal;
        this.Name = Name;
        this.td1_processs = new ArrayList<>();
        this.td1_components = new ArrayList<>();
    }

    public td1_Variable(
        String initVal,        String Name        ArrayList<td1_Process> td1_processs,        ArrayList<td1_Component> td1_components    ) {
        this.initVal = initVal;
        this.Name = Name;
        this.td1_processs = td1_processs;
        this.td1_components = td1_components;
    }

    public String getInitval() {
        return initVal;
    }

    public void setInitval(String initVal) {
        this.initVal = initVal;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public td1_Process getTd1_process() {
        return td1_process;
    }

    public void setTd1_process(td1_Process td1_process) {
        this.td1_process = td1_process;
    }
    public td1_Component getTd1_component() {
        return td1_component;
    }

    public void setTd1_component(td1_Component td1_component) {
        this.td1_component = td1_component;
    }
    public td1_Program getTd1_program() {
        return td1_program;
    }

    public void setTd1_program(td1_Program td1_program) {
        this.td1_program = td1_program;
    }
    public List<td1_Process> getTd1_processs() {
        return td1_processs;
    }

    public void addTd1_process(Td1_process td1_process) {
        this.td1_processs.add(td1_process);
    }
    public List<td1_Component> getTd1_components() {
        return td1_components;
    }

    public void addTd1_component(Td1_component td1_component) {
        this.td1_components.add(td1_component);
    }
    public td1_DataType getTd1_datatype() {
        return td1_datatype;
    }

    public void setTd1_datatype(td1_DataType td1_datatype) {
        this.td1_datatype = td1_datatype;
    }
    public td1_Trigger getTd1_trigger() {
        return td1_trigger;
    }

    public void setTd1_trigger(td1_Trigger td1_trigger) {
        this.td1_trigger = td1_trigger;
    }

}