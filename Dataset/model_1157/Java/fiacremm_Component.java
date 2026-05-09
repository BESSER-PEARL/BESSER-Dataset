





import java.util.List;
import java.util.ArrayList;

public class fiacremm_Component extends EModelElement {

    private int VarSize;
    private String Name;
    private int ProcessSize;





    private fiacremm_Port fiacremm_port;




    private List<fiacremm_Process> fiacremm_processs;




    private List<fiacremm_Port> fiacremm_ports;




    private fiacremm_Program fiacremm_program;




    private List<fiacremm_Variable> fiacremm_variables;




    private fiacremm_Variable fiacremm_variable;


    public fiacremm_Component(
        int VarSize,        String Name,        int ProcessSize    ) {
        super(
        );
        this.VarSize = VarSize;
        this.Name = Name;
        this.ProcessSize = ProcessSize;
        this.fiacremm_processs = new ArrayList<>();
        this.fiacremm_ports = new ArrayList<>();
        this.fiacremm_variables = new ArrayList<>();
    }

    public fiacremm_Component(
        int VarSize,        String Name,        int ProcessSize        ArrayList<fiacremm_Process> fiacremm_processs,        ArrayList<fiacremm_Port> fiacremm_ports,        ArrayList<fiacremm_Variable> fiacremm_variables    ) {
        this.VarSize = VarSize;
        this.Name = Name;
        this.ProcessSize = ProcessSize;
        this.fiacremm_processs = fiacremm_processs;
        this.fiacremm_ports = fiacremm_ports;
        this.fiacremm_variables = fiacremm_variables;
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
    public int getProcesssize() {
        return ProcessSize;
    }

    public void setProcesssize(int ProcessSize) {
        this.ProcessSize = ProcessSize;
    }

    public fiacremm_Port getFiacremm_port() {
        return fiacremm_port;
    }

    public void setFiacremm_port(fiacremm_Port fiacremm_port) {
        this.fiacremm_port = fiacremm_port;
    }
    public List<fiacremm_Process> getFiacremm_processs() {
        return fiacremm_processs;
    }

    public void addFiacremm_process(Fiacremm_process fiacremm_process) {
        this.fiacremm_processs.add(fiacremm_process);
    }
    public List<fiacremm_Port> getFiacremm_ports() {
        return fiacremm_ports;
    }

    public void addFiacremm_port(Fiacremm_port fiacremm_port) {
        this.fiacremm_ports.add(fiacremm_port);
    }
    public fiacremm_Program getFiacremm_program() {
        return fiacremm_program;
    }

    public void setFiacremm_program(fiacremm_Program fiacremm_program) {
        this.fiacremm_program = fiacremm_program;
    }
    public List<fiacremm_Variable> getFiacremm_variables() {
        return fiacremm_variables;
    }

    public void addFiacremm_variable(Fiacremm_variable fiacremm_variable) {
        this.fiacremm_variables.add(fiacremm_variable);
    }
    public fiacremm_Variable getFiacremm_variable() {
        return fiacremm_variable;
    }

    public void setFiacremm_variable(fiacremm_Variable fiacremm_variable) {
        this.fiacremm_variable = fiacremm_variable;
    }

}