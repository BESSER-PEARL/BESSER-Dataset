





import java.util.List;
import java.util.ArrayList;

public class sexec_ExecutionFlow extends ScopedElement, ExecutionNode, ExecutionScope {






    private List<sexec_ExecutionRegion> sexec_executionregions;




    private sexec_Step sexec_step;




    private sexec_Step sexec_step;




    private List<sexec_ExecutionNode> sexec_executionnodes;




    private List<sexec_ExecutionState> sexec_executionstates;




    private sexec_StateVector sexec_statevector;


    public sexec_ExecutionFlow(
    ) {
        super(
        );
        this.sexec_executionregions = new ArrayList<>();
        this.sexec_executionnodes = new ArrayList<>();
        this.sexec_executionstates = new ArrayList<>();
    }

    public sexec_ExecutionFlow(
        ArrayList<sexec_ExecutionRegion> sexec_executionregions,        ArrayList<sexec_ExecutionNode> sexec_executionnodes,        ArrayList<sexec_ExecutionState> sexec_executionstates    ) {
        this.sexec_executionregions = sexec_executionregions;
        this.sexec_executionnodes = sexec_executionnodes;
        this.sexec_executionstates = sexec_executionstates;
    }


    public List<sexec_ExecutionRegion> getSexec_executionregions() {
        return sexec_executionregions;
    }

    public void addSexec_executionregion(Sexec_executionregion sexec_executionregion) {
        this.sexec_executionregions.add(sexec_executionregion);
    }
    public sexec_Step getSexec_step() {
        return sexec_step;
    }

    public void setSexec_step(sexec_Step sexec_step) {
        this.sexec_step = sexec_step;
    }
    public sexec_Step getSexec_step() {
        return sexec_step;
    }

    public void setSexec_step(sexec_Step sexec_step) {
        this.sexec_step = sexec_step;
    }
    public List<sexec_ExecutionNode> getSexec_executionnodes() {
        return sexec_executionnodes;
    }

    public void addSexec_executionnode(Sexec_executionnode sexec_executionnode) {
        this.sexec_executionnodes.add(sexec_executionnode);
    }
    public List<sexec_ExecutionState> getSexec_executionstates() {
        return sexec_executionstates;
    }

    public void addSexec_executionstate(Sexec_executionstate sexec_executionstate) {
        this.sexec_executionstates.add(sexec_executionstate);
    }
    public sexec_StateVector getSexec_statevector() {
        return sexec_statevector;
    }

    public void setSexec_statevector(sexec_StateVector sexec_statevector) {
        this.sexec_statevector = sexec_statevector;
    }

}