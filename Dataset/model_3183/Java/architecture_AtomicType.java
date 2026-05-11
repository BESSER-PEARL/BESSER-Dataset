





import java.util.List;
import java.util.ArrayList;

public class architecture_AtomicType  {

    private String atomType;





    private architecture_Operation architecture_operation;




    private architecture_Component architecture_component;




    private architecture_Variable architecture_variable;


    public architecture_AtomicType(
        String atomType    ) {
        this.atomType = atomType;
    }


    public String getAtomtype() {
        return atomType;
    }

    public void setAtomtype(String atomType) {
        this.atomType = atomType;
    }

    public architecture_Operation getArchitecture_operation() {
        return architecture_operation;
    }

    public void setArchitecture_operation(architecture_Operation architecture_operation) {
        this.architecture_operation = architecture_operation;
    }
    public architecture_Component getArchitecture_component() {
        return architecture_component;
    }

    public void setArchitecture_component(architecture_Component architecture_component) {
        this.architecture_component = architecture_component;
    }
    public architecture_Variable getArchitecture_variable() {
        return architecture_variable;
    }

    public void setArchitecture_variable(architecture_Variable architecture_variable) {
        this.architecture_variable = architecture_variable;
    }

}