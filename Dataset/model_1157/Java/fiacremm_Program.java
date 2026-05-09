





import java.util.List;
import java.util.ArrayList;

public class fiacremm_Program extends EModelElement {

    private int ComponentSize;
    private String Name;





    private List<fiacremm_DataType> fiacremm_datatypes;




    private List<fiacremm_Variable> fiacremm_variables;




    private List<fiacremm_Process> fiacremm_processs;


    public fiacremm_Program(
        int ComponentSize,        String Name    ) {
        super(
        );
        this.ComponentSize = ComponentSize;
        this.Name = Name;
        this.fiacremm_datatypes = new ArrayList<>();
        this.fiacremm_variables = new ArrayList<>();
        this.fiacremm_processs = new ArrayList<>();
    }

    public fiacremm_Program(
        int ComponentSize,        String Name        ArrayList<fiacremm_DataType> fiacremm_datatypes,        ArrayList<fiacremm_Variable> fiacremm_variables,        ArrayList<fiacremm_Process> fiacremm_processs    ) {
        this.ComponentSize = ComponentSize;
        this.Name = Name;
        this.fiacremm_datatypes = fiacremm_datatypes;
        this.fiacremm_variables = fiacremm_variables;
        this.fiacremm_processs = fiacremm_processs;
    }

    public int getComponentsize() {
        return ComponentSize;
    }

    public void setComponentsize(int ComponentSize) {
        this.ComponentSize = ComponentSize;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public List<fiacremm_DataType> getFiacremm_datatypes() {
        return fiacremm_datatypes;
    }

    public void addFiacremm_datatype(Fiacremm_datatype fiacremm_datatype) {
        this.fiacremm_datatypes.add(fiacremm_datatype);
    }
    public List<fiacremm_Variable> getFiacremm_variables() {
        return fiacremm_variables;
    }

    public void addFiacremm_variable(Fiacremm_variable fiacremm_variable) {
        this.fiacremm_variables.add(fiacremm_variable);
    }
    public List<fiacremm_Process> getFiacremm_processs() {
        return fiacremm_processs;
    }

    public void addFiacremm_process(Fiacremm_process fiacremm_process) {
        this.fiacremm_processs.add(fiacremm_process);
    }

}