





import java.util.List;
import java.util.ArrayList;

public class avm_Workflow  {

    private String Name;





    private List<avm_WorkflowTaskBase> avm_workflowtaskbases;




    private avm_TestBench avm_testbench;


    public avm_Workflow(
        String Name    ) {
        this.Name = Name;
        this.avm_workflowtaskbases = new ArrayList<>();
    }

    public avm_Workflow(
        String Name        ArrayList<avm_WorkflowTaskBase> avm_workflowtaskbases    ) {
        this.Name = Name;
        this.avm_workflowtaskbases = avm_workflowtaskbases;
    }

    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public List<avm_WorkflowTaskBase> getAvm_workflowtaskbases() {
        return avm_workflowtaskbases;
    }

    public void addAvm_workflowtaskbase(Avm_workflowtaskbase avm_workflowtaskbase) {
        this.avm_workflowtaskbases.add(avm_workflowtaskbase);
    }
    public avm_TestBench getAvm_testbench() {
        return avm_testbench;
    }

    public void setAvm_testbench(avm_TestBench avm_testbench) {
        this.avm_testbench = avm_testbench;
    }

}