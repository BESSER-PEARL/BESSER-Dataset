





import java.util.List;
import java.util.ArrayList;

public class fiacre_Program extends EModelElement {






    private List<fiacre_Component> fiacre_components;




    private List<fiacre_Variable> fiacre_variables;




    private List<fiacre_Process> fiacre_processs;


    public fiacre_Program(
    ) {
        super(
        );
        this.fiacre_components = new ArrayList<>();
        this.fiacre_variables = new ArrayList<>();
        this.fiacre_processs = new ArrayList<>();
    }

    public fiacre_Program(
        ArrayList<fiacre_Component> fiacre_components,        ArrayList<fiacre_Variable> fiacre_variables,        ArrayList<fiacre_Process> fiacre_processs    ) {
        this.fiacre_components = fiacre_components;
        this.fiacre_variables = fiacre_variables;
        this.fiacre_processs = fiacre_processs;
    }


    public List<fiacre_Component> getFiacre_components() {
        return fiacre_components;
    }

    public void addFiacre_component(Fiacre_component fiacre_component) {
        this.fiacre_components.add(fiacre_component);
    }
    public List<fiacre_Variable> getFiacre_variables() {
        return fiacre_variables;
    }

    public void addFiacre_variable(Fiacre_variable fiacre_variable) {
        this.fiacre_variables.add(fiacre_variable);
    }
    public List<fiacre_Process> getFiacre_processs() {
        return fiacre_processs;
    }

    public void addFiacre_process(Fiacre_process fiacre_process) {
        this.fiacre_processs.add(fiacre_process);
    }

}