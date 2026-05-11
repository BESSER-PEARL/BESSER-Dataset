





import java.util.List;
import java.util.ArrayList;

public class fiacre_Component extends EModelElement {

    private String ID;





    private List<fiacre_Variable> fiacre_variables;




    private fiacre_Variable fiacre_variable;




    private List<fiacre_Process> fiacre_processs;


    public fiacre_Component(
        String ID    ) {
        super(
        );
        this.ID = ID;
        this.fiacre_variables = new ArrayList<>();
        this.fiacre_processs = new ArrayList<>();
    }

    public fiacre_Component(
        String ID        ArrayList<fiacre_Variable> fiacre_variables,        ArrayList<fiacre_Process> fiacre_processs    ) {
        this.ID = ID;
        this.fiacre_variables = fiacre_variables;
        this.fiacre_processs = fiacre_processs;
    }

    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }

    public List<fiacre_Variable> getFiacre_variables() {
        return fiacre_variables;
    }

    public void addFiacre_variable(Fiacre_variable fiacre_variable) {
        this.fiacre_variables.add(fiacre_variable);
    }
    public fiacre_Variable getFiacre_variable() {
        return fiacre_variable;
    }

    public void setFiacre_variable(fiacre_Variable fiacre_variable) {
        this.fiacre_variable = fiacre_variable;
    }
    public List<fiacre_Process> getFiacre_processs() {
        return fiacre_processs;
    }

    public void addFiacre_process(Fiacre_process fiacre_process) {
        this.fiacre_processs.add(fiacre_process);
    }

}